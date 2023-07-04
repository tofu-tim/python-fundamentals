num1 = 42 #number

num2 = 2.3 #float

boolean = True #boolean

string = 'Hello World' #string

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list

person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary

fruit = ('blueberry', 'strawberry', 'banana') #array

print(type(fruit)) #type check

print(pizza_toppings[1]) #print selected value from array

pizza_toppings.append('Mushrooms') #edit array

print(person['name']) #accesses and prints value

person['name'] = 'George' #changes value

person['eye_color'] = 'blue' #adds value

print(fruit[2]) #prints selected value from array

if num1 > 45:
    print("It's greater") #if statement
else:
    print("It's lower") #else statement



if len(string) < 5:
    print("It's a short word!") #if statement
elif len(string) > 15:
    print("It's a long word!") #elif statement
else:
    print("Just right!") #else statement

for x in range(5): #for loop 
    print(x) #prints 0,1,2,3,4

for x in range(2,5): #for loop
    print(x) #prints 2,3,4

for x in range(2,10,3): #for loop prints ranger 2-10 in increments of 3
    print(x) #prints 2, 5, 8

x = 0
while(x < 5): #while loop: prints x, than increase x by 1 as long as x<5. once x=5, loop breaks.
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1) # deletes value from list.

print(person) #prints entire dictionary

person.pop('eye_color') #removes value from dictionary

print(person) #prints dictionary sans eye color

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break #for loop. prints 'After 1st if statement' until list reaches "olives".

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times() #prints hello ten times

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #prints hello four times

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()  #prints hello ten times
print_hello_x_or_ten_times(4) #prints hello four times


"""
Bonus section
"""

print(num3)
num3 = 72 #name error

fruit[0] = 'cranberry' #type error

print(person['favorite_team']) #key error

print(pizza_toppings[7]) #index error

print(boolean) #prints True

fruit.append('raspberry') #AttributeError: 'tuple' object has no attribute 'append'

fruit.pop(1) #AttributeError: 'tuple' object has no attribute 'pop'