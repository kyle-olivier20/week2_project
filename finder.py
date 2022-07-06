import requests
import urllib.parse

url = "https://images.plurk.com/32B15UXxymfSMwKGTObY5e.jpg"
api_url='https://api.trace.moe/search'

requests.get("{}?url={}".format(api_url,urllib.parse.quote_plus(url))).json()

requests.post(f"{api_url}", data=open("demo.jpg", "rb"),headers={"Content-Type": "image/jpeg"}).json()

requests.post(f"{api_url}", files={"image": open("demo.jpg", "rb")}).json()

requests.get("{}?cutBorders&url={}".format(api_url,urllib.parse.quote_plus(url))).json()

requests.get("{}?anilistID=1&url={}".format(api_url,urllib.parse.quote_plus(url))).json()

requests.get("https://api.trace.moe/search?anilistInfo&url={}".format(urllib.parse.quote_plus("https://images.plurk.com/32B15UXxymfSMwKGTObY5e.jpg"))).json()
