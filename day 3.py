# Programa 1

age = 19
print(type(age))
height = 1.72
print(type(height))
numeroComplejo = 9j
print(type(numeroComplejo))

# Area of the triangle

Muiltiplica= .5
base = float(input("enter the base of the triangle: "))
height= float(input("enter the height of the triangle: "))
area = Muiltiplica*base*height
print("the area is:  "  , area)

# perimeter of the triangle

sideA = int(input("enter the sideA: "))
sideB = int(input("enter the sideB: "))
sideC = int(input("enter the sideC: "))
per = int(sideA + sideB + sideC)
print("the perimeter of the triangle is: ", per)

# area y perimetro de un rectangulo

long = float(input("enter the lenght of the rectangle: "))
Anch = float(input("enter the width of the rectangle: "))
area = long * Anch
print("the area of the rectangle is :  " ,  area)
perimeter = 2 * area
print ("the perimeter of the rectangle is:  ", perimeter)

# radio de un circulo
radius= float(input("enter the radius: "))
pi=3.1416
area= pi * radius**2
print("the area of the circle is: " , area)
circumference= 2*pi*radius
print("the circumeference of the circle is: " , circumference)

# Calcular variables
m = 2
b= -2
x_intercept= -b/m
print("pendiente (m): ",  m)
print("interseccion en y (b)",   b)
print("interseccion en x (m)",   m)

# distancia entre punto a y b
import math

x_1= 2
x_2= 2
y_1= 6
y_2= 10
pendiente = (y_2)-(y_1)/(x_2)-(x_1)
euclides = math.sqrt (x_2 - x_1)**2 + (y_2)-(y_1)**2
print("la pendiente es de: ", pendiente)
print("la euclides es: ",  euclides)

#comparar las pendientes

if m == pendiente:
    print(" las pendientes son iguales")
elif m>pendiente:
    print("la primera pendiente es mayor")

else: ("la segunda pendiente es mayor")   

# calcular el valor de y

def calculate_y(x):
    y = x**2 + 6*x + 9
    return y

# Probar diferentes valores de x
for x in range(-10, 5):
    result = calculate_y(x)
    print(f"x: {x}, y: {result}")


# find lenght of python and dragon

lenght_python = len('python')
lenght_dragon = len('dragon')
print(lenght_python != lenght_dragon)

# check if on is in dragon and python
result = 'on' in 'python ' and 'on' in 'dragon'
print(result)

# sentence

sentence = "i hope thos course is not full or jargon."
print('jargon' in sentence)

# lenght float to str
result= 'on' not in 'python' and 'on'  not in 'dragon'
print(result)

length_python = len('python')
length_float= float(length_python)
length_str= str(length_float)
print(length_str)

# Numbers pair of inpair
number = 6
if number % 2 == 0:
    print(" your number is pair")
else:
    print(" your number is inpair")



# check if  the division is 2.7
div= 7//3
valorconvertido = int(2.7)
if div==valorconvertido:
   print("son iguales")
else:
   print(" no son iguales")

   #verify if the 10 type it's the same as the other 10 type
if (type('10') == type(10)):
 print('true')
else:
        print('false')

        #verify if int('9.8) is the same to 10
if (int(float('9.8'))== 10):
 print('true')
else:
    print('false')

# calculate the payment

hours= input("enter hours")
rph= input("enter rate")
weeklyearning= int(hours)*int(rph)
print(" your payment is: $ " , weeklyearning)


# write a table
print( 1, 1, 1, 1, 1)
print( 2, 1, 2, 4, 8)
print( 3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)