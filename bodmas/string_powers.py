#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:37:23 2019

@author: yuribyk
"""

a= "ghghaaadddbbbccc/abcdeeeff"

#a= "aaadddbbbccc"
#a="adcbsvdfvsdfvadcbadcb"


def vc(a):
    variable_dict= {}
    poww= 0
    for i in a:
        try:
            poww= variable_dict[i]
            poww+=1
            variable_dict[i]= poww
        except KeyError:
            variable_dict[i]= 1
    return variable_dict
    

def division(a):
    
    parts= a.split("/")
    print(parts[0])
    numerator= vc(parts[0])
    denominator= vc(parts[1])
    
    print(numerator)
    print(denominator)
    div= {}
    for i in numerator.keys():
        for j in denominator.keys():
            if i==j:
                div[i]= numerator[i] - denominator[j]
    
    for i in denominator:
        try:
            div[i]
        except KeyError:
            div[i]=  -1* denominator[i]
            
    print(div)
    print()
    
    
    del div
    del numerator
    del denominator
    
    
division(a)