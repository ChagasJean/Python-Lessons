'''
Flag = To mark a location
NONE = is not a value
id = identity is where the variable is stored within memory
'''

# v1 = 'a'
# print(id(v1))

condition = False
passed_if = None

if condition:
    passed_if = True
    print('do something')
else:
    print("don't do something")

if passed_if is None:
    print("Did not pass if.")
else:
    print('Passed if')
