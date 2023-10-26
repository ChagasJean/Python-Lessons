'''
MAKE A PROGRAM THAT ASKS FOR THE USER'S FIRST NAME. IF THE NAME IS 4 LETTERS OR LESS, WRITE "YOUR NAME IS SHORT"; IF IT HAS BETWEEN 5 AND 6 LETTERS, WRITE "YOUR NAME IS NORMAL"; GREATER THAN 6, WRITE "YOUR NAME IS TOO BIG".
'''

name = input("What's your name? ")

count = len(name)

if count <= 4:
    print('Your name is short!')
elif count == 5 or count <= 6:
    print('Your name is normal!')
elif count > 6:
    print('Your name is too big')
