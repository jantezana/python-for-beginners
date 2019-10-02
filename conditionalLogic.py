price = 2.5

if price >= 1.00:
    tax = .07
else:
    tax = 0
print(tax)

province = 'Alberta'
# if province == 'Alberta':
#     tax = 0.05
# elif province == 'Nunavut':
#     tax = 0.06
# elif province == 'Ontario':
#     tax = 0.13

# if province == 'Alberta' \
#     or province == 'Nunavut':
#     tax = 0.05
# elif province == 'Ontario':
#     tax = 0.13
# else:
#     tax = 0.15

if province in ('Alberta', \
                'Nunavut', 'Yukon'):
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15


print(tax)

# compare strings is case sensitive
country = 'CANADA'
if country.lower() == 'canada':
    print('Oh look a Canadian')
else:
    print('You are not from Canada')


gpa = .9
lowest_grade = .8
if gpa >= .85 and lowest_grade >= .70:
    print('You made the honour roll')