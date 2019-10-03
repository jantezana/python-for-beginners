
# Reading an environmental variable
from dotenv import load_dotenv
import os

load_dotenv()

os_version = os.getenv('OS')
print(os_version)

if(os.name == 'posix'):
    print(os.system('uname -a')) 
else:
    print('Unknown OS')
password = os.getenv('PASSWORD')
print(password)