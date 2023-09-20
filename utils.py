import redis

r = redis.Redis(host='localhost', port=6379, db=0)

#  str elementlarni o'qib olish
# value = r.get('key')
# print(value.decode('utf-8'))

#  list elementlarini o'qib olish
# items = r.lrange('mylist', 0, -1)
# for item in items:
#     print(item.decode('utf-8'))

#  set elementlarini o'qib olish
# members = r.smembers('myset')
# for member in members:
#     print(member.decode('utf-8'))

#  hashset(dict) elementlarini o'qib olish
myhashset = r.hgetall('myhashset')
for key, value in myhashset.items():
    print(key.decode('utf-8'), value.decode('utf-8'))


field1 = r.hget('myhashset', 'key1')
print(field1.decode('utf-8'))
