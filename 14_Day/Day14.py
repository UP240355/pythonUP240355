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