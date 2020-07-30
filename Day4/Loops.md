```

>>> user_1 = {'username': 'Mk', 'id': 1}
>>> user_2 = {'username': 'abc', 'id': 2, 'email': 'abc@abc.abc'}
>>> print(my_users)
[{'username': 'jmitchel3', 'id': 1}, {'username': 'abc', 'id': 2}]
>>> my_users = [user_1, user_2]
>>> print(my_users)
[{'username': 'jmitchel3', 'id': 1}, {'username': 'abc', 'id': 2, 'email': 'abc@abc.abc'}]
>>> for user in my_users:
...     print(user['email'])
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyError: 'email'
>>> for user in my_users:
...     if 'email' in user:
...         print(user['email'])
... 
abc@abc.abc
>>> selected_user = {}
>>> my_user_lookup = 2
>>> for user in my_users:
...     if 'id' in user:
...        if user['id'] == my_user_lookup:
...           selected_user = user
... 
>>> print(selected_user)
{'username': 'abc', 'id': 2, 'email': 'abc@abc.abc'}
>>> for x in range(0, 10):
...    print(x)
... 
0
1
2
3
4
5
6
7
8
9
>>> for x in range(0, 10):
...    for user in my_users:
...        if user['id'] == x:
...           print(user)
... 
{'username': 'jmitchel3', 'id': 1}
{'username': 'abc', 'id': 2, 'email': 'abc@abc.abc'}
```
