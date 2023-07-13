#the function takes an array and reverses the order of it's indexes.

def reverse_array(array):
    reversed_array = []
    for x in array[::-1]:
        reversed_array.append(x)
    return reversed_array

print(reverse_array([1,2,3,4,5,6,7,8,9]))
