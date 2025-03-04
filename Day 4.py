# concatenate thirty days of python
print("programa 1:")
str= 'thirty'  + " "'days' " "+ 'of' " " + 'python'
print(str )

#concatenate coding for all
print("programa 2:")
str= 'coding' " "+ 'for' " "+ 'all' 
print(str)

# 3 and 4 declare variable and print company
print("programa 3:")
company= "coding for all"
print(company)

# length of company
print("programa 4:")
length_company=len('company')
print(length_company)

#change characters to upper
print("programa 5:")
min= ("thirty days of python")
may= min.upper()
print("Tu enunciado en mayusculas es:", may)

#change characters to lower
print("programa 6:")
may= ("THIRTY DAYS OF PYTHON")
min= may.lower()
print("Tu enunciado en minusculas es:", min)

# use methods
print("programa 7:")
str=("coding for all")
str_capitalize= str.capitalize()
str_title= str.title()
str_swapcase= str.swapcase()
print("the function capitalize is:", str_capitalize)
print("the function title is:", str_title)
print("the function swapcase is:", str_swapcase)

# cut word
print("programa 9:")
str= ("coding for all")
cut= str[6:14]
print("now your sentence is: ", cut)

# check if coding
print("programa 10:")
Stc= ("coding for all")
print('coding' in Stc)

# replace the word
print("programa 11:")
str= ("coding for all")
remplazar = (str.replace('coding', 'python'))
print("your sentence is:"  , remplazar)

#change python for everyone
print("programa 12:")
str= ("python for everyone")
remp= (str.replace('everyone',  'all'))
print(remp)

#split the string
print("programa 13:")
str=("coding for all")
space= (str.split())
print(space)

#split face, ig, etc
print("programa 14:")
str= ("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon")
space= (str.split())
print(space)

# index
print("programa 15:")
str= ("coding for all")
find= str[0]
print(find)

# last index
print("programa 16:")
str=("coding for all")
find= str[12]
print(find)

# index 10
print("programa 17:")
str=("coding for all")
find= str[10]
print(find)

#create an acronym
print("programa 18:")
acronym= ("python for all")
abbreviation= acronym[0][0]+ acronym[7][0]+ acronym[11][0]
print(abbreviation)

# create an acronym2
print("programa 19:")
acronym= ("coding for all")
abbreviation= acronym[0][0]+ acronym[7][0]+ acronym[11][0]
print(abbreviation)

# use index
print("programa 20:")
str=("coding for all")
find= str.index('c')
print('position:', find)

# use index 2
print("programa 21:")
str=("coding for all")
find= str.index('f')
print('position:', find)

# use index 3
print("programa 22:")
str=("coding for all people")
find= str.index('l')
print('position:', find)

# use index in sentence
print("programa 23:")
str= ("You cannot end a sentence with because because because is a conjunction")
find= str.index("because")
print('position:', find)

# use rindex
print("programa 24:")
str= ("You cannot end a sentence with because because because is a conjunction")
find= str.rindex('because')
print('position:', find)

# cut sentence
print("programa 25:")
str= ("You cannot end a sentence with because because because is a conjunction")
cut= str[0:30]+ str[54:71]
print("the sentence is:", cut)

# find position
print("programa 26:")
str= ("You cannot end a sentence with because because because is a conjunction")
find= str.index('because')
print('position:', find)

# cut sentence
print("programa 27:")
str= ("You cannot end a sentence with because because because is a conjunction")
cut= str[0:30]+ str[54:71]
print("the sentence is:", cut)

# does starts with coding
print("programa 28:")
str=("coding for all")
strstar= str.startswith('coding')
print(strstar)

# does ends with coding
print("programa 29:")
str=("coding for all")
strstar= str.endswith('coding')
print(strstar)

# remove left and right side
print("programa 30:")
