import httpx

r = httpx.get("https://spa16.scrape.center/", verify=False)
print(r.text)
