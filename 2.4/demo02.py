import httpx

r = httpx.get("https://www.httpbin.org/get")
print(r.status_code)
print(r.headers)
print(r.text)
