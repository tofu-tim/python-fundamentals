# Basic
for x in range(151):
    print(x)

#multiples of 5
for x in range(5, 1001, 5):
    print(x)

# Counting, the Dojo way
for x in range(101):
    if (x % 10 == 0):
        print('Coding Dojo')
    elif (x % 5 == 0):
        print('Coding')
    else:
        print(x)

# Whoa, that sucker's huge
for x in range(50000):
    odd_sum = 0
    if (x % 2 != 0):
        odd_sum += x
print(odd_sum)

# Countdown by fours
for x in range(2018, 0, -4):
    print(x)

# Flexible counter
lowNum = 1
highNum = 50
mult = 2

for x in range(lowNum, highNum, mult):
    print(x)

