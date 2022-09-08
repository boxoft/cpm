"""
Parameter
https://docs.python.org/3/glossary.html#term-parameter

var-keyword: specifies that arbitrarily many keyword arguments can be provided
 (in addition to any keyword arguments already accepted by other parameters).
  Such a parameter can be defined by prepending the parameter name with **, for example kwargs in the example above.


"""


def hi(**user):
    print("Hi,", user)


hi(firstName="Tom", lastName="Cat")
