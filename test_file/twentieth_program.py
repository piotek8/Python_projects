#faults faults faults faults faults faults faults faults faults 
from multiprocessing.sharedctypes import Value
import sys


import sys

tasksPerPerson = 0

try:
    tasks = 32
    personsStr = input('How many persons are there in the team?')
    persons = int(personsStr)

    tasksPerPerson = tasks / persons
except:
    print('Something went wrong...',sys.exc_info()[0])
     
print('Every person should have around', tasksPerPerson, 'tasks')


#exercise

import sys


file_path = r'c:\temp\data_input\orders.csv'
 
with open(file_path,"r") as file:
 
    for line in file:
 
        line = line.replace('\n','')
        order = line.split(',')
    try:
        pharmacy_name = order[0]
        item = order[1]
        amount = int(order[2])
        print('Order from drugstore "%s", item "%s", amount %d',(pharmacy_name,item,amount))
    except:
        print("Problem with line %s" % line)
        print(sys.exc_info()[0])    
print("Processing finished")               
 
#print("Processing finished")
#Pharma A, Vitamin C,100
#Drugstore XYZ,Penicilin, 20, pills
#Drugstore ABC,Aspirin,60
#Pharma X,Montelukast,10
#Pharma at grocery,Amoxicillin,?
#Pharmacy 123,Cephalexin,100
#Pharmacy 123,Prednisolone Sodium Phosphate
#Pharma X,Nystatin,45



#except except except except except except except except except except except except

import sys

tasksPerPerson = 0

try:
    tasks = 32
    personStr = input('How many persons are there in the team?')
    persons = int(personsStr)

    tasksPerPerson = tasks/ persons

except ValueError as e:
    print('Sorry - you need to enter an integer number',e)

except ZeroDivisionError as e:
    print('Sorry - you need to enter value >0', e)
    
except:
    print('Something went wrong...',sys.exc_info()[0])

print ('Every person should have around', tasksPerPerson, 'tasks')        

#exercise

'''Pharma A, Vitamin C,100
Drugstore XYZ,Penicilin, 20, pills
Drugstore ABC,Aspirin,60
Pharma X,Montelukast,10
Pharma at grocery,Amoxicillin,?
Pharmacy 123,Cephalexin,100
Pharmacy 123,Prednisolone Sodium Phosphate
Pharma X,Nystatin,45'''
 
import sys
 
file_path = r'c:\temp\data_input\orders.csv'
 
 
with open(file_path,"r") as file:
 
    for line in file:
 
        line = line.replace('\n','')
        order = line.split(',')
 
        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print('Order from drugstore "%s", item "%s", amount %d' %
                      (pharmacy_name, item, amount))
 
        except ValueError as e:
            print("Problem with conversion. Check whether the amount is correct. Line: %s" % line)
 
        except IndexError as e:
            print("Missing information. Check whether the line is build of at least 3 fields separated by comma. Line: %s" % line)
 
        except:
            print("General error: %s" % sys.exc_info()[0])
            
print("Processing finished")

#else_finally else_finally else_finally else_finally else_finally 

 
import sys
tasksPerPerson = 0

try:
    tasks = 32
    personsStr = input ('How many persons are there in the team?') 
    persons = int(personsStr)
    
    tasksPerPerson = tasks / persons
    
except ValueError as e:
    print('Sorry - you need to enter an integer number',e)

except ZeroDivisionError as e:
    print('Sorry - you need to enter value >0', e)
    
except:
    print('Something went wrong...',sys.exc_info()[0])
else:
    print ('Every person should have around', tasksPerPerson, 'tasks')        

Finally: # zostana wykonane niezaleznie czy doszlo do bledu, czy tez nie
    print ('Script finished with/without errors')
    
#exercise

import os 

#1
line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
file = open(filepath,'w+')
file.write(line)
file.close()


#2  
line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
try:
    file = open(filepath,'w+')
    file.write(line)
    file.close()
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')



#3  
line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
try:
    file = open(filepath,'w+')
    file.write(line)
    file.close()
except FileNotFoundError as e:
    print('Error opening file',filepath,e)
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')



#4 
line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
try:
    file = open(filepath,'w+')
    file.write(line)
    value = int(line)
    file.close()
    print('The value saved in file is',value)
except FileNotFoundError as e:
    print('Error opening file',filepath,e)
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')



#5  
line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
try:
    file = open(filepath,'w+')
    file.write(line)
    file.close()
    value = int(line)
    print('The value saved in file is',value)
except FileNotFoundError as e:
    print('Error opening file',filepath,e)
except ValueError as e:
    print('The value entered cannot be converted to a number',line,e)
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')
else:
    print('Actions completed successfully')






#THE_END   THE_END   THE_END   THE_END   THE_END   THE_END   THE_END 









