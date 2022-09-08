"""
Parameter
https://docs.python.org/3/glossary.html#term-parameter

*var-positional*: specifies that an arbitrary sequence of positional arguments can be provided
 (in addition to any positional arguments already accepted by other parameters).
  Such a parameter can be defined by prepending the parameter name with *, for example args in the following:
`def func(arg, *, kw_only1, kw_only2): ...`
"""


def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total


print(add(*range(10)))
print(add(1, 2, 3))
