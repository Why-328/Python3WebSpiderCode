import httpx

with httpx.Client() as client:
    response = client.get("https://httpbin.org/get")
    print(response)

# 两种方法运行结果是一样的，只不过下面的方法需要显示地调用close方法来关闭Client对象

client = httpx.Client()
try:
    response = client.get("https://httpbin.org/get")
    print(response)
finally:
    client.close()
