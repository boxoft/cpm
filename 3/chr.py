"""
chr(i)
https://docs.python.org/3.5/library/functions.html?highlight=ord#chr

Return the string representing a character whose Unicode code point is the integer i.

The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in base 16).
 `ValueError` will be raised if `i` is outside that range.
"""

print(chr(97))  # a
print(chr(8364))  # €

print('\U0001f4af')  # 💯
print(chr(195028), hex(195028))  # 貫 0x2f9d4
print('\U0002f9d4')  # 貫
