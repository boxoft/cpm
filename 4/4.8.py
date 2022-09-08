first = "Tom"
last = "Cat"


def change(last_name):
    global first, last
    first = "Jerry"
    last = last_name


print(f"{first} {last}")  # Tom Cat
change("Mouse")
print(f"{first} {last}")  # Jerry Mouse
