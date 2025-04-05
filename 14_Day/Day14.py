# differences
print("programa 1:")
# map: aplica una funcion a cada elemento de un iterable como una lista.
# filter: aplica una funcion a cada elemento  de un iterable y devuleve un nuevo iterable.
#reduce: aplica una funcion acumulativa a los elemntos de un iterable.

print("programa 2:")
#higher order functions: una funcion que recibe otra funcion como argumento o devuelve una funcion como resultado.
# closures: una funcion que recuerda las variables de su entorno.
#decorator: una funcion que toma otra funcion como entyrada y devuelve una nueva funcion con funcionalidad añadida.

print("programa 3:")
def square(X):
    return X**2
nums=[1, 2, 3, 4]
result= list(map(square,nums))
print(result)

# use for
print("programa 4:")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for country in countries:
    print(country)

# use for in names
print("programa 5:")
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(name)

#use for in numbers
print("programa 6:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)

# level 2
print("level 2:")
print("programa 1 level 2:")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
upper= list(map(str.upper, countries))
print(upper)

#square numbers
print("programa 2 level 2:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def square(X):
    return X**2
squared_numbers= map(square, numbers)
print(list(squared_numbers))

#uppercase names
print("programa 3 level 2:")
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
upper_names= list(map(str.upper, names))
print(upper_names)

# use filter
print("programa 4 level 2:")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
filtered_countries= list(filter(lambda country: 'land' not in country.lower(), countries))
print(filtered_countries)

# only 6 characters
print("programa 5 level 2:")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
sixchar_countries= filter( lambda country: len(country) == 6, countries)
print(sixchar_countries)

#only 6 or above char
print("programa 6 level 2:")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
sixchar_countries2= filter( lambda country: len(country) < 6, countries)
print(sixchar_countries2)

# only E word
print("programa 7 level 2:")
filtered_E= filter(lambda country: not country.startswith('E'), sixchar_countries)
print(filtered_E)

# iterate
print("programa 8 level 2:")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
iterate= list(
    map(
        lambda country: country.upper(), filter (lambda country: len(country) <6 and not country.startswith('E'), countries)
    )
)
print(iterate)

# declare function
print("programa 9 level 2:")
def get_str_list(lst):
    return[item for item in lst if isinstance(item, str)]
mix_list= ['hello', 55, True, 'coding', 3.14]
string_items = get_str_list(mix_list)
print(string_items)

#reduce
from functools import reduce
numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_numbers= reduce(lambda x, y: x + y, numbers)
print(sum_numbers)

#reduce2
print("programa 11 level 2:")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
sentence=reduce(lambda x, y: f"{x}, {y}" if y != countries[-1] else f"{x}, {y}", countries)
print(sentence)

#countries
print("programa 12 level 2")
def categorize_countries(countries3):
    return[country for cuntry in countries if 'a' in country.lower()]
import countries3 as p
countries4= p.countries3

categorize_countries= categorize_countries(countries4)
print(categorize_countries)

# create function
print("programa 13 level 2:")
keys = []
keys = [i[0] for i in countries4 if i[0] not in keys]
def contarcountry(contador):
    return sum([True for i in countries4 if i[0].startswith(contador)])
values = [contarcountry(l) for l in keys]
print(dict(zip(keys, values)))

#Programa 14, nivel 2
print ("programa 14, nivel 2:")
def getFirstTenCountries():
     return countries4[:10]
print (getFirstTenCountries())

#Programa 15, nivel 2
print ("programa 15, nivel 2:")
def getLastTenCountries():
     return countries4[-10:]
print (getLastTenCountries())

#level 3