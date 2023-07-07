# Countdown - Create a function that accepts a number as an input.
# Return a new list that counts down by one, from the number
# (as the 0th element) down to 0 (as the last element).

# Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(number):
    result = []
    for i in range(number, -1, -1):
        result.append(i)
    return result

print('Countdown')
print(countdown(10))

# Print and Return - Create a function that will receive a list
# with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(num1, num2):
    print(num1)
    return num2

print('Print and return')
print(print_and_return(10, 5))


# First Plus Length - Create a function that accepts a list and
# returns the sum of the first value in the list plus the list's length.

# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length(test_array_1):
    first = test_array_1[0]
    length = len(test_array_1)
    return (first+length)

print('First plus length')
print(first_plus_length([1, 1, 2, 3, 5, 1, 8, 6, 4, 5]))


# Values Greater than Second - Write a function that accepts a
# list and creates a new list containing only the values from the
# original list that are greater than its 2nd value. Print how
# many values this is and then return the new list. If the list
# has less than 2 elements, have the function return False

# Example: values_greater_than_second([5,2,3,2,1,4]) should
# print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def values_greater_than_second(test_array_2):
    new_array = []
    if len(test_array_2) <= 2:
        return False
    else:
        for i in range(0, len(test_array_2), 1):
            if test_array_2[i] > test_array_2[1]:
                new_array.append(test_array_2[i])
    return new_array

print('Values greater than second')
print(values_greater_than_second([1, 1, 2, 3, 5, 1, 8, 6, 4, 5]))


# This Length, That Value - Write a function that accepts two
# integers as parameters: size and value. The function should
# create and return a list whose length is equal to the given
# size, and whose values are all the given value.

# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(param1, param2):
    new_array = []
    for i in range(param1):
        new_array.append(param2)
    return new_array

print('Length and values')
print(length_and_value(10, 1))