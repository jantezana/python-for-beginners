x = 42
y = 0

# Handling runtime error
try:
    print(x / y)
except ZeroDivisionError as zde:
    print('Not allowed to divide by zero')
else:
    print('Something else went wrong')
finally:
    print('This is our cleanup code')

# Runtime error
# print(x / y)