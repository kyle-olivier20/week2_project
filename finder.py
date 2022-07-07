import requests
import pandas as pd

# creating data frame to add data to
col_names = ['Title', 'Author', 'Link']
df = pd.DataFrame(columns = col_names)

# get most recent post ID
response = requests.get("https://hacker-news.firebase\
io.com/v0/maxitem.json?print=pretty")
mostRecent = response.json()

#loop through the last 100 posts and add only stories to dataframe
response = requests.get("https://hacker-news.firebaseio.com/v0/item/"+str(mostRecent)+".json?print=pretty")
data = response.json()
for i in range(int(mostRecent)-100, int(mostRecent)-1):
    if data is not None and data['type'] == 'story' and 'title' in data and 'by' in data and 'url' in data:
    # Adding as new row to dataframe
    df.loc[len(df.index)] = [data['title'], data['by'], data['url']]
    print("Added " + data['title'])
  mostRecent = int(mostRecent) - 1
  response = requests.get("https://hacker-news.firebaseio.com/v0/item/"+str(mostRecent)+".json?print=pretty")
  data = response.json()
