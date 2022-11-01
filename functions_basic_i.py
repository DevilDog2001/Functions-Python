#1
def number_of_food_groups():
    return 5
print(number_of_food_groups()) #OutPut 5


#2
#def number_of_military_branches():
    #return 5
#print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches()) #OutPut Error because of first function does not exist in print statement.


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold()) #OutPut 5 becuase the first return = 5 and that is the final return what comes after does not output


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())   #OutPut 5 because there us a return statement and what comes after does not output


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)                     #OutPut None 


#6
def add(b,c):
    print(b+c)
print(add(1,2) , add(2,3))   #OutPut 3 and 5 seprate lines and none none


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))   #OutPut 25 


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())  #OutPut printed out b which is equal to 100 and returned 10 due to if statement


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))   #OutPut returned 7 due to if statement then other if statement and added the 2 if statements of 7 & 14 to get last output 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))  #OutPut gave first return statement of b+c and thats 3+5 = 8


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)    #OutPut is 500 and then 300 and after that 500 and after 500


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)    #OutPut 500 then 300 then 500 and after 300 and then 500


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)    #OutPut 500 then 300 then 300 and 500 and after 300 and then 500


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()    #OutPut output 1, 3 ,2


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)     #OutPut 1, 3, 5 and 10 