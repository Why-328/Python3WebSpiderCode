import httpx

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OSX 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
response = httpx.get("https://www.httpbin.org/get",headers = headers)
print(response.text)