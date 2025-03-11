
# create an empty tuple
print("programa 1:")
empty_tuple=()

# create a tuple
print("programa 2:")
brother=('kenneth')
sister=('keisha')
print(brother)
print(sister)

# join the tuples
print("programa 3:")
siblings= brother , sister
print(siblings)

# question
print("programa 4:")
siblingsLen= len(siblings)
print(siblingsLen)

#modify
print("programa 5:")
fathers=('geovanni', 'gisela')
family_members= fathers + siblings
print(family_members)

#level 2
print("excerises level 2:")
unpack= family_members[0:2]
unpack2= family_members[2:4]
print(unpack)
print(unpack2)

#create fruits
print("programa 2 level 2:")
fruits= ('apple', 'watermelon', 'pineapple', 'peach', 'orange')
vegetables= ('tomato', 'carrot', 'pumpkin')
animalProducts=('meat', 'fish', 'dairy')

food_stuff_tp= fruits +  vegetables + animalProducts
print(food_stuff_tp)

#change the name list
print("programa 3:")
food_stuff_lt= ('apple', 'watermelon', 'pineapple', 'peach', 'orange', 'tomato', 'carrot', 'pumpkin' , 'meat', 'fish', 'dairy')

# slice items
print("programa 4:")
slice= food_stuff_lt[0:4] + food_stuff_lt[7:10]
print(slice)

# slice first three
print("programa 5:")
slice= food_stuff_lt[3:8]
print(slice)

#delete
print("porgrama 6:")
del food_stuff_lt

