import requests
import json


def getcity(c): 
    response = requests.get('https://api.teleport.org/api/cities/?search={}'.format(c))
    jsonObject = response.json()
    #_embedded: object
        #city:search-results : array
            #_links: object
                #city:item : object
                    #href : string
    if '_embedded' in jsonObject:
        if 'city:search-results' in jsonObject['_embedded']:
            if len(jsonObject['_embedded']['city:search-results']) > 1:
                p = jsonObject['_embedded']['city:search-results'][0]['_links']['city:item']['href'][46:53]
                r = requests.get('https://api.teleport.org/api/cities/geonameid%3A{}'.format(p))
                jsonObj2 = r.json()
                print('Full name:', jsonObj2['full_name'])
                print('Population:', jsonObj2['population'])
    else:
        print('No known city')

# Get city input from user CHECK
# Get 'https://api.teleport.org/api/cities/?search=CITY' CHECK
# Parse for geonameid:NUM  CHECK
# return geonameid:NUM CHECK
# Get https://api.teleport.org/api/cities/geonameid%3ACITYID/ CHECK
# %3AC is : 
# Parse for population CHECK
# Parse for name CHECK
# Display it to user CHECK


# Shove city name and population into database
# On request, give user top 5 populous cities

if __name__ == '__main__':
    city = input()

    getcity(city)