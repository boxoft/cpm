"""
ord(c)
https://docs.python.org/3.5/library/functions.html?highlight=ord#ord

Given a string representing one Unicode character,
 return an integer representing the Unicode code point of that character.
"""

print(ord("a"))  # 97
print(ord("€"))  # 8364
print(ord("貫"), hex(ord("貫")))  # 195028 0x2f9d4
