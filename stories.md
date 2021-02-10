## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "wayanad"}
    - slot{"location": "wayanad"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - verify_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "10000"}
    - slot{"budgetmax": "10000"}
    - slot{"budgetmin": "700"}
    - verify_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "sectyn@gmail.com"}
    - slot{"emailid": "sectyn@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - verify_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "10000"}
    - slot{"budgetmax": "10000"}
    - slot{"budgetmin": "700"}
    - verify_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "sectyn@gmail.com"}
    - slot{"emailid": "sectyn@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "vasai-virar city"}
    - slot{"cuisine": "italian"}
    - slot{"location": "vasai-virar city"}
    - verify_location
    - slot{"location": "vasai-virar city"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "0", "budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - slot{"budgetmin": "0"}
    - verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "vasai-virar city"}
    - slot{"restaurant_exist": false}
    - utter_goodbye
    - action_restart

## interactive_story_4
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai", "location": "delhi"}
    - slot{"cuisine": "thai"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "10000"}
    - slot{"budgetmax": "10000"}
    - slot{"budgetmin": "700"}
    - verify_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* dont_send_email
    - utter_goodbye
    - action_restart


## interactive_story_5
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "wayanad"}
    - slot{"location": "wayanad"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - verify_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "10000"}
    - slot{"budgetmax": "10000"}
    - slot{"budgetmin": "700"}
    - verify_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "maria.manoj24@gmail.com"}
    - slot{"emailid": "maria.manoj24@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_6
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - verify_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* thankyou
    - utter_goodbye
    - action_restart

## interactive_story_7
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - verify_location
    - slot{"location": "Allahabad"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "10000"}
    - slot{"budgetmax": "10000"}
    - slot{"budgetmin": "700"}
    - verify_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Allahabad"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "maximus.smgs@gmail.com"}
    - slot{"emailid": "maximus.smgs@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_8
* greet
    - utter_greet
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - verify_location
    - slot{"location": "chandigarh"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - verify_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "0", "budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - slot{"budgetmin": "0"}
    - verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* dont_send_email
    - utter_goodbye
    - action_restart

## interactive_story_9
* greet
    - utter_greet
* restaurant_search{"location": "durg-bhilai nagar"}
    - slot{"location": "durg-bhilai nagar"}
    - verify_location
    - slot{"location": "durg-bhilai nagar"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "0", "budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - slot{"budgetmin": "0"}
    - verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "durg-bhilai nagar"}
    - slot{"restaurant_exist": false}
    - utter_goodbye
    - action_restart

## interactive_story_10
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - verify_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - verify_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* dont_send_email
    - utter_goodbye
    - action_restart

## interactive_story_11
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "hubli-dharwad"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "hubli-dharwad"}
    - verify_location
    - slot{"location": "hubli-dharwad"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "10000"}
    - slot{"budgetmax": "10000"}
    - slot{"budgetmin": "700"}
    - verify_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "hubli-dharwad"}
    - slot{"restaurant_exist": false}
    - utter_goodbye
    - action_restart



## interactive_story_12 - continued with action_restart
* affirm
    - utter_ask_howcanhelp
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "briyani"}
    - slot{"cuisine": "briyani"}
    - verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "500", "budgetmax": "900"}
    - slot{"budgetmax": "900"}
    - slot{"budgetmin": "500"}
    - verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": false}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "sectyn@gmail.com"}
    - slot{"emailid": "sectyn@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_13 - after action restart being continued - starts with utter_ask_howcanhelp
    - utter_ask_howcanhelp
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "500", "budgetmax": "500"}
    - slot{"budgetmax": "500"}
    - slot{"budgetmin": "500"}
    - verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": false}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - utter_ask_budget
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "sectyn@gmail.com"}
    - slot{"emailid": "sectyn@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_14
* affirm
    - utter_ask_howcanhelp
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - verify_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* dont_send_email
    - utter_goodbye
    - action_restart

## interactive_story_15
* affirm
    - utter_ask_howcanhelp
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - verify_location
    - slot{"location": "allahabad"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - verify_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "allahabad"}
    - slot{"restaurant_exist": false}
    - utter_goodbye
    - action_restart
