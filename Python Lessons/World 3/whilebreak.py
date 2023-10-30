"""
Reps
while
Performs an action while a condition is true
"""

condition = int(input('Enter "1" to start the program or "0" to exit: '))


if condition == 1:
    while condition:
        name = input("What's your name? ").capitalize()

        if name == "Jean":
            print("Little gay of Colêgio.")
        elif name == 'Lucas':
            print("Pure white and German.")
        elif name == 'Enzo':
            print("From God's city.")
        elif name == 'Quit':
            print("END OF PROGRAM!")
            break
        else:
            print("I do not know that one.")
elif condition == 0:
    print("NOTHING WILL HAPPEN!")
