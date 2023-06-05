from redis import StrictRedis

# 创建一个 redis 客户端对象
r = StrictRedis(host='localhost', port=6379, db=0, password='123456')


# zadd: 向有序集合中添加一个或多个元素，如果元素已存在，则更新其分数。返回添加成功的元素个数。
def zadd(key, mapping):
    return r.zadd(key, mapping)


# zrem: 从有序集合中移除一个或多个元素，如果元素不存在，则忽略。返回移除成功的元素个数。
def zrem(key, *values):
    return r.zrem(key, *values)


# zincrby: 将有序集合中指定元素的分数增加指定的值，并返回新的分数。如果元素不存在，则添加该元素并将其分数设为指定的值。
def zincrby(key, amount, value):
    return r.zincrby(key, amount, value)


# zrank: 返回有序集合中指定元素的排名，即按照分数从小到大排序时的索引，从 0 开始。如果元素不存在，则返回 None。
def zrank(key, value):
    return r.zrank(key, value)


# zrevrank: 返回有序集合中指定元素的排名，即按照分数从大到小排序时的索引，从 0 开始。如果元素不存在，则返回 None。
def zrevrank(key, value):
    return r.zrevrank(key, value)


# zrange: 返回有序集合中指定索引范围内的元素，按照分数从小到大排序。如果指定了 withscores 参数，则返回元素及其分数。索引可以是正数或负数，正数表示从头开始，负数表示从尾开始，-1 表示最后一个元素。
def zrange(key, start, end, withscores=False):
    return r.zrange(key, start, end, withscores)


# zrevrange: 返回有序集合中指定索引范围内的元素，按照分数从大到小排序。如果指定了 withscores 参数，则返回元素及其分数。索引可以是正数或负数，正数表示从头开始，负数表示从尾开始，-1 表示最后一个元素。
def zrevrange(key, start, end, withscores=False):
    return r.zrevrange(key, start, end, withscores)


# zrangebyscore: 返回有序集合中指定分数范围内的元素，按照分数从小到大排序。如果指定了 withscores 参数，则返回元素及其分数。分数范围可以用圆括号或方括号表示开区间或闭区间，如 (2,5] 表示大于 2 小于等于 5 的分数区间。如果指定了 limit 参数，则返回指定偏移量和数量的元素。
def zrangebyscore(key, min_, max_, withscores=False, limit=None):
    return r.zrangebyscore(key, min_, max_, withscores, limit)


# zrevrangebyscore: 返回有序集合中指定分数范围内的元素，按照分数从大到小排序。如果指定了 withscores 参数，则返回元素及其分数。分数范围可以用圆括号或方括号表示开区间或闭区间，如 (2,5] 表示大于 2 小于等于 5 的分数区间。
def zrevrangebyscore(key, max_, min_, withscores=False):
    return r.zrevrangebyscore(key, max_, min_, withscores)


# zcount: 返回有序集合中指定分数范围内的元素个数。分数范围可以用圆括号或方括号表示开区间或闭区间，如 (2,5] 表示大于 2 小于等于 5 的分数区间。
def zcount(key, min_, max_):
    return r.zcount(key, min_, max_)


# zcard: 返回有序集合中的元素个数。
def zcard(key):
    return r.zcard(key)


# zremrangebyrank: 移除有序集合中指定排名范围内的元素，并返回移除的元素个数。排名按照分数从小到大排序，索引可以是正数或负数，正数表示从头开始，负数表示从尾开始，-1 表示最后一个元素。
def zremrangebyrank(key, start, end):
    return r.zremrangebyrank(key, start, end)


# zremrangebyscore: 移除有序集合中指定分数范围内的元素，并返回移除的元素个数。分数范围可以用圆括号或方括号表示开区间或闭区间，如 (2,5] 表示大于 2 小于等于 5 的分数区间。
def zremrangebyscore(key, min_, max_):
    return r.zremrangebyscore(key, min_, max_)


if __name__ == '__main__':
    # 测试示例
    print(zadd('zset1', {'a': 1, 'b': 2, 'c': 3}))  # 返回 3
    print(zadd('zset1', {'a': 4, 'd': 5}))  # 返回 1
    print(zrem('zset1', 'a', 'b'))  # 返回 2
    print(zrem('zset1', 'e', 'f'))  # 返回 0
    print(zincrby('zset1', 2, 'a'))  # 返回 3.0
    print(zincrby('zset1', -1, 'b'))  # 返回 1.0
    print(zincrby('zset1', 4, 'd'))  # 返回 4.0
    print(zrank('zset1', 'a'))  # 返回 0
    print(zrank('zset1', 'c'))  # 返回 2
    print(zrank('zset1', 'e'))  # 返回 None
    print(zrevrank('zset1', 'a'))  # 返回 2
    print(zrevrank('zset1', 'c'))  # 返回 0
    print(zrevrank('zset1', 'e'))  # 返回 None
    print(zrange('zset1', 0, -1))  # 返回 ['a', 'b', 'c']
    print(zrange('zset1', 1, 2))  # 返回 ['b', 'c']
    print(zrange('zset1', -2, -1))  # 返回 ['b', 'c']
    print(zrange('zset1', 0, -1, withscores=True))  # 返回 [('a', 3.0), ('b', 4.0), ('c', 5.0)]
    print(zrevrange('zset1', 0, -1))  # 返回 ['c', 'b', 'a']
    print(zrevrange('zset1', 1, 2))  # 返回 ['b', 'a']
    print(zrevrange('zset1', -2, -1))  # 返回 ['b', 'a']
    print(zrevrange('zset1', 0, -1, withscores=True))  # 返回 [('c', 5.0), ('b', 4.0), ('a', 3.0)]
    print(r.zrevrangebyscore('zset1', '+inf', '(2'))  # 返回 ['c']
    print(r.zrevrangebyscore('zset1', '(3', '-inf'))  # 返回 ['a', 'b']
    print(r.zrevrangebyscore('zset1', '+inf', '(2', withscores=True))  # 返回 [(b'd', 9.0), (b'c', 3.0)]
    print(r.zcount('zset1', '(2', '+inf'))  # 返回 2
    print(r.zcount('zset1', '-inf', '(3'))  # 返回 2
    print(r.zcard('zset1'))  # 返回 4
    print(r.zremrangebyrank('zset1', 0, 1))  # 返回 2
    print(r.zremrangebyrank('zset1', -2, -1))  # 返回 2
    print(r.zremrangebyscore('zset1', '(2', '+inf'))  # 返回 0
    print(r.zremrangebyscore('zset1', '-inf', '(3'))  # 返回 0
