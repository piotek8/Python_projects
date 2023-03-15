#function function function function function function function function

def PrintHello():
    print('Hello')
    return




#exercise


#PrintCat() - wyświetlającą kota

#PrintBear() - wyświetlającą misia

#PrintBat() - wyświetlającą nietoperza.





def PrintCat():
    txt = r'''
|\---/|
| o_o |
 \_^_/ '''
    print(txt)
    return

def PrintBear():
    txt = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
    print(txt)
    return

def PrintBat():
    txt = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/       '''
    print(txt)
    return          



#function2 function2 function2 function2 function2 function2 

def GiveWorkingDay ():
    
    from datetime import date
    from datetime import timedelta


    day = date.today()

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print ('working day for', day,'is',workingday)    
    
    return

GiveWorkingDay()    

#exercise

def DaysToEndOfYear():
    from datetime import date

    date_today = date.today()

    current_year = date_today.year
    
    date_end_year = date(current_year, 12, 31)

    delta = date_end_year - date_today

    print (delta.days)

DaysToEndOfYear()

#function_parameters function_parameters function_parameters function_parameters



def GiveWorkingDay (year,month,day):
    
    from datetime import date
    from datetime import timedelta


    day = date(year,month,day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print ('working day for', day,'is',workingday)    
    
    return

GiveWorkingDay(2017,9,30)    
GiveWorkingDay(2017,10,1)    
GiveWorkingDay(2017,10,2)    
GiveWorkingDay(2017,10,3)    
GiveWorkingDay(2017,10,4)    
GiveWorkingDay(2017,10,5)    
GiveWorkingDay(2017,10,6)         
GiveWorkingDay(2017,10,7)     



GiveWorkingDay(year = 2017, month = 12, day = 6)     
GiveWorkingDay(day = 6, month = 12, year = 2018)



#exercise

#1
def PrintAnimal(animal):
    if animal == 'cat':      
        print(PrintCat)
    elif animal == 'bear':
        print(PrintBear)
    elif animal == 'bat':
        print(PrintBat)
    else:
        print('Cannot print %s. Correct values for the parameter are: cat, bear, bat' % (animal))
    return

print(PrintAnimal('cat'))
print(PrintAnimal(animal='bear'))
print(PrintAnimal(animal='bat'))
print(PrintAnimal('unicorn'))

#2


def DaysToEndOfYear(year, month, day):
    from datetime import date
 
    date_today = date(year,month,day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)
 
DaysToEndOfYear(2020,12,20)
DaysToEndOfYear(2021,12,21)
DaysToEndOfYear(year = 2022, month = 12, day = 22)
DaysToEndOfYear(day = 23, month =12, year = 2023)


#exercise 2

#1

def PrintAnimal(animal = ''):
    # this function prints a cat, bear or bat ascii-art
    txt_cat = r'''
|\---/|
| o_o |
 \_^_/'''
    txt_bear = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
    txt_bat = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/  
     '''
 
    if animal == 'cat':
        print(txt_cat)
    elif animal == 'bear':
        print(txt_bear)
    elif animal == 'bat':
        print(txt_bat)
    else:
        print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)
    
    return




#2
from datetime import date
from secrets import token_hex
def DaysToEndOfYear(year=date.today().year, month=date.today().month, day=date.today().day):

 
    date_today = date(year,month,day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)
 
DaysToEndOfYear(2020,12,20)
DaysToEndOfYear(day = 23, month =12, year = 2023)
DaysToEndOfYear()
DaysToEndOfYear(year=2020)
DaysToEndOfYear(year=2020, month=10)
DaysToEndOfYear(day=1)


#


from datetime import date
from datetime import timedelta

def GiveWorkingDay(year=date.today().year, month = date.today().month, day = date.today().day):

    day = date(year,month,day)
    
    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    if day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day 
     
    
    return workingday

nextworkingday = GiveWorkingDay(2017,9,2)
print('Next working day after',2017,9,2,'is', nextworkingday)
nextworkingday = GiveWorkingDay()
print('Next working day after today is', nextworkingday)

print('Next working day after today is', GiveWorkingDay())

#exercise

def PrintAnimal(animal = ''):
    if animal == 'cat':      
        print(PrintCat)
    elif animal == 'bear':
        print(PrintBear)
    elif animal == 'bat':
        print(PrintBat)
    else:
        print('Cannot print %s. Correct values for the parameter are: cat, bear, bat' % (animal))
        return False
    return True

if PrintAnimal():
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')
 
 
if PrintAnimal('dog'):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')
 
 
if PrintAnimal('bat'):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')



#2
from datetime import date
def DaysToEndOfYear(year=date.today().year, month=date.today().month, day=date.today().day):

 
    date_today = date(year,month,day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    return (delta.days)

print('Date: 2020-12-20 days to end of year: %d' %( DaysToEndOfYear(2020,12,20)))
 
print('Date: 2020-12-21 days to end of year: %d' %( DaysToEndOfYear(2020,12,21)))
 
print('Date: TODAY days to end of year: %d' %( DaysToEndOfYear()))
6
#function function function function function function function function 

def DoAction(action, *parameter): #  *wyswietla wszystkie parametry
    print('action:',action)
    print('parameter:',parameter)
    for element in parameters:
        print(element,'=',parameter[element])
    return

DoAction('buy','shoes')
DoAction('buy','shoes','socks')
DoAction('buy','shoes','socks','t-shirt')

def DoAction(action,what, **parameter): #  *wyswietla wszystkie parametry
    print('action:',action)
    print('what:',what)
    print('parameter:',parameter)
    for element in parameters:
        print('element is', element)
    return

DoAction('buy','shoes',size=45,color='brown',type='sport')












