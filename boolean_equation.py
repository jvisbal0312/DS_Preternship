#!/usr/bin/env python3
#Source: https://booleanpy.readthedocs.io/en/latest/users_guide.html

import boolean
algebra = boolean.BooleanAlgebra()

x, y = algebra.symbols('x','y','z')
TRUE, FALSE, NOT, AND, OR, symbol = algebra.definition()

# TODO: function that simplify input expressions
def simplify(expr):
    '''
    Returns the simplified expression of the input expression
    >>> simplify("(((x|y)&z)|x&y)")
    '(x&y)|(z&(x|y))'
    '''     
    boolexpr = algebra.parse(expr)
    return boolexpr.simplify()

# TODO: function that output the equality of expressions
def equality(expr1,expr2):
    '''
    Returns if two expressions are equal
    >>> equality("x|y","y|x")
    True
    '''
    boolexpr1 = algebra.parse(expr1)
    boolexpr2 = algebra.parse(expr2)
    return boolexpr1 == boolexpr2

# TODO: function that gets all the sub-terms
def sub_terms(expr):
    '''
    Returns sub-terms of an expression to make it easier to simplify
    >>> sub_terms("(((x|y)&z)|x&y)")
    (AND(OR(Symbol('x'), Symbol('y')), Symbol('z')), AND(Symbol('x'), Symbol('y')))
    '''     
    return algebra.parse(expr).args

# TODO: function that gets all the unique symbols
def symbol(expr):
    ''' 
    Returns a set of unique symbols in an expression
    >>> symbol("(((x|y)&z)|x&y)")
    {Symbol('z'), Symbol('x'), Symbol('y')}
    '''
    return algebra.parse(expr).symbols

