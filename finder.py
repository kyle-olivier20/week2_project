import requests
import urllib.parse

requests.get("https://api.trace.moe/search?url={}".format(urllib.parse.quote_plus("https://images.plurk.com/32B15UXxymfSMwKGTObY5e.jpg"))).json()

requests.post("https://api.trace.moe/search", data=open("demo.jpg", "rb"),headers={"Content-Type": "image/jpeg"}).json()

requests.post("https://api.trace.moe/search", files={"image": open("demo.jpg", "rb")}).json()

requests.get("https://api.trace.moe/search?cutBorders&url={}".format(urllib.parse.quote_plus("https://images.plurk.com/32B15UXxymfSMwKGTObY5e.jpg"))).json()

requests.get("https://api.trace.moe/search?anilistID=1&url={}".format(urllib.parse.quote_plus("https://images.plurk.com/32B15UXxymfSMwKGTObY5e.jpg"))).json()

requests.get("https://api.trace.moe/search?anilistInfo&url={}".format(urllib.parse.quote_plus("https://images.plurk.com/32B15UXxymfSMwKGTObY5e.jpg"))).json()
