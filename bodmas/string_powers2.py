#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 22:50:42 2019

@author: yuribyk
"""


a= "-6ghghaaadddbbbccc/-26abcdeeeff"

#a= "aaadddbbbccc"
#a="adcbsvdfvsdfvadcbadcb"

#a= "-fg(caab-bcba)(-xy)/ba"
#a= "-fg(caab-bcba)(-xy)"

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
    
def simplify(a):
    pass

def division(a):
    
    parts= a.split("/")
    #print(parts[0])
    numerator= vc(parts[0])
    denominator= vc(parts[1])
    
    #print(numerator)
    #print(denominator)
    
    
    for i in numerator.keys():
        try:
            numerator[i]-=denominator[i]
        except KeyError:
            pass
    for i in denominator.keys():
        try:
            numerator[i]
        except KeyError:
            numerator[i]= -1*denominator[i]
        
    
    print(numerator)

division(a)
    



































