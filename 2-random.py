import random

uniqNumber = random.randint(1,10)

# print(uniqNumber)

a = None
tries = 0

while uniqNumber != a:
    a = int(input())
    tries += 1

    if uniqNumber > a:
        print("Too low!")
    elif uniqNumber <a:
        print("Too high!")
    else:
        print("your guss is write")
        print("tries" ,tries)


