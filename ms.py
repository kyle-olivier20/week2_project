import requests
import json

city = input()

response = requests.get('https://api.teleport.org/api/cities/?search={}'.format(city))

'''print(json.dumps(response.json(), indent=4))'''

jsonObject = response.json()
#_embedded: object
    #city:search-results : array
        #_links: object
            #city:item : object
                #href : string


if '_embedded' in jsonObject:
    if 'city:search-results' in jsonObject['_embedded']:
        if len(jsonObject['_embedded']['city:search-results']) > 1:
            print(jsonObject['_embedded']['city:search-results'][0]['_links']['city:item']['href'][46:53])



# Get city input from user CHECK
# Get 'https://api.teleport.org/api/cities/?search=CITY' CHECK
# Parse for geonameid:NUM  CHECK
# return geonameid:NUM CHECK
# Get https://api.teleport.org/api/cities/geonameid%3ACITYID/
# %3AC is :
# Parse for population
# Parse for name
# Display it to user

# Shove city name and population into database
# On request, give user top 5 populous cities