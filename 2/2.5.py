first = "Tom"
last = "Cat"
full = first + " " + last
print(full)  # Tom Cat

"""
2.4.3. Formatted string literals
https://docs.python.org/3.7/reference/lexical_analysis.html#f-strings
New in version 3.6.
A formatted string literal or f-string is a string literal that is prefixed with 'f' or 'F'. 
"""
full = f"{first} {last}"
print(full)  # Tom Cat
