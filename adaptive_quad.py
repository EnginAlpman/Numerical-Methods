#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:11:35 2019

@author: engin
"""

# a is the lower bound b is the upper bound.
# e is the error tolerance
# you can integrate the function you want via changing f(x) in the code


import numpy as np

def f(x):
    s = (100/(x*x)) * np.sin(10/x)
    return s


def simpson(a,b):
    h= (b-a)/2
    s = h/3 * (f(a) + 4*f(a+h) + f(b))
    return s


def adaptive_quad(a,b,e):
    s_1 = simpson(a,b)
    c = (a + b) / 2
    s_2 = simpson(a,c) + simpson(c,b)
    e_c= s_2-s_1 #error control
    
    if abs(e_c) < 15 * e:
        answer = s_2 + (e_c) / 15
        return answer
    else:
        
        l = adaptive_quad(a,c,e/2)
        r = adaptive_quad(c,b,e/2)
        answer = l + r
        
        return answer
    
a = 1
b = 3
e = 1e-4

ans = adaptive_quad(a,b,e)

print("Answer is: " + str(ans))
