# empty list
print("programa 1:")
empty_list=[]
print(empty_list)

# list
print("programa 2:")
list=['banana', 'orange', 'watermelon', ' pineapple', 'alejandro']
print(list)

# length
print("programa 3:")
list=['banana', 'orange', 'watermelon', ' pineapple', 'alejandro']
print (len(list))

# find items
print("programa 4:")
list=['banana', 'orange', 'watermelon', ' pineapple', 'alejandro']
first_item= list[0]
print(first_item)
second_item=list[2]
print(second_item)
third_item=list[4]
print(third_item)

# list by my name
print("programa 5: ")
mixed_data_types= ['yazid', '19 ', '1.74', 'solitaire', 'versalles 1ra seccion']

# list of companies
print("programa 6:")
it_companies=['facebook', ' google', 'microsoft', 'apple', 'IBM', 'oracle', 'amazon']

#print the list
print("programa 7:")
print(it_companies)
print(mixed_data_types)


#print number of companies
print("programa 8:")
print(len(it_companies))

# print items
print("programa 9:")
first_item= it_companies[0]
print(first_item)
second_item=it_companies[3]
print(second_item)
third_item=it_companies[6]
print(third_item)

# modifying list
print("programa 10:")
it_companiesMod=['facebook', ' google', 'microsoft', 'apple', 'IBM', 'oracle', 'amazon']
it_companiesMod [0]= 'instagram'
print(it_companiesMod)

# add IT
print("programa 11:")
it_companies1=['facebook', ' google', 'microsoft', 'apple', 'IBM', 'oracle', 'amazon']
it_companies1.append('X')
print(it_companies1)

# add company in the middle
print("programa 12:")
it_companies1.insert(4, 'whatsapp')
print(it_companies1)

# min company to upper
print("programa 13:")
it_companies= ['facebook', ' google', 'microsoft', 'apple', 'IBM', 'oracle', 'amazon']
may= it_companies[3].upper()
print(may)

# hash
print("programa 14:")
it_companies=['facebook',' google', 'microsoft', 'apple', 'IBM', 'oracle', 'amazon']
print('#'.join(it_companies))

# check if one company is in the string
print("programa 15:")
it_companies=['facebook','google', 'microsoft', 'apple', 'IBM', 'oracle', 'amazon']
print('google' in it_companies)

#sort
print("programa 16:")
it_companies.sort()
print(it_companies)

# reverse the list
print("programa 17:")
it_companies.reverse()
print(it_companies)

# slice first
print("programa 18:")
cut=it_companies1[3:9]
print(cut)

#slice the latest
print("programa 19:")
cut= it_companies1[0:6]
print(cut)

#slice the middle company
print("programa 20:")
cutM= it_companies1[0:3] + it_companies1[6:9]
print(cutM)

# reomve the first company
print("programa 21:")
del it_companies1[0]
print(it_companies1)

#remove the middle
print("programa 22:")
del it_companies1[4]
print(it_companies1)
 
# remove the last
print("programa 23:")
del it_companies1[6]
print(it_companies1)

# remove all
print("programa 24:")
del it_companies1[0:5]

#destroy list
print("programa 25:")
it_companies1.clear()
print(it_companies1)

# join list
print("programa 26:")
front_end= ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end= ['Node','Express', 'MongoDB']

# assign
print("programa 27:")
full_stack= front_end + back_end
print(full_stack)

#add python and sql
add= ['Python', 'SQL']
final_stack= front_end + add + back_end
print(final_stack)

