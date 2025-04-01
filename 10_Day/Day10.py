# loop 0 to 10
print("programa 1:")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    print ('bucle : ', numero)
#while
cont = 0
while cont <= 10:
    print('bucle while: ', cont)
    cont = cont + 1

#loop 10 to 0
print ("programa 2:")
numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for number in numbers:
    print ('bucle : ', number)
#while
cont = 10
while cont > -1:
    print('bucle while: ', cont)
    cont = cont -1

# pyramid
print("programa 3:")
e= '#'
for i in range (1, 8):
    print(e * i)

# loop #
print("programa 4:")
e ='#'
for i in range (8):
    print(e * 8)

#print numbers
print("programa 5:")
for i in range (11):
    print(f"{i} x {i}= {i * i}")

#lst
print("programa 6:")
programas= ['Python', 'Numpy','Pandas','Django', 'Flask']
for programa in programas:
    print(programas)

#even numbers
print("programa 7:")
for i in range (101):
    if i % 2==0:
        print(i)

#odd numbers
print("programa 8:")
for i in range (101):
    if i % 2!=0:
        print(i)

#exercises level 2
print("exercises level 2:")
print("programa 1: level 2")
sumaTotal=0
for i in range (101):
    sumaTotal += i
    print("la suma total es:" , sumaTotal)

# even numbers
print("programa 2 level 2:")
sumaPares=0
sumaImpares= 0
for i in range (101):
    if i % 2==0:
        sumaPares += i
else: 
    sumaImpares += i
    print(" la suma de pares es:", sumaPares)
    print(" la suma de Impares es:", sumaImpares)