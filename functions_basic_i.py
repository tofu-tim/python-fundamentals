#1
def number_of_food_groups():
    return 5
print(number_of_food_groups()) #prints 5


2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches()) #prints error.

# 'number_of_days_in_a_week_silicon_or_triangle_sides()' not defined.

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold()) #prints 10


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers()) #prints 10


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x) #prints 5


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3)) #prints 8


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5)) #prints 25


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents()) #prints 10, 7


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) #prints 7, 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #prints 14, 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #prints 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5)) #prints 8

#11
b = 500
print(b) #prints 500
def foobar():
    b = 300
    print(b)
print(b) #prints 500
foobar() #prints 300
print(b) #prints 500


#12
b = 500
print(b) #prints 500
def foobar():
    b = 300
    print(b)
    return b
print(b) #prints 500
foobar() #prints 300
print(b) #prints 300

#13
b = 500
print(b) #prints 500
def foobar():
    b = 300
    print(b)
    return b
print(b) #prints 500
b=foobar()
print(b) #prints 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo() #prints 1 3

print("hello")

#15
def foo():
    print(1) #prints 1
    x = bar()
    print(x) #prints 3 5
    return 10 #prints 10
def bar():
    print(3)
    return 5
y = foo()
print(y) #prints 1 3 5 10
