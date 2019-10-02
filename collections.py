# List
print('###########LIST###########')
names = ['Juan', 'Carlos', 'Lucas']
print(names)
names.sort()
print(names)

presenters = names[0:2]
print(presenters)

# sorted_names = sorted(names)
# print(sorted_names)

last_names = []
last_names.append('Antezana')
last_names.append('Master')
# Get the number of items
print(len(last_names))
print(last_names)
# Insert before index
last_names.insert(0, 'Adrian')
print(last_names)
print(last_names[1])

# Array
from array import array
print('###########ARRAY###########')
scores = array('d')
scores.append(97)
scores.append(98)
# Only integers are allow 
#scores.append('Juan')
print(scores)
print(scores[1])

# Dictionaries
print('###########DICTIONARIES###########')
person = {'first': 'Juan', 'age': 32}
person['last'] = 'Antezana'
print(person)
print(person['first'])
