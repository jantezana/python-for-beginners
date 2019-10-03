# Imports
import json

# create a dictionary object
person_dict = {'first': 'Juan', 'last': 'Antezana'}
person_dict['city'] = 'Cochabamba'

programing_languages = ['Java', 'C#', 'C++', 'C', 'Python']
person_dict['languages'] = programing_languages
phone_numbers = {'home': 4265696, 'work': [70358629, 72720217]}
#phone_numbers['work'] = [70358629, 72720217]
person_dict['phones'] = phone_numbers

# languages
print('#####Languages#####')
for language in person_dict['languages']:
    print(language)
print('###################')

print()

# phones
print('#####Phones#####')
for phone in person_dict['phones']['work']:
    print(phone)
print('################')

print(person_dict['languages'])
print(person_dict['phones']['work'])
print(person_dict['phones']['work'][1])

# convert dictionary to JSON object
person_json = json.dumps(person_dict)
print(person_json)
