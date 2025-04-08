# filter only negative
print("programa 1:")
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
lst= [i for i in numbers[0:5]]
print(lst)

# flatten the list
print("programa 2:")
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list=[item for sublist1 in list_of_lists for sublist2 in sublist1 for item in sublist2]
print(flatten_list)

# list comprehension
print("programa 3:")
list_of_tuples= [(n, 1, n, n**2, n**3, n**4, n**5) for n in range(11)]
print(list_of_tuples)

# flatten the list
print("programa 4:")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries= [[country.upper(), country[0:3].upper(), capital.upper()]for nested_list in countries for country, capital in nested_list]
print(flattened_countries)

# dictionary
print("programa 5:")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list_od_dicts= [{'country': country.upper(), 'city': city.upper()} for nested_list in countries for country, city in nested_list]

# change name
print("programa 6:")
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated=[f"{first}{last}" for nested_list in names for first, last in nested_list]
print(concatenated)

#slope
print("programa 7:")
slope= lambda x1, y1, x2, y2: (y2 - y1)/(x2- x1)
print(slope(1, 2, 3, 6))
print("Revisado")