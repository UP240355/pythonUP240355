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
it_companies=['facebook', ' google', 'microsoft', 'apple', 'IBM', 'oracle', 'amazon']
it_companies.append('X')
print(it_companies)

# add company in the middle
print("programa 12:")
it_companies=['facebook', ' google', 'microsoft', 'apple', 'IBM', 'oracle', 'amazon']
it_companies.insert(4, 'whatsapp')
print(it_companies)

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
google= 'google' is  it_companies 
print(google)