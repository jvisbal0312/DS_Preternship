#!/usr/bin/env python3
#Source: https://booleanpy.readthedocs.io/en/latest/users_guide.html

import boolean
algebra = boolean.BooleanAlgebra()

x, y = algebra.symbols('x','y')
TRUE, FALSE, NOT, AND, OR, symbol = algebra.definition()

# TODO: Testprint logical expressions
print(x & y)
print(x | y)
print(x | ~y)

# TODO: Evaluate expressions
print(x & ~x)
print(x | ~x)
print(x | x)
print(x & x)
print(x & (x | y))
print((x&y) | (x & ~y))

# TODO: Simplify expressions
x, y, z = algebra.symbols('x', 'y', 'z')
print("Simplified expression of(((x|y)&z)|x&y):")
print((((x|y)&z)|x&y).simplify())

# TODO: Equality of Symbols
x1, x2 = algebra.symbols(10, 10)
print(x1 == x2)
x3, x4 = algebra.symbols("x", "x")
print(x3 == x4)

# TODO: function that simplify input expressions
def simplify(expr):
'''Returns the simplified expression of the input expression

>>> simplify('(((x|y)&z)|x&y)')
'Simplified expression of (((x|y)&z)|x&y): (x&y)|(z&(x|y))'
'''

# TODO: function that output the evaluations of expressions

# TODO: function that output the equality of symbols

# TODO: function that gets all the sub-terms

# TODO: function that gets all symbols (can be used in simplify/evaluation/equality)

