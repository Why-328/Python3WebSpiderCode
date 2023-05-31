import httpx

client = httpx.Client(http2=True, verify=False)
r = client.get("https://spa16.scrape.center/")
print(r.text)
