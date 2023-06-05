from redis import StrictRedis

# 创建一个 redis 客户端对象
r = StrictRedis(host='localhost', port=6379, db=0, password='123456')


# 在列表的左侧插入一个或多个值，返回列表的长度，如果键不存在则先创建并设为空列表再插入
def lpush(key, *values):
    return r.lpush(key, *values)


# 实例：在列表 fruits 的左侧插入 apple 和 banana
lpush('fruits', 'apple', 'banana')
print(f"lpush:{r.lrange('fruits', 0, -1)}")


# 返回：2

# 在列表的右侧插入一个或多个值，返回列表的长度，如果键不存在则先创建并设为空列表再插入
def rpush(key, *values):
    return r.rpush(key, *values)


# 实例：在列表 fruits 的右侧插入 orange 和 lemon
rpush('fruits', 'orange', 'lemon')
print(f"rpush:{r.lrange('fruits', 0, -1)}")


# 返回：4

# 获取列表的长度，如果键不存在则返回 0
def llen(key):
    return r.llen(key)


# 实例：获取列表 fruits 的长度
print(f"llen:{llen('fruits')}")


# 返回：4

# 获取列表中指定范围内的值，返回一个列表，如果键不存在则返回空列表
def lrange(key, start, end):
    return r.lrange(key, start, end)


# 实例：获取列表 fruits 中索引从 0 到 -1 的值
print(f"lrange:{lrange('fruits', 0, -1)}")


# 返回：[b'banana', b'apple', b'orange', b'lemon']

# 截取列表中指定范围内的元素，并保留在原键中，其他元素被删除，如果键不存在则不做任何操作
def ltrim(key, start, end):
    r.ltrim(key, start, end)


# 实例：截取列表 fruits 中索引从 0 到 1 的元素，并保留在原键中
ltrim('fruits', 0, 1)
print(f"ltrim:{r.lrange('fruits', 0, -1)}")


# 返回：True

# 获取列表中指定索引的值，如果索引超出范围则返回 None
def lindex(key, index):
    return r.lindex(key, index)


# 实例：获取列表 fruits 中索引为 1 的值
print(f"lindex:{lindex('fruits', 1)}")


# 返回：b'apple'

# 设置列表中指定索引的值，如果索引超出范围或键不存在则报错
def lset(key, index, value):
    r.lset(key, index, value)


# 实例：设置列表 fruits 中索引为 0 的值为 cherry
lset('fruits', 0, 'cherry')
print(f"lset:{lindex('fruits', 0)}")


# 返回：True

# 删除列表中等于指定值的元素，可以指定删除的个数，返回删除的元素个数，如果键不存在则返回 0
def lrem(key, count, value):
    return r.lrem(key, count, value)


# 实例：删除列表 fruits 中等于 cherry 的元素，最多删除 1 个
lrem('fruits', 1, 'cherry')
print(f"lrem:{r.lrange('fruits', 0, -1)}")


# 返回：1

# 从列表的左侧弹出一个值，并返回该值，如果列表为空或不存在则返回 None
def lpop(key):
    return r.lpop(key)


# 实例：从列表 fruits 的左侧弹出一个值
print(f"lpop:{lpop('fruits')}")


# 返回：b'banana'

# 从列表的右侧弹出一个值，并返回该值，如果列表为空或不存在则返回 None
def rpop(key):
    return r.rpop(key)


# 实例：从列表 fruits 的右侧弹出一个值
print(f"rpop:{rpop('fruits')}")


# 返回：None

# 从指定的多个列表中按顺序从左侧弹出第一个非空元素，并返回该元素和所属的键，如果所有列表都为空或不存在则阻塞指定的时间，如果超时则返回 None
def blpop(*keys, timeout=0):
    return r.blpop(*keys, timeout=timeout)


# 实例：从列表 fruits 中按顺序从左侧弹出第一个非空元素，阻塞 10 秒
print(f"blpop:{blpop('fruits', timeout=10)}")


# 从指定的多个列表中按顺序从右侧弹出第一个非空元素，并返回该元素和所属的键，如果所有列表都为空或不存在则阻塞指定的时间，如果超时则返回 None
def brpop(*keys, timeout=0):
    return r.brpop(*keys, timeout=timeout)


# 实例：从列表 fruits 中按顺序从右侧弹出第一个非空元素，阻塞 10 秒
print(f"brpop:{brpop('fruits', timeout=10)}")


# 返回：(b'vegetables', b'carrot')

# 从一个列表的右侧弹出一个值，并将该值插入到另一个列表的左侧，返回该值，如果源列表为空或不存在则阻塞指定的时间，如果超时则返回 None
def rpoplpush(src, dst):
    return r.rpoplpush(src, dst)


# 实例：从列表 fruits 的右侧弹出一个值，并将该值插入到列表 vegetables 的左侧
print(rpoplpush('fruits', 'vegetables'))
# 返回：b'orange'