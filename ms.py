import requests
import json

# to get city input
city = input()


response = requests.get('https://api.teleport.org/api/cities/?search={}'.format(city))
jsonObject = response.json()
#_embedded: object
    #city:search-results : array
        #_links: object
            #city:item : object
                #href : string

# to get the geonameid
if '_embedded' in jsonObject:
    if 'city:search-results' in jsonObject['_embedded']:
        if len(jsonObject['_embedded']['city:search-results']) > 1:
            print(jsonObject['_embedded']['city:search-results'][0]['_links']['city:item']['href'][36:53])

#to get the correct city in mind
p = jsonObject['_embedded']['city:search-results'][0]['_links']['city:item']['href'][46:53]
r = requests.get('https://api.teleport.org/api/cities/geonameid%3A{}'.format(p))

# to get full name and population
jsonObj2 = r.json()
print('Full name:', jsonObj2['full_name'])
print('Population:', jsonObj2['population'])


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