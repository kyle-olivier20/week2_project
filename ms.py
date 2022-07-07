import requests
import json
import pandas as pd
import sqlalchemy as db

def convert_into_database(dictionary):
    # convert dictionary to a DATABASE will need Jhermey 

def get_top_3_populations(DATABASE):
    # loop through database get top 3 databases

def get_lower_3_populations(DATABASE):
    # loop through database get bottom 3 populations

def select_choice():
    choice = str(input('Enter bottom or top'))
    while choice == "":
        choice = str(input("ERROR: No choice entered, try again: "))
    return choice

def getcity(): 
    city = str(input("Enter City Name: "))
    population = 0
    i = False
    while i != True:
        response = requests.get('https://api.teleport.org/api/cities/?search={}'.format(city))
        jsonObject = response.json()
        #_embedded: object
            #city:search-results : array
                #_links: object
                    #city:item : object
                        #href : string
        if '_embedded' in jsonObject:
            if 'city:search-results' in jsonObject['_embedded']:
                if len(jsonObject['_embedded']['city:search-results']) > 0:
                    p = jsonObject['_embedded']['city:search-results'][0]['_links']['city:item']['href'][46:53]
                    r = requests.get('https://api.teleport.org/api/cities/geonameid%3A{}/'.format(p))
                    jsonObj2 = r.json()
                    name = jsonObj2['full_name']
                    population =jsonObj2['population']
                    print('Full name:', name)
                    print('Population:', population)
                    i = True
        else:
            city = str(input("ERROR: No known city, try again: "))
    return [name,population]


# Get city input from user CHECK reprompt user if wrong
# Get 'https://api.teleport.org/api/cities/?search=CITY' CHECK
# Parse for geonameid:NUM  CHECK
# return geonameid:NUM CHECK
# Get https://api.teleport.org/api/cities/geonameid%3ACITYID/ CHECK
# %3AC is : 
# Parse for population CHECK
# Parse for name CHECK
# Display it to user CHECK
# returns a list of 


# Shove city name and population into database
# On request, give user top 5 populous cities

if __name__ == '__main__':
    engine = db.create_engine('sqlite:///data_base_name.db')

    print('This Program finds the bottom three or bottom three city populations')

    # propbably could be made in anothre function from here
    first_input = 'yes'
    dictionary = {}
    while first_input != 'no':
        x = getcity()
        dictionary[x[0]] = x[1]
        first_input = int(input('Do you want to add another city?(enter yes or no)'))
    # to here and return database
    print('Do you want bottom three populations or top three populations')

    DATABASE = convert_into_database(dictionary)
    choice = select_choice
    if choice[0] = 'top':
        get_top_3_populations(DATABASE)
    else:
        get_lower_3_populations(DATABASE)
