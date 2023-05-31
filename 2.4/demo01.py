import requests

r = requests.get("https://spa16.scrape.center/", verify=False)
print(r.status_code)
print(r.text)
