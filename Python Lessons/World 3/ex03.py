'''
MAKE A PROGRAM THAT ASKS FOR THE USER'S FIRST NAME. IF THE NAME IS 4 LETTERS OR LESS, WRITE "YOUR NAME IS SHORT"; IF IT HAS BETWEEN 5 AND 6 LETTERS, WRITE "YOUR NAME IS NORMAL"; GREATER THAN 6, WRITE "YOUR NAME IS TOO BIG".
'''

name = input("What's your name? ")

count = len(name)

count1 = count <= 4
count2 = count == 5 or count <= 6
count3 = count > 6

if count1:
    print('Your name is short!')
elif count2:
    print('Your name is normal!')
elif count3:
    print('Your name is too big')
