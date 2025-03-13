#exercises level 1
print("exercises level 1:")

#find the length
print("programa 1:")
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

#add twitter
print("programa 2:")
it_companies.add('twitter')
print(it_companies)

# add companies
print("programa 3:")
it_companies.update(['samsung', 'lenovo', 'instagram'])
print(it_companies)

#remove
print("programa 4:")
it_companies.remove('instagram')
print(it_companies)

# difference 
print("programa 5:")
# remove get out an element from a list
# discard eliminate an element only if it is present 


#level 2
print("exercises level 2:")

# join
print("programa 1:")
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
c= A.union(B)
print(c)

#find intersection
print("programa 2:")
intersection= A.intersection(B)
print(intersection)

#subset
print("programa 3:")
subset= A.issubset(B)
print(subset)

# disjoint
print("programa 4:")
disjoint= A.isdisjoint(B)
print(disjoint)

# join
print("programa 5:")
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.union(B))
print(B.union(A))

#symmetric
print("programa 6:")
difference= A.symmetric_difference(B)
print(difference)

#del
print("programa 7:")
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
del A, B

#exercises level 3

print("exercises level 3:")

#list and set
print("programa 1:")
ages = ['22', '19', '24', '25', '26', '24', '25', '24']
st= set(ages)
if len(ages) > len(st):
    print ("La lista es mayor ")
else:
    print ("El set es mayor")

#explain concepts
print("programa 2:")
 # string: es una cadena de characters.
 # list: es conjunto de items:
 # tuple: es similar a una lista pero con la diferencia de que es inmutable, es decir no puedes modificar sus elementos.
 # set: es una lista que no esta ordenada de elementos unicos.

# sentence 
print("programa 3:")
sentence= ['I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and', 'teach', 'people.']
sentence_set = set(sentence)
print (len(sentence_set))
print (sentence_set)