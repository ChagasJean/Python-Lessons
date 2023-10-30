counter = 0

while counter <= 100:
    counter += 1

    if counter == 6:
        print("I won't show 6.")
        continue

    if counter >= 10 and counter <= 20:
        continue

    print(counter)

    if counter == 40:
        break


print("Finish")
