# day 8

#empty dictionary
print("programa 1:")
dog= {}

# add name and others things
print("programa 2:")
dog={
    'name': 'xavi',
    'color': 'black',
    'breed': 'mastin napolitano',
    'legs': '4',
    'age': '3 years'

}
print(dog)

#create a student dictionary
print("programa 3:")
student_Dictionary={
    'first_name':'kaili ',
    'last_name': 'barba',
    'gender': 'male',
    'age': '19',
    'marital status': 'single',
    'skills': ['python', 'voleyball', 'intelligent'],
    'country':'mexico',
    'city':'san juan de los lagos jalisco',
    'address':{'street': 'pedro moreno 7B',
               'zipcode': '47010'
    }
    }

# get length
print("programa 4:")
print(len(student_Dictionary))

# get the value
print("programa 5:")
print(student_Dictionary['skills'])
print(type(student_Dictionary['skills']))

# modify the skills
print("programa 6:")
student_Dictionary['skills'].append('fast')
print(student_Dictionary)

# get key as a list
print("programa 7:")
keys=student_Dictionary.keys()
print(keys)

# get values as a list
print("programa 8:")
values= student_Dictionary.values()
print(student_Dictionary)

# change dictionary
print("programa 9:")
tuples= student_Dictionary.items()
print(tuples)

#delete one of the items
print("programa 10:")
del student_Dictionary['first_name']
print(student_Dictionary)

# delete a dictionary
print("programa 11:")
del student_Dictionary

print("revisado")