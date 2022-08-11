
# format napisów
from email import message


message1 = 'Processing file %s'
print(message1 % ('file_1.txt')) 

message2 = 'File %s has size %d KB'
print(message2 % ('file1_txt',100))

message3 = 'File %20s has size %10d KB' # %s ma zarezerwowane 20 znakow, %d jest zarezerwowane 10 znakow
print(message3 % ('file1.txt',100))

# %d - liczba
# %s - napis

message4 = 'Processing {0:s}' # 0 oznacza jeden(python liczy od 0) parametr, ktory zostanie wstawiony i bedzie napisem
print(message4.format('file1.txt'))

message5 = 'File {0:s} has size {1:d}'
print(message5.format('file1.txt',100))

message6 = 'File {0:20s} has size {1:10d}'
print(message6.format('file1.txt',100))

#exercise
helloMessage = "Hello %s!" #1
print(helloMessage)

print(helloMessage % ('Kate'))  #2
print(helloMessage % ('Chris')) #2

helloMessage = "Hello {0:s}!" #3

print(helloMessage.format('Kate'))  #4
print(helloMessage.format('Chris')) #4

helloMessage = "%s has %d %s" #5

print(helloMessage % ('Kate',1,'animal')) #6
print(helloMessage % ('Chris',100000,'$')) #6

helloMessage = "{0:s} has {1:d} {2:s}" #7

print(helloMessage.format('Kate',1,'animal')) #8
print(helloMessage.format('Chris',100000,'$')) #8

line1 = 'ICE CREAM {0:20s} {1:6d}€'           #9 B
line2 = 'TRIP TO VENICE {0:20s} {1:6d}€'      #9 A
line3 = 'PIZZA HAWAII {0:20s} {1:6d}€'        #9 D
print(line1.format('costs',3))                #9 L
print(line2.format('costs',119))              #9 Y
print(line3.format('costs',6))                #9 !

line = '{0:20s} costs {1:6d} €'               #9 F
print(line.format('ICE CREAM',3))             #9 I                    
print(line.format('TRIP TO VENICE',119))      #9 N
print(line.format('PIZZA HAWAII',6))          #9 E

line ='{0:s} {1:d}'
print(line.format('ICE CREAM ',3))          #10
print(line.format('TRIP TO VENICE',119))    #10
print(line.format('PIZZA HAWAI',6))         #10


# float float float float float float float


five = 5    
three = 3
 

print (five/three)
print (five//three)  # ile 3 miesci sie w 5 (1)
print (five % three) # ile w dzieleniu zostanie reszty (2)

print(float('inf') >999999999999999999999999999999999999)
print(-float('inf') >999999999999999999999999999999999999)


#exercise
name = 'Piotr'                                                   #1

age = 22                                                         #2

daysInYear = 365                                                 #3

message = '%s is %d years old, so is about %d days old'          #4
print(message % (name,age,daysInYear))                           #4

message = '%s is %d years old, so is about %d days old'          #5
print(message % (name,age,daysInYear*age))                       #5

name = 'Chris'                                                   #6
age = 17                                                         #6      
print(message % (name,age,daysInYear*age))                       #6
 
message = '%s is %d years old, so is about %d days old'          #7

print(type(name))
print(type(age))
print(type(daysInYear))

message = '{0:s} is {1:d} years old, so is about {2:d} days old' #8
print(message.format(name,age,daysInYear*age))                   #8



N1 =(1234567890 // 12345) #100005                                #9
N2 =(1234567890 % 12345) #6165                                   #9
print('1234567890 divided by 12345 is',N1, 'and the rest is',N2) #9












