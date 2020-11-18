import requests
import random
import sys

#----------------------------------------
# Make a HTTP GET request to cat-fact API
cat_url = "https://cat-fact.herokuapp.com/facts"
r = requests.get(cat_url)
r_obj_list = r.json()["all"]

#----------------------------------------
# Create an empty list to store facts
# This makes it easy to select one random
fact_list = []

#-----------------------------------------
# Add "text" of every object into the list
for fact in r_obj_list:
  fact_list.append( fact["text"] )
  
#-------------------------------
# Select a random text from list
def select_random_fact(fact_arr):
  return fact_arr[random.randint(0, len(fact_list)+1)]
random_fact = select_random_fact(fact_list)

#----------------------
# Print the random text
print(random_fact)

#--------------------------------------------------------------
# Set the fact-output of the action as the value of random_fact
print(f"::set-output name=fact::{random_fact}")
