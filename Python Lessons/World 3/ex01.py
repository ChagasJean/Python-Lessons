'''
MAKE A PROGRAM THAT ASKS THE USER TO TYPE A WHOLE NUMBER, INFORM IF THIS NUMBER IS EVEN OR ODD. IF THE USER DOES NOT TYPE A WHOLE NUMBER, INFORM THAT IT IS NOT A WHOLE NUMBER.
'''

num = input('Enter a value: ')

try:
    num_int = int(num)

    if num_int % 2 == 0:
        print('This number is even.')
    else:
        print('This number is not even.')
except:
    print('This number is not integer.')
