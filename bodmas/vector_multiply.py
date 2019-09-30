#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 22:26:51 2019

multiplying two vectors

@author: yuribyk
"""
#a="-2ab(-cc-dbbd)"

#a=[[-3, 'aa'], [3, 'd'], [-1, ""], [-7, 'a'], [8, 'h']]
#b=[[5, 'b'], [-1, 'aa'], [-5, ""]]

#b=[[1,'a'],[1,'b']]
#a=[[1,'a'],[-1,'b']]

#a=[[1,'a'],[-1,'b']]
#b=[[1, 'aa'], [-1, 'ab'], [1, 'bb']]


def add_vector(a):
    
    d=len(a)
    #print(d)
    for i in range(d):
        c=a[i][1]
        for j in range(d):
            if i!=j and c==a[j][1]:
                a[j][0]+=a[i][0]
                a[i][0]=0
                
    #print(a)
    b=[]
    for i in a:
      if i[0]!=0:
          b.append(i)
    #print(b)
    return b
       

def variable_counter(a):
    if type(a)==int:
        return [a,0]
    
    var_raw_lib=[]
    for i in a:
        try:
            count=int(i)
            
        except ValueError:
            var_raw_lib.append(i)
    
    var_counter=set(var_raw_lib)
    var_counter=sorted(var_counter)
    #print(var_counter)
    
    data_var=""
    # var_counter is total variables in one matrix element
    for i in var_counter:
        counter=var_raw_lib.count(i)
        k=(i*counter)
        
        data_var+=k
    
    return data_var

    
"""we want to multiply two vectors"""
def mul_vector(a,b):
    m=[]
    for i in a:
        for j in b:
            m.append([i[0]*j[0],i[1]+j[1]])
    
    return m

def multiply_simplify(a,b):
      #raw multiplication  
    x=mul_vector(a,b)
    #rearranging coefficients
    for i in x:
        i[1]=variable_counter(i[1])
    #ading vectors
    y=add_vector(x)
    #print(y)
    return y
#print(a)
#x=multiply_simplify(a,a)  #2
#y=multiply_simplify(x,a)  #3
#z=multiply_simplify(x,x)  #4
#za=multiply_simplify(z,a) #5
#zb=multiply_simplify(y,y) #6
#y=multiply_simplify(x,a)
