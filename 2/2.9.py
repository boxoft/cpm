x = input("x: ")
print(type(x))  # <class 'str'>

y = int(x) + 1
print(f"x: {x}, y: {y}")  # e.g. x: 123, y: 124

# Falsy
if not ("" or 0 or None or False):
    print("Falsy")
