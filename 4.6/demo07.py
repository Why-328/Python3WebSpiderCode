from redis import StrictRedis

# 创建一个 redis 客户端对象
r = StrictRedis(host='localhost', port=6379, db=0, password='123456')


# sadd: 向集合中添加一个或多个元素，如果元素已存在，则忽略。返回添加成功的元素个数。
def sadd(key, *values):
    return r.sadd(key, *values)


# srem: 从集合中移除一个或多个元素，如果元素不存在，则忽略。返回移除成功的元素个数。
def srem(key, *values):
    return r.srem(key, *values)


# spop: 随机弹出集合中的一个元素，并返回它。如果集合为空，则返回 None。
def spop(key):
    return r.spop(key)


# smove: 将一个元素从一个集合移动到另一个集合，并返回 True。如果元素不存在于源集合，或目标集合已存在该元素，则返回 False。
def smove(src, dst, value):
    return r.smove(src, dst, value)


# scard: 返回集合中的元素个数。
def scard(key):
    return r.scard(key)


# sismember: 判断一个元素是否属于集合，如果是，则返回 True，否则返回 False。
def sismember(key, value):
    return r.sismember(key, value)


# sinter: 返回多个集合的交集，即同时属于这些集合的元素。
def sinter(*keys):
    return r.sinter(*keys)


# sinterstore: 将多个集合的交集存储到一个新的集合中，并返回该集合的元素个数。
def sinterstore(dst, *keys):
    return r.sinterstore(dst, *keys)


# sunion: 返回多个集合的并集，即至少属于其中一个集合的元素。
def sunion(*keys):
    return r.sunion(*keys)


# sunionstore: 将多个集合的并集存储到一个新的集合中，并返回该集合的元素个数。
def sunionstore(dst, *keys):
    return r.sunionstore(dst, *keys)


# sdiff: 返回多个集合的差集，即属于第一个集合但不属于其他集合的元素。
def sdiff(*keys):
    return r.sdiff(*keys)


# sdiffstore: 将多个集合的差集存储到一个新的集合中，并返回该集合的元素个数。
def sdiffstore(dst, *keys):
    return r.sdiffstore(dst, *keys)


# smembers: 返回集合中的所有元素。
def smembers(key):
    return r.smembers(key)


# srandmember: 随机返回集合中的一个或多个元素，如果指定了 count 参数，则返回 count 个不重复的元素，如果 count 为负数，则返回 count 个可能重复的元素。
def srandmember(key, count=None):
    return r.srandmember(key, count)


if __name__ == '__main__':
    # 测试示例
    print(sadd('set1', 'a', 'b', 'c'))  # 返回 3
    print(sadd('set1', 'a', 'd'))  # 返回 1
    print(srem('set1', 'a', 'b'))  # 返回 2
    print(srem('set1', 'e', 'f'))  # 返回 0
    print(spop('set1'))  # 返回 'c'
    print(spop('set2'))  # 返回 None
    print(sadd('set1', 'a', 'b', 'c'))
    print(sadd('set2', 'd', 'e', 'f'))
    print(smove('set1', 'set2', 'a'))  # 返回 True
    print(smove('set1', 'set2', 'g'))  # 返回 False
    print(scard('set1'))  # 返回 2
    print(scard('set2'))  # 返回 4
    print(sismember('set1', 'b'))  # 返回 True
    print(sismember('set1', 'd'))  # 返回 False
    print(sadd('set3', 'c', 'd', 'e'))
    print(sinter('set1', 'set2', 'set3'))  # 返回 {'c'}
    print(sinterstore('set4', 'set1', 'set2', 'set3'))  # 返回 1
    print(sunion('set1', 'set2', 'set3'))  # 返回 {'b', 'c', 'd', 'e', 'f'}
    print(sunionstore('set5', 'set1', 'set2', 'set3'))  # 返回 5
    print(sdiff('set1', 'set2', 'set3'))  # 返回 {'b'}
    print(sdiffstore('set6', 'set1', 'set2', 'set3'))  # 返回 1
    print(smembers('set1'))  # 返回 {'b', 'c'}
    print(srandmember('set2'))  # 返回 'd'
    print(srandmember('set2', 2))  # 返回 ['e', 'f']
    print(srandmember('set2', -2))  # 返回 ['d', 'd']
