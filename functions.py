from datetime import datetime

def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

first_name = 'Susan'
print_time('first name assigned')

for x in range(0,10):
    print(x)
print_time('loop completed')


def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = 'juan'
#first_name_initial = first_name[0:1]
first_name_initial = get_initial(first_name)
last_name = 'antezana'
#last_name_initial = get_initial(last_name, False)
last_name_initial = get_initial(force_uppercase=False, name=last_name)
#last_name_initial = last_name[0:1]

print('Your initials are: {}{}'.format(first_name_initial, last_name_initial))