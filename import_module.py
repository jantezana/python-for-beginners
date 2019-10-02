# import module as namespace
import helpers;
helpers.display('Sample Message', True)

# import all into current namespace
from helpers import *
display('Not a warning')

# import specific items into current namespace
from helpers import display
display('Not a warning')