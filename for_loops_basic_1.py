# Basic
for x in range(151):
    print(x)

print('Prediction: prints number 1-151')
# prints numbers 1-151

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

print("Prediction: alternates between printing 'dojo' and 'coding dojo' 10x each.")

# Whoa, that sucker's huge
for x in range(50000):
    odd_sum = 0
    if (x % 2 != 0):
        odd_sum += x
print(odd_sum)

print("prediction: sums all odd numbers from 0-50000 and prints the result.")

# Countdown by fours
for x in range(2018, 0, -4):
    print(x)

print("Prediction: prints a countdown from 2018-0. Counts down by four.")

# Flexible counter
lowNum = 1
highNum = 50
mult = 2

for x in range(lowNum, highNum, mult):
    print(x)

print("Prediction: prints all odd numbers from 1-50.")
