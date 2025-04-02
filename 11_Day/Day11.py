
# functions
print("programa 1:")
def add_two_numbers():
    num_one= int(input("enter a number:"))
    num_two= int(input("enter a second number:"))
    Sum= num_one + num_two
    print("suma total:", Sum)
add_two_numbers()

#radius
print("programa 2:")
def area_of_circle(R):
    pi= 3.14
    area= pi * Rad**2
    return area
Rad = int(input("enter a radius:"))
print(area_of_circle(Rad))

# numbers
print("programa 3:")
def add_all_nums(*nums):
    total= 0
    for num in nums:
        total += num
        return total
    
# celsius a farenheit
print("programa 4:")
def convertirCelsiusAfarenheit(celsius):
    farenheit= (celsius *9/5)+ 32
    return farenheit
degrees= float(input("ingrese los grados celsius:"))
print(convertirCelsiusAfarenheit(degrees))

# season
print("programa 4:")
def checkSeason(month):
 primavera = ['marzo', 'abril', 'mayo']
verano = ['junio', 'julio', 'agosto']
    otoño = ['septiembre', 'octubre', 'noviembre']
    invierno = ['diciembre', 'enero', 'febrero']
    
    if mes in primavera:
        return "Primavera"
    elif mes in verano:
        return "Verano"
    elif mes in otoño:
        return "Otoño"
    elif mes in invierno:
        return "Invierno"
    else:
        return "no esta mi apa"

month = input("Ingrese el mes: ")
print(checkSeason(month))