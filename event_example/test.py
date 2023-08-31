# coding:utf-8

import json
from deepdiff import DeepDiff

json1 = '{"name": "Alice", "age": 30}'
json2 = '{"age": 30, "name": "Alice"}'
json3 = '{"name": "Bob", "age": 30}'

obj1 = json.loads(json1)
obj2 = json.loads(json2)
obj3 = json.loads(json3)

print(obj1)
print(obj1 == obj2)
print(obj1 == obj3)


diff = DeepDiff(obj1, obj2, ignore_order=True)
print(diff)

path = 'upfMap/upf-s/nfProfile/t3Addr'
path = path.split('/')
for item in path:
    if not item:
        print("lhb")
        continue
    else:
        print("item: %s" % item)


even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)

even_numbers_new = []
for x in range(1, 11):
    if x % 2 == 0:
        even_numbers_new.append(x)
else:
    print("even numbers: %s" % even_numbers_new)