"""Generate 20 activation keys and store them in a Redis database.
Using uuid.
code in Python2"""
import uuid
import random
import redis
activation_key = []

r = redis.StrictRedis(host = 'localhost', port=6379,db =0)
for i in range(1,21):  #generate 20 codes
    name = str(random.random())
    key = uuid.uuid3(uuid.NAMESPACE_DNS,name)
    activation_key.append(key)
    r.set(i,key)       #store in the database
print activation_key
for i in range(1,21):
    print r.get(i) # read from database
