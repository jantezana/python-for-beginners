first_name = 'Juan'
last_name = 'Antezana'

print(first_name + last_name)

print('Hello, ' + first_name + ' ' + last_name)

sentence = 'The dog is named Milo!!';
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))

output = 'Hello, ' + first_name + ' ' + last_name;
print(output)

output = 'Hello, {} {}'.format(first_name, last_name)
print(output)

output = 'Hello, {1} {0}'.format(first_name, last_name)
print(output)

output = f'Hello, {first_name.upper()} {last_name.upper()}'
print(output)

#first_name = input('What is your first name? ')
#last_name = input('What is your last name? ')
#print('Hello ' + first_name.capitalize() + ' ' + last_name.capitalize())