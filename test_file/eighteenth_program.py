#function_switch function_switch function_switch function_switch function_switch 

'''def WeekDayInFrench(dayNumber): 
    names = {
        0:'lundi',
        1:'mardi',
        2:'mercredi',          
        3:'jeudi',
        4:'vendredi',
        5:'samedi',                
        6:'diamache'       
    }

    return names.get(dayNumber,'error')
print(WeekDayInFrench(3))
print(WeekDayInFrench(7))


#exercise

#1
import math
from re import X

def GiveGeomSeqElement(a1 = 2,factor = 2,index = 2):
    #returns n-th term of geometric sequence starting with element a1 and having  
    value = a1*pow(factor,index-1)
    return value
print('element 64 =',GiveGeomSeqElement(1,2,64))
    #n1 = 2
    #n64 = ?

    
#2
a1=3 
#a2,a3...a10 = ?
factor=2 
maxindex=10

for i in range(1,maxindex+1):
    an = GiveGeomSeqElement(a1=a1,factor=factor,index=i)
    print('a\a',i,'=',an)


#3
def GiveFactorForGeomSeq(term,nextterm):
    #returns factor for geometrical sequence having two following terms of the sequence
    return nextterm/term
print('12',GiveFactorForGeomSeq(12,24))
print('The factor',GiveFactorForGeomSeq(24,12))

#4
#suma pierwszych wyrazow ciagu

a1 = 2 # domyslna wartosc
factor = 2 # pierwszy wyraz ciagu
n = 2 #ile elementow ma byc dodanych
r = 3 #wspolczynnik
a2 = factor

# iloczynem kolejnej liiczby 2,4,8,16 ; wspolczynnik 2
def GiveSumOfNElementsGeomSeq(a1, factor, n):
    value = a1*(1-pow(factor,n))/(1-factor)
    return value
print('Sum of n elements is', GiveSumOfNElementsGeomSeq(2,3,4))



#5

#plik modułu:

def GiveGeomSeqElement(a1=2,factor=2,index=2):
    #returns n-th term of geometric sequence starting with element a1 and having 
    value = a1*pow(factor,index-1)
    return value
 
def GiveFactorForGeomSeq(term, nextterm):
    #returns factor for geometrical sequence having two following terms of the sequence
    return nextterm/term
 
def GiveSumOfNElementsGeomSeq(a1=2, factor=2, n=2):
    #returns sum of n first elements of geometrical sequence with first term a1 and factor
    sumN = a1*(1-pow(factor,n))/(1-factor)
    return sumN


#plik skryptu:

from math import geom
print('2^64 =',geom.GiveGeomSeqElement(1,2,64))

a1=3
factor=2
maxindex=11
for i in range(1,maxindex+1):
    an = geom.GiveGeomSeqElement(a1=a1,factor=factor,index=i)
    print('Term ',i,'=',an)

print('Factor is', geom.GiveFactorForGeomSeq(12,24))
'''

#user_input user_input user_input user_input user_input user_input 

filename = input('Enter filename:')
print('The file name is: %s '(filename))

while True:
    filesizeStr = input('Enter the max file size:')
    if filesizeStr.isdecimal():
        filesizeInt = int (filesizeStr) 
        break
print('The max size is %d' % (filesize))

print('Size in KB is %d' % (filesize *1024))


#exercise


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


a1 = input('a=')
b1 = input('b=')
c1 = input('c=')


if not (check_int(a_str)) and (check_int(b_str)) and (check_int(c_str)) :
    print("a, b and c need to be int!")
else:
    a = int(a1)
    b = int(b1)
    c = int(c1)
 
    if a == 0:
        print('a cannot be 0!')
    else:
        delta = b**2 - 4*a*c
 
        if delta < 0:
            print("there is no solution")
        elif delta == 0:
            x1 = -b/(2*a)
            print("there is one solution: %.2f" % (x1))
        else:
            x1 = (-b-delta**0.5)/(2*a)
            x2 = (-b+delta**0.5)/(2*a)
            print("there are two solutions: %.2f and %.2f" % (x1,x2))
















       
            
            
            
            
            
            
            

  
