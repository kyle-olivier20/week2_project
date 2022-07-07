USE cities;
INSERT INTO cityname (geonameid, name, population)
VALUES (jsonObject['_embedded']['city:search-results'][0]['_links']['city:item']['href'][46:53], jsonObj2['full_name'], jsonObj2['population']);