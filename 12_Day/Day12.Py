# function that generates digit
print("programa 1:")
import random
import string
def randomUserId ():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))
print('usuario generado', randomUserId())

# user by user
print("programa 2:")
def userIdGenByUser():
    numCaracteres= int(input("enter a number of characteres"))
    numIds= int(input("enter numbers of ids:"))
    ids = [
        ''.join(random.choices(string.ascii_letters + string.digits, k=numCaracteres))
        for _ in range(numIds)
    ]
    return ids
print(userIdGenByUser())

# gen rgb
print("programa 3:")
def rgbColorGen():
    green= random.randint(0,255)
    blue= random.randint(0,255)
    red= random.randint(0,255)
    return (green, blue, red)
print(rgbColorGen())

# color's list
print("programa 1 level 2:")
import random
def ListadeColoresHexa(n):
    return['#' + ''.join(random.choices('0123456789abcdef', k=6)) for _ in range (n)]
hexacolor= ListadeColoresHexa(8)
print("colores generados:", hexacolor)

#rgb's list
print("programa 2 level 2:")
def listOfRgbColors(n):
    return[(random.randint(0,255), random.randint(0,255), random.randint(0,255)) for _ in range (n)]

#generar colores
print("programa 3 level 2: ")
def generarColores(color_type, n):
    return ['#' + ''.join(random.choices('0123456789abcdef', k=6)) for _ in range (n)] if color_type== 'hexa' else [(random.randint(0,255), random.randint(0,255), random.randint(0,255)) for _ in range(n)] if color_type== 'rgb' else "error: usa 'hexa' o 'rgb' "
print(generarColores('hexa', 5))
print(generarColores('rgb', 5))

# shuffle list
print("programa 1 level 3:")
def shuffleList(lst):
    random.shuffle(lst)
    return lst
myList= [5,6,7,8,9,10]
print("lista revuelta:",  shuffleList(myList))

# unique numbers
print("programa 2 level 3:")
import random
def uniquesNumbers():
    return random.sample(range(10), 7)
randomNumbers= uniquesNumbers()
print("unique random numbers: ", randomNumbers)