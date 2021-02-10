from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

from email.message import EmailMessage
import requests

import smtplib
from concurrent.futures import ThreadPoolExecutor
email_rest = []

class ActionSearchRestaurants(Action):

    config = {"user_key": "43a9a75029a9bfced3fe385d54bf2355"}

    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        zomato = zomatopy.initialize_app(self.config)
        # Get location from slot
        loc = tracker.get_slot('location')

        # Get cuisine from slot
        cuisine = tracker.get_slot('cuisine')
        
        # Get the budget from the slot
        cost_min = int(tracker.get_slot('budgetmin'))
        cost_max = int(tracker.get_slot('budgetmax'))
        
        results, lat, lon = self.get_location_suggestions(loc,zomato)

        is_restaurant_exist = False
        if (results == 0):
            # No results for this location
            dispatcher.utter_message("Sorry, no results found in this location:("+ "\n")
        else:
            try:
                rest = self.get_restaurants(lat, lon, cost_min, cost_max, cuisine)

                # Filter the results based on budget
                budget = [rest_single for rest_single in rest if ((rest_single['restaurant']['average_cost_for_two'] > cost_min) & (rest_single['restaurant']['average_cost_for_two'] < cost_max))]
                # Sorting the results 
                budget_rating_sorted = sorted(budget, key=lambda k: k['restaurant']['user_rating']['aggregate_rating'], reverse=True)

                # Build the response
                response = ""
                is_restaurant_exist = False
                if len(budget_rating_sorted) == 0:
                    dispatcher.utter_message("Sorry, no results found :("+ "\n")
                else:
                    # Pick the top 5
                    budget_rating_top5 = budget_rating_sorted[:5]
                    global email_rest
                    email_rest = budget_rating_sorted[:10]
                    if(email_rest and len(email_rest) > 0):
                        is_restaurant_exist = True
                    for restaurant in budget_rating_top5:
                        response = response + restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address'] + \
                            " has been rated " + \
                            restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n" + "\n"
                    dispatcher.utter_message("These are the top restaurants!"+ "\n" + response)
            except:
                dispatcher.utter_message("Sorry, no results found :("+ "\n")
        return [SlotSet('location', loc), SlotSet('restaurant_exist', is_restaurant_exist)]

    def get_location_suggestions(self, loc, zomato):
        # Get location details including latitude and longitude
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = 0
        lon = 0
        results = len(d1["location_suggestions"])
        if (results > 0):
            lat = d1["location_suggestions"][0]["latitude"]
            lon = d1["location_suggestions"][0]["longitude"]
        return results, lat, lon

    def get_restaurants(self, lat, lon, budgetmin, budgetmax , cuisine):
        cuisines_dict = {'american': 1, 'chinese': 25, 'italian': 55,
                         'mexican': 73, 'north indian': 50, 'south indian': 85}
        rest = []
        executor = ThreadPoolExecutor(max_workers=5)
        for res_key in range(0, 101, 20):
            executor.submit(retrieve_restaurant, lat, lon, cuisines_dict, cuisine, res_key, rest)
        executor.shutdown()
        return rest
    
class VerifyLocation(Action):

    tier = []

    def __init__(self):
        self.tier = ['ahmedabad', 'bangalore', 'chennai', 'delhi', 'hyderabad', 'kolkata', 'mumbai', 'pune','agra', 'ajmer', 'aligarh', 'allahabad', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bokaro steel city', 'chandigarh', 'coimbatore', 'cuttack', 'dehradun', 'dhanbad', 'durg-bhilai nagar', 'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gurgaon', 'guwahati', 'gwalior', 'hubli-dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kannur', 'kanpur', 'kakinada', 'kochi', 'kottayam', 'kolhapur', 'kollam', 'kota', 'kozhikode', 'kurnool', 'lucknow', 'ludhiana', 'madurai', 'malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'noida', 'palakkad', 'patna', 'pondicherry', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli', 'siliguri', 'solapur', 'srinagar', 'sultanpur', 'surat', 'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tirunelveli', 'tiruppur', 'ujjain', 'vijayapura', 'vadodara', 'varanasi', 'vasai-virar city', 'vijayawada', 'visakhapatnam', 'warangal']
    def name(self):
        return "verify_location"
    
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        if not (self.verify_location(loc)):
            dispatcher.utter_message("We do not operate in this city yet. Please try some other city.")
            return [SlotSet('location', None), SlotSet("location_ok", False)]
        else:
            return [SlotSet('location', loc), SlotSet("location_ok", True)]

    def verify_location(self, loc):
        try:
            return loc.lower() in self.tier
        except:
            return
        
class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'
        
    def run(self, dispatcher, tracker, domain):
        # Get user's email id
        to_email = tracker.get_slot('emailid')

        dispatcher.utter_message(to_email)
        # Getting location and cuisines to put in the email
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        global email_rest
        email_rest_count = len(email_rest)
        # Construct the email 'subject' and the contents.
        email_subj = "Top " + str(email_rest_count) + " " + cuisine.capitalize() + " restaurants in " + str(loc).capitalize()

        email_msg = "Hi there! Here are the " + email_subj + "." + "\n" + "\n" +"\n"
        for restaurant in email_rest:
            email_msg = email_msg + restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n" +"\n"

        # Open SMTP connection to our email id.
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login("sectyn.maria@gmail.com", "TestPassword123")

        # Create the msg object
        msg = EmailMessage()

        # Fill in the message properties
        msg['Subject'] = email_subj
        msg['From'] = "sectyn.maria@gmail.com"

        # Fill in the message content
        msg.set_content(email_msg)
        msg['To'] = to_email

        s.send_message(msg)
        s.quit()
        dispatcher.utter_message("**** Email has been sent ****")
        return []


class VerifyBudget(Action):

    def name(self):
        return "verify_budget"

    def run(self, dispatcher, tracker, domain):
        budgetmin = None
        budgetmax = None
        error_msg = "This price range is not supported. Select another option."
        try:
            budgetmin = int(tracker.get_slot('budgetmin'))
            budgetmax = int(tracker.get_slot('budgetmax'))
        except ValueError:
            dispatcher.utter_message(error_msg)
            return [SlotSet('budgetmin', None), SlotSet('budgetmax', None), SlotSet('budget_ok', False)]
        min_dict = [0, 300, 700]
        max_dict = [300, 700]
        if budgetmin in min_dict and (budgetmax in max_dict or budgetmax > 700):
            return [SlotSet('budgetmin', budgetmin), SlotSet('budgetmax', budgetmax), SlotSet('budget_ok', True)]
        else:
            dispatcher.utter_message(error_msg)
            return [SlotSet('budgetmin', 0), SlotSet('budgetmax', 10000), SlotSet('budget_ok', False)]

class VerifyCuisine(Action):

    def name(self):
        return "verify_cuisine"

    def run(self, dispatcher, tracker, domain):
        cuisines = ['chinese','mexican','italian','american','south indian','north indian']
        error_msg = "This cuisine is not supported. Select another option."
        cuisine = tracker.get_slot('cuisine')
        try:
            cuisine = cuisine.lower()
        except (RuntimeError, TypeError, NameError, AttributeError):
            dispatcher.utter_message(error_msg)
            return [SlotSet('cuisine', None), SlotSet('cuisine_ok', False)]
        if cuisine in cuisines:
            return [SlotSet('cuisine', cuisine), SlotSet('cuisine_ok', True)]
        else:
            dispatcher.utter_message(error_msg)
            return [SlotSet('cuisine', None), SlotSet('cuisine_ok', False)]

def retrieve_restaurant(lat, lon, cuisines_dict, cuisine, res_key, rest):
    base_url = "https://developers.zomato.com/api/v2.1/"
    headers = {'Accept': 'application/json',
                'user-key': '43a9a75029a9bfced3fe385d54bf2355'}
    try:
        results = (requests.get(base_url + "search?" + "&lat=" + str(lat) + "&lon=" + str(lon) + "&cuisines=" + str(cuisines_dict.get(cuisine)) + "&start=" + str(res_key)+"&count=20", headers=headers).content).decode("utf-8")
    except:
        return
    d = json.loads(results)
    rest.extend(d['restaurants'])