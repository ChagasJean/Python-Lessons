'''
MAKE A PROGRAM THAT ASKS THE USER THE TIME AND, BASED ON THE TIME DESCRIBED, DISPLAY THE APPROPRIATE GREETING. EX.
Good morning 0-11, Good afternoon 12-17 and Good evening 18-23
'''

name = input("What's your name? ")
hour = int(input('What time is it? '))

morning = hour == 0 or hour <= 11
afternoon = hour == 12 or hour <= 17
night = hour == 18 or hour <= 23


if morning:
    print('Good morning, {}'.format(name))

elif afternoon:
    print('Good afternoon, {}'.format(name))

elif night:
    print('Good night, {}'.format(name))
