#for for for for for for for for for for for 

import email


persons = ['Elizabeth','Steven','Margaret','Svetlana','Raphael']

domain = 'mycompany.com'

for person in persons:
    email = person + '@'+ domain
    print('Email for\t', person, '\tis\t', email)
else:
    print('\t\t\t  end of the list')
    
#exercise
#1    
data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']
for date in data:
    print(date.upper())

#2    
data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']
for element in data:
    elements = element.split(':')
    print(elements[0].upper())
    print(elements[1])

#   if  elements[0] in data:                                
#       print(elements.split(':') and elements.upper())     Ź L E 
#   if  elements[1] in data:
#       print(elements.split(':') and elements.lower())       

#3
data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']
for element in data:
    elements = element.split(':')
    if elements[0] == 'Error':
        print(elements[1].upper())
    else:
        print(elements[1])

    
   # print(elements[0].upper())
   # print(elements[1])
   
#for for for for for for for for for for for   
for number in range (1,21): # liczy od 1 do 20 i co ile, czyli co 2
    if number %2 == 0:
        print('Number %2d is %s' % (number,'even')) #even - parzysta
    else:
        print('Number %2d is %s' % (number,'odd')) #nieparzysta - odd
    #print(number)
  
#exercise 
string_A = '+---+---+---+---+'  
string_B = '|   |   |   |   |'

for i in range(1,11):
    print(string_A)
   
for i range(1,11):
    if i % 2 == 0:
        print(string_A)
    else:
        print(string_B)  
        

for i in range(1,10):
    print('x'*i)
      
for i in range(1,10):
    if i % 2 == 0:
        print('x'*i)
    else:   
        print('o'*i)
 
#for for for for for for for for for

for x in range (1,6):
    line = str(x)
    for y in range (1,6):
        line +=  ('\t%3d' % (x*y))
    print(line)
#exercise
#1
i = 10
result = 1
 
for j in range(1,i+1):
    result *=j
print(i,result)    

#2
x = 10
 
for i in range(1,x+1):
    result = 1
    for j in range(1,i+1):
        result *= j
    print(i, result)
    
Chcesz wyznaczyć wartości silnia dla liczb od 1 do 10. 
Napisz pętlę for iterującą przez wartości od 1 do 10, 
a w tej pętli for wyznaczaj silnię dla każdej z tych liczb

#3
list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']


for i in list_noun:
    for x in list_adj:
        print(x, i)        





