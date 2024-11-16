
# 8. Function with Keywords
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="Waheed", degree="BSCS")
print_kwargs(name="Waheed")
print_kwargs(name="Waheed", degree="BSCS", age = 22)