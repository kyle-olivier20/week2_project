import requests
import json
import pandas as pd
import sqlalchemy as db

def convert_into_database(dictionary):
    # taken from codio don't know how to use
    engine = db.create_engine('sqlite:///data_base_name.db')
    dataframe_name.to_sql('table_name', con=engine, 
    if_exists='replace', index=False)
    query_result = engine.execute("SELECT * FROM table;").fetchall()
    print(pd.DataFrame(query_result))
    # convert dictionary to a DATABASE will need Jhermey or kyle kinda struggling 
    return 



def get_top_3_populations(DATABASE): # focus on convert_into_database 
                                     # this is easier
    # loop through database get top 3 populations
    # print top three populations 
    # <- new funciton(print populations)

def get_lower_3_populations(DATABASE):
    # loop through database get bottom 3 populations
    # print bottom three populations 
    # <- new funciton(print populations)

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
                    # consider taking the print statment out?
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

def getcities():
    dictionary = {}
    first_input = 'yes'
    while first_input != 'no':
        x = getcity()
        dictionary[x[0]] = x[1]
        first_input = int(input('Do you want to add another city?(enter yes or no)'))
    return dictionary

# Shove city name and population into database
# On request, give user top 5 populous cities

if __name__ == '__main__':
    print('This Program finds the bottom three or bottom three city populations')

    # propbably could be made in anothre function from here
    population_dictionary = getcities()
    NEW_DATABASE = convert_into_database(population_dictionary)

    # to here and return database
    print('Do you want bottom three populations or top three populations')
    choice = select_choice
    if choice[0] = 'top':
        get_top_3_populations(NEW_DATABASE)
    else:
        get_lower_3_populations(NEW_DATABASE)
