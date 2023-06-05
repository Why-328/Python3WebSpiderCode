import redis
from redis import StrictRedis

# 创建一个 redis 客户端对象
r = StrictRedis(host='localhost', port=6379, db=0, password='123456')


# hset: 将散列中指定字段的值设为指定的值，如果字段不存在，则创建该字段。返回 1 表示设置成功，返回 0 表示字段已存在且值未改变。
def hset(key, field, value):
    return r.hset(key, field, value)


# hsetnx: 将散列中指定字段的值设为指定的值，如果字段不存在，则创建该字段。如果字段已存在，则不做任何操作。返回 1 表示设置成功，返回 0 表示字段已存在。
def hsetnx(key, field, value):
    return r.hsetnx(key, field, value)


# hget: 返回散列中指定字段的值，如果字段不存在，则返回 None。
def hget(key, field):
    return r.hget(key, field)


# hmget: 返回散列中多个指定字段的值，如果某个字段不存在，则返回 None。
def hmget(key, *fields):
    return r.hmget(key, *fields)


# hmset: 将散列中多个指定字段的值设为指定的值，如果某个字段不存在，则创建该字段。返回 True 表示设置成功。
def hmset(key, mapping):
    return r.hmset(key, mapping)


# hincrby: 将散列中指定字段的值增加指定的整数，并返回新的值。如果字段不存在，则创建该字段并将其值设为指定的整数。如果字段的值不是整数，则报错。
def hincrby(key, field, amount):
    return r.hincrby(key, field, amount)


# hexists: 判断散列中是否存在指定的字段，如果存在，则返回 True，否则返回 False。
def hexists(key, field):
    return r.hexists(key, field)


# hdel: 删除散列中一个或多个指定的字段，并返回删除成功的字段个数。如果某个字段不存在，则忽略。
def hdel(key, *fields):
    return r.hdel(key, *fields)


# hlen: 返回散列中的字段个数。
def hlen(key):
    return r.hlen(key)


# hkeys: 返回散列中的所有字段名称。
def hkeys(key):
    return r.hkeys(key)


# hvals: 返回散列中的所有字段值。
def hvals(key):
    return r.hvals(key)


# hgetall: 返回散列中的所有字段和值，以字典的形式返回。
def hgetall(key):
    return r.hgetall(key)


if __name__ == '__main__':
    # 测试示例
    print(hset('hash1', 'name', 'Alice'))  # 返回 1
    print(hset('hash1', 'age', 18))  # 返回 1
    print(hset('hash1', 'name', 'Alice'))  # 返回 0
    print(hsetnx('hash1', 'name', 'Bob'))  # 返回 0
    print(hsetnx('hash1', 'gender', 'female'))  # 返回 1
    print(hget('hash1', 'name'))  # 返回 'Alice'
    print(hget('hash1', 'height'))  # 返回 None
    print(hmget('hash1', 'name', 'age', 'gender'))  # 返回 ['Alice', 18, 'female']
    print(hmget('hash1', 'name', 'height'))  # 返回 ['Alice', None]
    print(hmset('hash1', {'name': 'Bob', 'age': 19}))  # 返回 True
    print(hincrby('hash1', 'age', 2))  # 返回 21
    print(hincrby('hash1', 'score', 10))  # 返回 10
    try:
        print(hincrby('hash1', 'name', 1))
    except redis.RedisError as e:
        print(f"hincrby('hash1', 'name', 1):{e}")  # 报错 hash value is not an integer
    print(hexists('hash1', 'name'))  # 返回 True
    print(hexists('hash1', 'height'))  # 返回 False
    print(hdel('hash1', 'name', 'age'))  # 返回 2
    print(hdel('hash1', 'height'))  # 返回 0
    print(hlen('hash1'))  # 返回 2
    print(hkeys('hash1'))  # 返回 ['gender', 'score']
    print(hvals('hash1'))  # 返回 ['female', 10]
    print(hgetall('hash1'))  # 返回 {'gender': 'female', 'score': 10}
