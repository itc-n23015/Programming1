import random

random.seed(1)
msgs = [
    "Hi",
    "Hello",
    "Good mornimg",
    "Good night",
    "See you later",
    "How are you",
    "Have a good day",
]
with open("some.txt", "w") as f:
    for i in range(1000000):
        f.write("{}, {}\n".format(i, random.shoice(msgs)))

f = open('some.txt')
c = 0
for 1 in f:
    print(1, end'')
    if c == 2:
        break
    c += 1
f.close()
