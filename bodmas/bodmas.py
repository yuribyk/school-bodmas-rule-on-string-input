#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:22:23 2019

@author: yuribyk
"""

#a= "-b(aa-aaa)/a-aab"
a= "-b(aa-aaa)/a"


import simple_brackets

def division(a):
    b= a.split("/")
    print(b)
    
    for i in b:
        print(simple_brackets.simplify_b(i))
        
division(a)