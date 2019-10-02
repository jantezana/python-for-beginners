# to get the current data and time we need to use the datetime library.
from datetime import datetime, timedelta

current_date = datetime.now()
print(current_date) # 2019-09-30 19:08:15.824871
print('Today is: ' + str(current_date))
#print('Today is: {}'.format(current_date)))

# Days
one_day = timedelta(days=1)
yesterday = current_date - one_day
print(f'Yesterday: {yesterday}')
# Weeks
one_week = timedelta(weeks=1)
last_week = current_date - one_week;
print(f'Last week: {last_week}')

print(f'Day: {current_date.day}')
print(f'Month: {current_date.month}')
print(f'Year: {current_date.year}')

# Format string to date
birthday = input('When is your birthday (dd/mm/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: {}'.format(birthday_date))
print('Birthday Year: {}'.format(birthday_date.year))