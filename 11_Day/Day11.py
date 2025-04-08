
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
degrees= int(input("ingrese los grados celsius:"))
print(convertirCelsiusAfarenheit(degrees))

# season
print("programa 4:")
def checkSeason(mes):
    spring = ['marzo', 'abril', 'mayo']
    summer = ['junio', 'julio', 'agosto']
    fall = ['septiembre', 'octubre', 'noviembre']
    winter = ['diciembre', 'enero', 'febrero']
    
    if mes in spring:
        return "Primavera"
    elif mes in summer:
        return "Verano"
    elif mes in fall:
        return "Otoño"
    elif mes in winter:
        return "Invierno"


month = input("Ingrese el mes: ")
print(checkSeason(month))

# calculate slope
print("programa 6:")
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)
x1= float(input("enter x1:"))
y1= float(input("enter y1:"))
x2= float(input("enter x2:"))
y2= float(input("enter y2:"))
print(calculate_slope(x1, y1, x2, y2))

#solve a quadratic
print("programa 7:")
def solve_quadratic(a, b, c):
    x1= (-b + ((b ** 2)-4 * a *c) ** 0.5)/ 2 * a
    x2= (-b - ((b ** 2)-4 * a *c) ** 0.5)/ 2 * a
a= float(input("enter a:"))
b= float(input("enter b:"))
c= float(input("enter c:"))
print(solve_quadratic(a, b, c))

# minlist
print("programa 8:")
def print_list(myList):
    for elemento in myList:
        print(elemento)

list= [100, 200, 300, 400, 500, 600]
print(list)

# reverse list
print("programa 9:")
def reverse_list(myList):
    myList.reverse()
    return myList
list= [100, 200, 300, 400, 500, 600]
print(reverse_list(list))

# upper
print("programa 10:")
def capitalize_list_items(myList):
    return [x.upper() for x in myList]
list= ['hello', 'world', 'python']
print(capitalize_list_items(list))

# add item
print("programa 11:")
def add_item(myList, item):
    myList.append(item)
    return myList
myList= ['meat', 'cheese']

#remove item
print("programa 12:")
def remove_item(myList, item):
 myList.remove(item)
 return myList
list= ['meat', 'cheese']
item= 'cheese'
print(remove_item(list, item))

# sum numbers
print("programa 13:")
def sum_of_numbers(n):
    if n< 1:
        return
    return sum(range(1, n + 1))
result= sum_of_numbers(10)
print("la suma final es:" , result)

# sum odd numbers
print("programa 14:")
def sum_of_odds(n):
    if n < 1:
        return
    return sum(range(1, n +1, 2))
resultado = sum_of_odds(10)
print(" la suma de numeros impares es:", resultado)

# sum even numbers
print("programa 15:")
def sum_of_evens(n):
    if n < 1:
        return
    return sum(range(2, n +1, 2))
resultado = sum_of_evens(10)
print(" la suma de numeros impares es:", resultado)

#exercises level 2
print("exercises level 2:")
print("programa 1 level 2:")
def evens_and_odds():
    numero= float(input("enter a number:"))
    if numero % 2==0:
        return "the number is even"
    else:
        return "the number is odd"
print(evens_and_odds())

# negative number
print("programa 2 level 2:")
def factorial(number):
    if number < 0:
        return "no esta definido para numeros negativos"
    elif number == 0 or number ==1:
        return 1
    else:
        result= 1
        for i in range (2, number + 1):
            result += i
            return result
try:
    fac = int(input("enter a entire number:"))
    print(f" el facotrial de {fac} es: {factorial(fac)}")
except ValueError:
    print("please, enter a entire number valid ")


# empty
print("programa 3 level 2:")
def is_empty(valido):
    if not valido:
        return True
    else:
        return False
print(is_empty([]))
print(is_empty([1, 2]))

#calculate
print("programa 4 level 2:")
def calculate_mean(lista):
    return sum(lista)/len(lista)
print(calculate_mean(lista = [1, 2, 3, 4, 5]))

def calcular_mediana(numeros):
    numeros_ordenados = sorted(numeros)
    n = len (numeros_ordenados)
    if n % 2==1:
        mediana= numeros_ordenados[n //2]
    else:
        mediana=(numeros_ordenados[n // 2 -1 ] + numeros_ordenados[n // 2]) /2
        return mediana
    numeros= [1,2,3,4,5]
    resultado= calcular_mediana(numeros)
    print(f"la mediana es:{resultado}")

def calcular_mode(numeros):
    from collections import Counter
    frecuencias= Counter(numeros)
    max_frecuencia = max (frecuencias.values())
    modos = [num for num, freq in frecuencias.items() if freq == max_frecuencia]
    return modos
numeros= [4, 5, 6, 4, 7, 4]
modos= calcular_mode(numeros)
print(f"el modo es: {modos}")

def calcular_rango(numeros):
    return max(numeros) - min(numeros)
numeros= [4, 5, 6, 4, 7, 4]
rango= calcular_rango(numeros)
print(f" el rango es {rango}")

#ejercicios level 3
print("level 3:")
print("programa 1 level 3:")

def is_primo(numero):
    if numero <=1:
        return False 
    for i in range (2, int(numero **0.5)+1):
        if numero % 1 ==0:
            return False
        return True
    numero= int(input("enter a number:"))
    if is_primo(numero):
        print(f" es un numero primo:" , numero)
    else:
        print(f"no es un numero primo:", numero)

# unique numbers
print("programa 2 level 3:")
def son_unicos(lista):
    unicos= []
    for elemento in lista:
        for elemento in not unicos:
            unicos.append(elemento)
            return unicos
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(son_unicos(lista))

# same data
print("programa 3 level 3:")
def same_data(lista):
    if not lista:
        return True
    return all (isinstance(item, type(lista[0]))for item in lista)
print(same_data([1,2,3,4,5,6]))

# variable python
print("programa 4 level 3:")
def python_variable(variable):
    if variable.isidentifier():
        return True
    else:
        return False
print(python_variable(variable = 'variable1'))


# countries
print("programa 5 level 3:")
import countriesData as cDatos
datos= cDatos.countries2
country_len= []
def mas_hab():
    for pais in datos:
        for lenguaje in pais ['languages']:
            country_len.append(lenguaje)
            setLen= set(country_len)
            dicLen= {

            }
            for lenguaje in setLen:
                dicLen[lenguaje]= 0
                for idioma in dicLen:
                    for pais in datos:
                        if idioma in pais ['languajes']:
                            dicLen [idioma]= pais['population'] + dicLen[idioma]
            sortVallenpopu= sorted(dicLen.values(),reverse=True)
            sortKeyLenPopu= sorted(dicLen, key= dicLen.get, reverse=True)
            return sortKeyLenPopu [:10], sortVallenpopu [:10]
        print(mas_hab())
        def paisesM ():
            dicPoblacion= {

            }
            for pais in datos:
                dicPoblacion[pais['name']] = pais ['population']
                sortValPopu = sorted (dicPoblacion.values(), reverse = True)
                sortKeyPopu= sorted (dicPoblacion, key= dicPoblacion.get, reverse= True)
                return sortKeyPopu[:10], sortValPopu[:10]
            print(paisesM())

print("Revisado")