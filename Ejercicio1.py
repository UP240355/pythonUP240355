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
pendiente = ((y_2)-(y_1)/(x_2)-(x_1))
euclides= math.sqrt ((x_2 - x_1)**2 + (y_2)-(y_1)**2)
print("la pendiente es de: ", pendiente)
print("la euclides es: ",  euclides)

#comparar las pendientes

if m == pendiente:
    print(" las pendientes son iguales")
elif m>pendiente:
    print("la primera pendiente es mayor")

else: ("la segunda pendiente es mayor")   

# calcular el valor de y



