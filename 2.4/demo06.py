import httpx

r = httpx.get('https://httpbin.org/get', params={'name': 'germy'})
print(r)
r = httpx.post('https://httpbin.org/post', data={'name': 'germy'})
print(r)
r = httpx.put('https://httpbin.org/put')
print(r)
r = httpx.delete('https://httpbin.org/delete')
print(r)
r = httpx.patch('https://httpbin.org/patch')
print(r)
