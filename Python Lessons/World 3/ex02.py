'''
MAKE A PROGRAM THAT ASKS THE USER THE TIME AND, BASED ON THE TIME DESCRIBED, DISPLAY THE APPROPRIATE GREETING. EX.
Good morning 0-11, Good afternoon 12-17 and Good evening 18-23
'''

name = input("What's your name? ")
hour = input('What time is it? ')

try:
    hour2 = int(hour)

    morning = hour2 == 0 or hour2 <= 11
    afternoon = hour2 == 12 or hour2 <= 17
    night = hour2 == 18 or hour2 <= 23

    if morning:
        print('Good morning, {}'.format(name))

    elif afternoon:
        print('Good afternoon, {}'.format(name))

    elif night:
        print('Good night, {}'.format(name))
    else:
        print('Invalid time.')
except:
    print('Invalid value. Only enter whole numbers.')
