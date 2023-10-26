
'''
Explanation about try except:

try -> tries to execute the code
except -> an error occurred when trying to execute
'''

num_str = input('I will double the number you enter: ')

try:
    print('STR:', num_str)
    num_float = float(num_str)
    print('FLOAT:', num_float)
    print('Twice {} is {:.1f}'.format(num_str, num_float * 2))
except:
    print('This is not a number!')

# if num_str.isdigit():
#    num_float = float(num_str)
#    print('Twice {} is {:.1f}'.format(num_str, num_float * 2))
# else:
#    print('This is not a number!')
