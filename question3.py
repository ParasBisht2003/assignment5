import random

i=0

string = "123456789"

r = 0
w = 0

while i<10:
    a = int(random.choice(string))
    b = int(random.choice(string))
    ans = int(input(f"Question {i+1}:  {a} x {b} = "))

    if (ans==a*b):
        print("Right.\n")
        r = r+1
    else:
        print(f"Wrong. The answer is {a*b}\n")
        w = w+1

    i = i+1

print(f"You scored {r*10}%")