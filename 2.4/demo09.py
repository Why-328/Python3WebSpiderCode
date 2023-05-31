import httpx

client = httpx.Client(http2=True, verify=False)
response = client.get('https://httpbin.org/get')
print(response.text)
print(response.http_version)
