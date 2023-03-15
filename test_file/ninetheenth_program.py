'''            
#os_module os_module os_module os_module os_module os_module 



from gettext import Catalog
import os 
import time

print('Current directory is:', os.getcwd())

currentDir = os.getcwd()
filename = 'results.txt'
fullpath = os.path.join(currentDir,filename)
print('\nThe constructed file path is:', fullpath)

relativePath = 'output.txt'
print('\nThe absolute path is:', os.path.abspath(relativePath))

filepath = r'c:\temp\results.txt'
print('\nThe file name part is:', os.path.basename(filepath))
print('The directory part is:', os.path.exists(filepath))

print('\nIs file existing?', os.path.exists(filepath))

if os.path.exists(filepath):
    print('\nLast modfiy date is:', os.path.getmtime(filepath))
    print('Last modify date is:',time.localtime(os.path.getmtime(filepath)))
   
    print('\nFile size is:', os.path.getsize(filepath))
   
    print('\nIs it a file?', os.path.isfile(filepath))
    print('Is it a dir?',os.path.isdir(filepath))

    print('\nPath splitted:', os.path.split(filepath))
    print('Only file name part:', os.path.split(filepath)[l])

    print('\nPath splitted into drive:',os.path.splitdrive(filepath))
    print('Only drive:',os.path.splitdrive(filepath)[0])

#exercise
#1
import os 
import time

#2
dir = input('Enter directory name: ')

#3
if not os.path.isdir(dir):
    print("%s must be a directory" % dir)    
#4    
else:
 
    file = input('Enter filename saved in directory %s: ' % dir)
#5    
    path = os.path.join(dir, file)
 
    if not os.path.isfile(path):
        print('File %s does not exist!' % path)
 
    else:
    
        print('displaying properties of file %s' % path)
 
        print('Last modified date', time.localtime(os.path.getmtime(path)))
        print('Size in bytes', os.path.getsize(path))
 
        print('Current directory is: ', os.getcwd())
        print('Relative path to the file is', os.path.relpath(path))


#file_path_control file_path_control file_path_control file_path_control

import os
fileIsOk = False

while True:
    
    filename = input ('Enter path to results file: ')
    if os.path.isfile(filename):
        break
    else:
        print('File name is not correct, try again!')



print('The results file is %s'(filename))



#exercise
#pliki csv i zlokalizowane w c:\temp\data_input
#godz 19

#1
import os 
import datetime
from datetime import date 

#2
data_input_catalog = 'c:\temp\data_input'

#3
data_output_catalog = 'c:\temp\data_output'

#4
today = datetime.date.today()

#5
today_output_catalog = os.path.join(data_output_catalog, today.strftime("%Y-%m-%d"))
 
#6
is_input_catalog_ok = os.path.isdir(data_input_catalog)

#7
is_output_catalog_ok = os.path.isdir(data_output_catalog)

#8
is_today_output_catalog_ok = not(os.path.isdir(today_output_catalog)) and \
                             not(os.path.isfile(today_output_catalog))

#9
if (is_input_catalog_ok) and (is_output_catalog_ok) and (is_today_output_catalog_ok):
    print ('Conditions met! We can continue!')

#10
else:
    print('Prerequisites not met! Check the paths!')
    #display detailed error conditions
    if not is_input_catalog_ok:
        print("Input catalog %s must exist!" % data_input_catalog)
    if not is_output_catalog_ok:
        print("Output catalog %s must exist!" % data_output_catalog)
    if not is_today_output_catalog_ok:
        print("Today's output %s cannot exist (neither as file nor as directory)!" % today_output_catalog)    

#files

file = open('c:\\temp\\joke.txt','r') # drugi parametr r - read otwiera plik dla odczytu tylko

content = file.read()                                                   
print(content)                                                          

file.close()                                                                

with open ('c:\\temp\\joke.txt','r') as file:               
    content = file.read()                                       
    print(content)                                                          

with open ('c:\\temp\\joke.txt','r') as file:                               
    for line in file:                                                               
        print(line)                                                     

file = open('c:\\temp\\joke.txt','r')                                                   
for line in file:                                                   
    print(line)                                                                                     
file.close()                                                                                               

file = open('c:\\temp\\joke.txt','r')                                       
for line in file.readlines():                                                       
    print(line)                                                         
file.close()                                                                        

file = open('c:\\temp\\joke.txt','r')                                       
for line in file.readlines():                                                   
    print(line)                                                             
file.close()                                                                                

file = open('c:\\temp\\joke.txt','r')                                       

fragment = file.read(10) # czyta max 10 bajtów
while fragment:
    print(fragment)
    fragment = file.read(10)
                                                             
file.close()                                                                                

'''
#exercise

'''
Pharma A, Vitamin C,100
Drugstore XYZ,Penicilin, 20, pills
Drugstore ABC,Aspirin,60

Pharma X,Montelukast,10

file = r'c:\temp\data_input\orders.csv'

with open(file_path,"r") as file:
 
    for line in file:
 
        line = line.replace('\n','')
        order = line.split(',')
 
        if len(order) == 3:
            print('Order from drugstore "%s", item "%s", amount %s' %
                  (order[0],order[1],order[2]))
        else:
            print("Line %s malformed!!!" % line)
 
print("Processing finished")

'''


#save_to_file save_to_file save_to_file save_to_file save_to_file

filename = 'C:\Windows\Temp\\temp.output.txt'

line = 'Europe'

cities = ['London','Berlin','Paris','Warsaw','Madrid','Rome']

file = open(filename,'w+') # w+ plik do odczytu i zapisu # a+ do odczytu i zapisu nie czyszcząc zawartości tego pliku

file.write(line)

file.writelines(cities)


for city in cities:
    file.write(city+'\n')


file.close()


#exercise 1 

#1
import os

#2
webaddresses = []

#3
line = input('Please enter the website address')

#4
while line != '':
    #5
    webaddresses.append(line)
    line = input('Enter web address like "www.python.org" or press ENTER to stop: ')
   
print(webaddresses)

#6
dirname = os.getcwd()

#7
filename = input('Please enter a file name')

#8
filepath = os.path.join(dirname,filename)

#9
file = open(filepath,'w+')

#10
for webaddress in webaddresses:
    file.write(webaddress+'\n') 
#11
file.close()

#exercise 2

import os 

filename =input('Enter filename with web addresses to read: ')

while not os.path.isfile(filename):
    print("File does not exist. Try again: ")
    filename =input('Enter filename to read: ')
webaddresses=[]
with open(filename,'r') as file:
    for line in file:
        webaddresses.append(line.replace("\n",''))
for line in webaddresses:
    if line.endswith('.pl'):
        print(line,'is a polish web page')
    else:
        print(line, 'is not a polish web page')
        
        
#exercise 3     

import os
filename =input('Enter filename with web addresses to read: ')
while not os.path.isfile(filename):
    print("File does not exist. Try again: ")
    filename =input('Enter filename to read: ')
webaddresses=[]
with open(filename,'r') as file:
    for line in file:
        webaddresses.append(line.replace("\n",''))
dirname = os.path.dirname(filename)
websPathPL = os.path.join(dirname,'webs_pl.txt')
websPathOther = os.path.join(dirname,'webs_other.txt')
filePL = open(websPathPL,'w')
fileOther = open(websPathOther,'w')
for line in webaddresses:
    if line.endswith('.pl'):
        filePL.write(line+"\n")
    else:
        fileOther.write(line+"\n")
filePL.close()
fileOther.close()



