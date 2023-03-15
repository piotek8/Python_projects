#time time time time time 
'''
from email.utils import localtime
import time
from xmlrpc.client import DateTime
print('Current time is ... unix epoch', time.time())
print('\n')
print('Current time is ... tuple', time.localtime(time.time()))
print('\n')
print('Current time is ... for human', time.asctime(time.localtime(time.time())))
print('\n')
#print('Current time is ... for human', time.localtime(time.clock()))
#print('\n')


import calendar
print(calendar.month(2022,8,w=5,l=2))

print(calendar.month(2022,8))

print('week day is',calendar.weekday(2022,8,16))

calendar.setfirstweekday(6)

print('is 2022 a leap year', calendar.isleap(2022)) # czy rok jest przestepny

print('Leap days 2000-2017 : ',calendar.leapdays(2000,2017)) # ile bylo dni przestepnych w tych latach

print(calendar.calendar(2022))

#exercise

import time                        #1                                        

print(time.time())                 #2                                

print(time.localtime(time.time())) #3

import calendar                    #4

print(calendar.month(2000,6))      #5                           

print(calendar.setfirstweekday(6)) #6

print(calendar.month(2000,7))      #7

print(calendar.isleap(2000))       #8

print(calendar.calendar(2019))     #9




#timedelta_date_datetime  timedelta_date_datetime  timedelta_date_datetime

import datetime

print('Minimum and maximum', datetime.MINYEAR, datetime.MAXYEAR)


d1 = datetime.timedelta(days=1,hours=2,minutes=-30)
print(d1)

d2 = datetime.timedelta(days=-1,hours=-2,minutes=-3)
print(d2)

print('timedelta sum',d1+d2)
print('')



from datetime import date

print('Today is',datetime.date.today())

today = datetime.date.today()
daysToPay = datetime.timedelta(days=7)
print('Today is', today)
print('Bills should be paid within:',daysToPay.days,'days')
print('The bill should be paid till:',today +daysToPay)



endOfTheWorld = datetime.date.max
print('The final end of world will happen (by Python):',\
    endOfTheWorld)
print (endOfTheWorld.weekday())

bornDate = datetime.date(2000,8,15)
today =datetime.date.today()
stayed = today - bornDate
print ('Until the end of the world it stayed %s days' % stayed.days)




from datetime import datetime

datetime.date

('now: \t',datetime.datetime.now())
('today: \t',datetime.datetime.today())
('utcnow: \t',datetime.datetime.utcnow())
('weekday: \t',datetime.datetime.today.weekday())

('%a',datetime.datetime.now().strftime('%a'))
('%A',datetime.datetime.now().strftime('%A'))
('%w',datetime.datetime.now().strftime('%w'))
('%a %A %w',datetime.datetime.now().strftime('%a %A %w'))
print('%Y-%m-%d_%H_%M_%S_%f', \
    datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S_%f'))


#exercise

inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]


#exercise

#1   
from hashlib import new
import math
import numbers
inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]
print('input data has',len(inputdata),'elements')
print('factor table has',len(factortable),'elements')
if len(inputdata) == len(factortable):
    i=0
    while i<len(inputdata):
        minvalue=inputdata[i]-factortable[i]*inputdata[i]
        maxvalue=inputdata[i]+factortable[i]*inputdata[i]
        print('minvalue=',minvalue,'maxvalue=',maxvalue)
        
        mininteger = math.floor(minvalue)
        maxinteger = math.ceil(maxvalue)
        print(mininteger,"\t",inputdata[i],"\t",maxinteger)
        i+=1
else:
    print("inputdata and factortable need to have equal number of elements")


#2
import random
inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

i=0
    
    while i<len(inputdata):
        minvalue=inputdata[i]-random.random[i]*inputdata[i]
        maxvalue=inputdata[i]+random.random[i]*inputdata[i]
        print('minvalue=',minvalue,'maxvalue=',maxvalue)
        
        mininteger = math.floor(minvalue)
        maxinteger = math.ceil(maxvalue)
        print(mininteger,"\t",inputdata[i],"\t",maxinteger)
        i+=1
    else:
         print("inputdata and factortable need to have equal number of elements")

from datetime import date, datetime
print (datetime.now())

'''

 













