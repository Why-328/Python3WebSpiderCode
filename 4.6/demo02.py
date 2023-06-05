from redis import StrictRedis, ConnectionPool

pool = ConnectionPool(host='localhost', port=6379, db=0, password='123456')
redis = StrictRedis(connection_pool=pool)
redis.set('name', 'Bob')
print(redis.get('name'))
