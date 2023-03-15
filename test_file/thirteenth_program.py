# a few math
#exercise
'''
percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,
           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
           8.740978348,6.174819567]
 
countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
             'Norway', 'Portugal','United Kingdom','Serbia','Germany','Albania',
             'France','Czech Republic','Denmark','Australia','Finland','Bulgaria',
             'Moldova','Sweden','Hungary','Israel','Netherlands','Ireland',
             'Cyprus','Italy']


sumOfPoints = 4988

#1
print ('max',max(percent)), ('min',min(percent))

#2
for i in range(len(countries)):

    print(percent[i], int(percent[i]), round(percent[i],2), 
          int(round(percent[i]*sumOfPoints/100,0)), countries[i])


#module module module module module module module 
import math #  
from math import * # 
print(math.pi)
print(math.floor(math.pi))


#exercise

#Oto lista wyników konkursu Eurowizja 2018:

percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,

           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,

           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,

           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,

           8.740978348,6.174819567]

import statistics
percent.sort()
print(percent)
print('Mediana wynosi:',statistics.median(percent))
print('Mediana wynosi:',statistics.median_low(percent))
print('Mediana wynosi:',statistics.median_high(percent))

#importowanie do sesji pythona wszystkie funkcje tak, 
# aby nie trzeba było ich poprzedzać nazwą modułu.
from statistics import *
print('Mediana wynosi:',median(percent))
print('Mediana wynosi:',median_low(percent))
print('Mediana wynosi:',median_high(percent))


# a few math more


f_smaller = 3.141592653589793
f_bigger = 3.87756392764
import math
 
print (math.cell(f_smaller),match.ceil(f_bigger) 
# math. ceil - najmniejsza liczba calkowita, ktora jest wieksza od podanego argumentu

print (math.floor(f_smaller),match.ceil(f_bigger) 
# math. ceil - najwieksza liczba calkowita, ktora jest mniejsza od podanego argumentu
       
print (math.cell(-f_smaller),match.ceil(-f_bigger)       
#math. ceil - najmniejsza liczba calkowita(na minusie), ktora jest wieksza od podanego argumentu     
       
print (math.floor(f_smaller),match.ceil(f_bigger) 
# math. ceil - najwieksza liczba calkowita(na minusie), ktora jest mniejsza od podanego argumentu
         
print (pow(2,8),pow(9,0.5))    # pierwiastek
# math.pow (..., ...) przyjmuje dwa argumenty - pierwszy to liczba **(potega), drugi to jaka potega   
       
print (sqrt(16))  
# math.sqrt zwraca pierwiastek

print (math.pi, math.e)  
# dwie stałe
# math.pi = 
# math.e =

print(math.sin(math pi/2), math.cos(math pi/4))
# sinus
# cosinus
    
    
#exercise

import math                                                    #1                                                      

#1° = (π * rad)/180                                            #2                                                    
#1 rad = 180°/π                                                #2                                                

degree = 360                                                   #3       
radian = degree * math.pi /180                                 #3           
print("%d degree is %f radians" % (degree, radian))            #3                                                       

degree = 45                                                    #4                   
radian = degree * math.pi/180                                  #4           
print('%d degree is %f radians' % (degree,radian))             #4                                               

print("%d degree is %f radians" % (360, math.radians(360)))    #5   
print("%d degree is %f radians" % (45, math.radians(45)))      #5

#########
#
##
##
#
#########

small_pizza_r = 0.22                                           #6          
big_pizza_r = 0.27                                             #6      
family_pizza_r = 0.38                                          #6          


small_pizza_r_price = 11.50                                    #6          
big_pizza_r_price = 15.60                                      #6      
family_pizza_r_price = 22.00                                   #6          





Pp_small_pizza  = math.pi * small_pizza_r**2                   #7 
Pp_big_pizza = math.pi *  big_pizza_r**2                       #7       
Pp_family_pizza = math.pi * family_pizza_r**2                  #7       


Pp_small_pizza_ =str(round(Pp_small_pizza,2))                  #7        
Pp_big_pizza_ =str(round(Pp_big_pizza,2))                      #7            
Pp_family_pizza_ =str(round(Pp_family_pizza,2))                #7

print('Pp small =',Pp_small_pizza_,'m²')                       #7           
print('Pp big =',Pp_big_pizza_,'m²')                           #7                         
print('Pp family =',Pp_family_pizza_,'m²')                     #7             
         
a = 11.50                           #Źle                              
b = 15.60                           #Źle                      
c = 22.00                           #Źle                                                  
         
a1 = 11.50                          #Źle                          
b1 = 15.60                          #Źle                              
c1 = 22.00                          #Źle                          
         
one_meter_small =(a/a1)             #Źle
one_meter_big =(b/b1)               #Źle                                                
one_meter_family =(c/c1)            #Źle                                                              

one_meter_small =(small_pizza_r_price/Pp_small_pizza)         #8      
one_meter_big =(big_pizza_r_price/Pp_big_pizza)               #8      
one_meter_family =(family_pizza_r_price/Pp_family_pizza)      #8          
                                                                            
print(one_meter_small )                                       #8          
print(one_meter_big )                                         #8              
print(one_meter_family )                                      #8              
  
math_ls = dir(math)                                           #9                  
print(math_ls)                                                #9          
                                                                            
#random random random random random random random random

 import random
 print('One random number:', random.randint(1,100) # 1 <=N <= 100)
       

'''
#exercise
#1
import random

#2
for i in range(10):
    print(random.randint(1,100))                                                            

#3                                                                          
number1 = random.randint(1,100)
print("The first generated number is %d" %(number1))                                                                           

counter = 1
number2 = random.randint(1,100)

while number1 != number2:
    counter+=1
    number2=random.randint(1,100)
    print(counter, number2)
    
print("I needed %d attempts to generate %d again" % (counter, number1))

#4
countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]
random.shuffle(countries)

groupNumber = 0 

for i in range(len(countries)):
    if  i % 4 == 0:
        groupNumber+=1
        print('----Grupa %d----', % (groupNumber))
    print(countries[i])        



































 