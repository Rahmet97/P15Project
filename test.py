import redis


r = redis.Redis(host='localhost', port=6379, db=0)

r.delete('key', 'mylist', 'myset', 'myhashset')
r.set('key', '49')  # str malumotlarni saqlash

r.lpush('mylist', 'A5', 'A4', 'A3', 'A2')  # list malumotlarni saqlash

r.sadd('myset', 9, 8, 12, 100, 13)  # set malumotlarni saqlash

r.hset('myhashset', 'key1', 'value1')
r.hset('myhashset', 'key2', 'value2')
r.hset('myhashset', 'key3', 'value3')