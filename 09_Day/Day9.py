# drive
print("level 1: ")
print("programa 1")
edad = int(input("enter your age:")   ) 
if edad > 17 :
    print(" you are old enough to drive")
else:
    print(" you need wait for the missing amount of years")


# compare values
print("programa 2:")
your_age= int(input("enter your age: "))
if edad > your_age:
    print(" tu edad es menor por: ",  edad - your_age, 'años' )
elif edad == your_age:
    print(" las edades son iguales")
else:
    print(" tu edad es mayor por: ",  your_age - edad, 'años' )

# get two numbers
print("programa 3:")
NO= input("enter a number:")
NT= input("enter a second number:")

if NO> NT:
    print( NO, " is greater than ", NT)
elif NO==NT:
    print(NO, "is equal to", NT)
else:
    print(NO, "is smaller than", NT)

#exercises level 2
print("exercises level 2:")
print("programa 1:")
grade= int(input("enter your score"))

if grade > 79 and grade < 101:
    print("la calificacion del alumnos es: A")
elif grade > 69 and grade <80:
    print("la calificacion del alumno es: B")
elif grade > 59 and grade <70:
    print("the student's grade is: C")
elif grade >49 and grade <60:
    print("the student's grade is: D")
else:
    print("the student's grade is: F")

#check
print("programa 2:")
seasons= str(input("enter a month:"))

if seasons in ['september', 'october', 'november']:
    print(" the season is: autumn")
elif seasons in ['december', 'january', 'february']:
    print(" the season is: winter")
elif seasons in ['march', 'april', 'may']:
    print("the season is : spring")
elif seasons in ['june', 'july', 'august']:
    print("the season is : summer")
else:
    print("there's no season")

#list
print("programa 3:")
fruit= input("enter a fruit:")
fruits= ['banana', 'orange', 'mango', 'lemon']

if fruit in fruits:
    print("that fruit is already exist in the list")
else: 
    print