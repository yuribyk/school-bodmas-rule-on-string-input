#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 23:36:24 2019

@author: yuribyk
"""

#a="+3dcb(-10+5a)"
#a="-3(-10+5a)dcb"
#a= "-(-10+5a)(-2)"
#a= "a-b(c+d)-(a-b)cd-a"
#a= "(-1)(a+b)(a-b)(a+b)(a-b)(-1)"
a= "-(a+b)(a-b)"

def simplify_b(a):
    b=""
    
    for i in a:
        if i=="(" or i==")":
            b+="_"
        else:
            b+=i

    termz= b.split("_")
    terms= []
    for i in termz:
        if i!= "":
            terms.append(i)
            
    n= len(terms)
    for i in range (n):
        if terms[i]=="-":
            terms[i]="-1"
            
    #print(terms)
    import vector_plus_minus_gamma
    import vector_multiply
    
    for i in range (n):
       terms[i] = vector_plus_minus_gamma.simplify(terms[i])
    #print(terms)
    
    if n==1:
        return terms
    else:
        k= terms[0]
    
        for i in range (1,n,1):
            k= vector_multiply.multiply_simplify(k, terms[i])
    
        return k


print(simplify_b(a))
