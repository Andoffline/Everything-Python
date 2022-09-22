# Task to find area and perimeter
#Function perimeter() to find perimeter of rectangle
def perimeter(a,b):
    return a*2+b*2
 
#Function area() to find area of rectangle
def area(a,b):
    return a*b

a = int(input("Enter first side of rectangle: "))
b = int(input("Enter second side of rectangle: "))
print('Perimeter =',perimeter(a,b))
print('Area =',area(a,b))