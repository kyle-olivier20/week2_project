import requests
import json
import pandas as pd
import sqlalchemy as db

col_names = ['City', 'Population', 'geonameid']
df  = pd.DataFrame(columns=col_names)


def getcity():
    city = str(input("Enter City Name: "))
    p = ''
    n = ''
    pop = 0
    i = False
    while i is not True:
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
                    n = jsonObj2['full_name']
                    pop = jsonObj2['population']
                    # consider taking the print statment out?
                    print('Full name:', n)
                    print('Population:', pop)
                    i = True
        else:
            city = str(input("ERROR: No known city, try again: "))
    df.loc[len(df.index)] = [n, pop, p]


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
    first_input = 'yes'
    while first_input != 'no':
        x = getcity()
        first_input = str(input('Do you want to add another city?(enter yes or no)'))


def print_cities():
    for i in range(len(df)):
        print(df.loc[i, :])
# Shove city name and population into database
# On request, give user top 5 populous cities


if __name__ == '__main__':
    print('This Program finds the bottom three or bottom three city populations')

    # propbably could be made in anothre function from here
    getcities()
    print_cities()

    # to here and return database
    # print('Do you want bottom three populations or top three populations')
    # choice = select_choice
    # # if choice[0] = 'top':
    # #     get_top_3_populations(NEW_DATABASE)
    # # else:
    # #     get_lower_3_populations(NEW_DATABASE)
