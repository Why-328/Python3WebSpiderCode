from redis import StrictRedis

# 创建一个 redis 客户端对象
r = StrictRedis(host='localhost', port=6379, db=0, password='123456')


# 设置一个键的值，如果键已存在则覆盖，如果键不存在则创建
def set(key, value):
    r.set(key, value)


# 实例：设置键 name 的值为 Alice
set('name', 'Alice')


# 返回：True

# 获取一个键的值，如果键不存在则返回 None
def get(key):
    return r.get(key)


# 实例：获取键 name 的值
print(get('name'))


# 返回：b'Alice'

# 设置一个键的值，并返回该键的旧值，如果键不存在则返回 None
def getset(key, value):
    return r.getset(key, value)


# 实例：设置键 name 的值为 Bob，并返回旧值
print(getset('name', 'Bob'))


# 返回：b'Alice'

# 获取多个键的值，返回一个列表，如果某个键不存在则返回 None
def mget(*keys):
    return r.mget(*keys)


# 实例：获取键 name 和 age 的值
print(mget('name', 'age'))


# 返回：[b'Bob', None]

# 设置一个键的值，只有当该键不存在时才生效，返回 True 或 False
def setnx(key, value):
    return r.setnx(key, value)


# 实例：设置键 name 的值为 Carol
if setnx('name', 'Carol'):
    print('True')
else:
    print('False')


# 返回：False

# 设置一个键的值，并为该键设置过期时间，单位为秒
def setex(key, seconds, value):
    r.setex(key, seconds, value)


# 实例：设置键 name 的值为 David，并设置 10 秒的过期时间
if setex('name', 10, 'David'):
    print('True')
else:
    print('False')


# 返回：True

# 用指定的字符串覆盖给定键所储存的字符串值，从偏移量 offset 开始
def setrange(key, offset, value):
    return r.setrange(key, offset, value)


# 实例：用 "Eve" 覆盖键 name 所储存的字符串值，从偏移量 1 开始
setrange('name', 1, 'Evee')
print(r.get('name'))


# 返回：4,修改后的字符串长度

# 同时设置多个键的值，返回 True 或 False
def mset(data):
    return r.mset(data)


# 实例：同时设置键 name 的值为 Frank 和 age 的值为 20
mset({'name': 'Frank', 'age': 20})
print(f"name:{r.get('name')},age:{r.get('age')}")


# 返回：True

# 同时设置多个键的值，只有当所有给定键都不存在时才生效，返回 True 或 False
def msetnx(data):
    return r.msetnx(data)


def msetnx(data):
    return r.msetnx(data)


# 实例：同时设置键 name 的值为 Grace 和 gender 的值为 F
msetnx({'name': 'Grace', 'gender': 'F'})
print(f"name:{r.get('name')},gender:{r.get('gender')}")


# 返回：False

# 将一个键所储存的数字值增一，返回增加后的结果，如果该键不存在则先创建并设为 0 再增一，如果该键不是数字类型则报错
def incr(key):
    return r.incr(key)


# 实例：将键 age 所储存的数字值增一
print('递增前:', r.get('age'))
incr('age')
print('递增后:', r.get('age'))


# 返回：21

# 将一个键所储存的数字值减一，返回减少后的结果，如果该键不存在则先创建并设为 0 再减一，如果该键不是数字类型则报错
def decr(key):
    return r.decr(key)


# 实例：将键 age 所储存的数字值减一
print('减少前:', r.get('age'))
decr('age')
print('减少后:', r.get('age'))


# 返回：20

# 将一个字符串追加到一个已存在的字符串末尾，返回追加后字符串的长度，如果该键不存在则先创建并设为空字符串再追加
def append(key, value):
    return r.append(key, value)


# 实例：将字符串 " Jr." 追加到键 name 所储存的字符串末尾
append('name', ' Jr.')


# 返回：7

# 获取一个键所储存的字符串值的子字符串，返回子字符串，如果该键不存在则返回空字符串
def substr(key, start, end):
    return r.substr(key, start, end)


# 实例：获取键 name 所储存的字符串值的子字符串，从偏移量 0 到 3
print(substr('name', 0, 3))


# 返回：b'Fran'

# 获取一个键所储存的字符串值的指定范围内的子字符串，返回子字符串，如果该键不存在则返回空字符串
def getrange(key, start, end):
    return r.getrange(key, start, end)


# 实例：获取键 name 所储存的字符串值的指定范围内的子字符串，从偏移量 1 到 -1
print(getrange('name', 1, -1))
# 返回：b'rank Jr.'
