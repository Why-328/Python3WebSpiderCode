from redis import StrictRedis, ConnectionPool

url = 'redis://:123456@localhost:6379/0'
pool = ConnectionPool.from_url(url)
redsi = StrictRedis(connection_pool=pool)
redsi.set('name', 'Bob')
print(redsi.get('name'))
