#!/usr/bin/python3
from uuid import uuid1, uuid3, uuid4, uuid5

for i in range(5):
    my_id = str(uuid1())
    print(my_id)
print("*" * 50)
for i in range(5):
    my_id = str(uuid4())
    print(my_id)
