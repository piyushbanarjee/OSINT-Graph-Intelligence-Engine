def x():
    return 13, 233

r1= x()

r2, r3 = x()

r4 = x()[0]
r5 = x()[1]
print(r1, r2, r3, r4, r5)