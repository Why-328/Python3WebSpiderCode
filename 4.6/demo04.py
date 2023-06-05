from redis import StrictRedis

# 创建一个 redis 客户端对象
r = StrictRedis(host='localhost', port=6379, db=0, password='123456')


# 判断一个键是否存在，返回 True 或 False
def exists(key):
    return r.exists(key)


# 实例：判断键 name 是否存在
r.set('name', 'Bob')
r.set('age', 22)
print(exists('name'))


# 删除一个或多个键，返回删除的键的数量
def delete(*keys):
    return r.delete(*keys)


# 实例：删除键 name 和 age
print(delete('name', 'age'))


# 查看一个键的类型，返回字符串表示，如 string, hash, list, set, zset 等
def type(key):
    return r.type(key)


# 实例：查看键 scores 的类型
r.set('score', 100)
print(type('scores'))


# 查找符合给定模式的所有键，返回一个列表
def keys(pattern):
    return r.keys(pattern)


# 实例：查找以 user 开头的所有键
r.set('user1', 'a')
r.set('user2', 'b')
print(keys('user*'))


# 随机返回一个键，如果数据库为空则返回 None
def randomkey():
    return r.randomkey()


# 实例：随机返回一个键
print(randomkey())


# 重命名一个键，如果新键已存在则覆盖，如果旧键不存在则报错
def rename(oldkey, newkey):
    r.rename(oldkey, newkey)


# 实例：将键 name 重命名为 username
r.set('name', 'Bob')
rename('name', 'username')
print(r.get('username'))


# 返回当前数据库的键的数量
def dbsize():
    return r.dbsize()


# 实例：返回当前数据库的键的数量
print(dbsize())


# 为一个键设置过期时间，单位为秒，返回 True 或 False
def expire(key, seconds):
    return r.expire(key, seconds)


# 实例：为键 username 设置 10 秒的过期时间
expire('username', 10)


# 查看一个键的剩余过期时间，单位为秒，如果键不存在或没有设置过期时间则返回 -1
def ttl(key):
    return r.ttl(key)


# 实例：查看键 username 的剩余过期时间
print(ttl('username'))


# 将一个键从当前数据库移动到另一个数据库，返回 True 或 False
def move(key, db):
    return r.move(key, db)


# 实例：将键 username 从数据库 0 移动到数据库 1
print(f"移动前{r.get('username')}")
move('username', 1)
print(f"移动后{r.get('username')}")


# 清空当前数据库中的所有键，返回 True 或 False
def flushdb():
    return r.flushdb()


# 实例：清空当前数据库中的所有键
flushdb()


# 清空所有数据库中的所有键，返回 True 或 False
def flushall():
    return r.flushall()


# 实例：清空所有数据库中的所有键
flushall()
