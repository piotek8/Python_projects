#tuple tuple tuple tuple tuple tuple tuple tuple
"""
from tkinter.tix import TEXT


Tax = (4,7,8,23)
print(Tax[2])
print(Tax[-1])
print(Tax.index(7)) # na ktorej pozycji jest liczba 
print(Tax.count(8)) # ile liczba 8 jest razy w liście
print(max(Tax))

TaxList = list(Tax) #Tax.revert()
TaxList.append(30) #dodanie wartosci 30 do listy
NewTax = tuple(TaxList) # zamiana z listy na krotke,czyli tuple

print(Tax)
print(TaxList)

a=1
b=10
print('a =',a,'\tb =',b)

a=1
b=10
print('a =',a, '\tb =',b)

#temp = a
#a = b 
#b = temp
(a,b) = (b,a)
print('a =',a, '\tb =',b)

#exercise

import email


marketing = ['loyality program','client promotion','market research'] #1

marketing.append('public relations')                                  #2  
print(marketing)

print(marketing[3])                                                   #3 

marketing.insert(2,'investor relations')                              #4
print(marketing)                                                      #4

emailMarketing = marketing.copy()                                     #5
print(emailMarketing)                                                 #5   

emailMarketing.sort()                                                 #6 
print(emailMarketing)                                                 #6 

internalEmails = ['internal communication']                           #7

emailMarketing.extend(internalEmails)                                 #8
print(emailMarketing)                                                 #8         

emailTuple = tuple(emailMarketing)                                    #9
print(emailTuple)                                                     #9 

#dictionary dictionary dictionary dictionary  dictionary dictionary 

from typing import Counter


CountryLeaders = {'PL': 'Duda', 'US': 'Trump'}

#print(CountryLeaders['US'])
CountryLeaders['DE'] = 'Merkel'

print(CountryLeaders.keys())
print(CountryLeaders.values())
print(CountryLeaders.items())
print(CountryLeaders.popitem())

print(CountryLeaders.setdefault('FR','Macron'))

print(CountryLeaders.get('RU'))

NewLeaders = {'RU': 'Putin', 'DE':'Schulz'}
print(NewLeaders)
CountryLeaders.update(NewLeaders)

print(CountryLeaders)

#exercise

chanels = {'Google' : 1480,'Email' : 300,'Email' : 300,'TV Spot' : 700}                   #1  

print(chanels['Email'])                                                                   #2  

chanelsUpdate = {'Natural Traffic': 520, 'News' : 600}                                    #3   

print(chanels.update(chanelsUpdate))                                                      #4 

print(chanels.keys())                                                                     #5 

print(chanels.pop('Email'))                                                               #6 

#if if if if if if if if if if if if if if if if

age = 17   

if age >= 18:
    print('You are adult and you can buy alcohol')   
else:
    print('You are too young, you cannot buy alcohol')

isDrunk = False

if age >= 18 and not isDrunk :
    print('You are adult and you can buy alcohol')  
else:
    print('Sorry, we cannot sell you alcohol')

isRestricedArea = False 

if age >= 18 and not isDrunk and not isRestricedArea :
    print('You are adult and you can buy alcohol') 
else:
    print('Sorry, we cannot sell you alcohol')
"""
#exercise   

from ast import If

#1
MIN_LIKES = 500
MIN_SHARES = 100

num_likes = 1300
num_shares = 55

if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES :
    print('Ceny spadną o 10%.')
else:
    print('Brak wystarczającej ilości lajków i sharów. Ceny pozostają bez zmian.')


#2
isPizzaOrdered = True                 #o wartości True/False, która informuje, czy klient kupił Pizzę
isBigDrinkOrdered = True              #o wartości True/False, która informuje, czy klient zamówił duży napój
isWeekend = True                      #o wartości True/False, która informuje, czy jest weekend

if (isBigDrinkOrdered or isPizzaOrdered) and not isWeekend :
    print('Otrzymujesz kupon na Burgera')
else:
    print('Zachęcamy do dalszych zakupów.')

#3

diskSize = 14000
diskSizeUsed = 1333
fileSize = 10

if diskSize > (diskSizeUsed + fileSize) : # if diskSize - diskSizeUsed >= fileSize :  druga możliwość
    print('Plik może zostać pobrany.')
else:
    print('Brak wystarczającego miejsca na dysku.')

#if elif if elif if elif if elif if elif if elif if elif 

age = 27
isDrunk = True
isRestrictedArea = False

if age <18:
    print('You are too young to buy alcohol')
else:
    if isDrunk:
        print('Are you drunk? We cannot sell you alcohol.')
    else:
        if isRestrictedArea:
            print('Resticted area. Alcohol is forbidden')
        else:
            print('Ok, you can buy alcohol')
print('-----')    

# lepsze wersja 

if age <18:
    print('You are too young to buy alcohol')
elif isDrunk:    
    print('Are you drunk? We cannot sell you alcohol')
elif isRestrictedArea:
    print('Resticted area. Alcohol is forbidden')
else:
    print('Ok, you can buy alcohol')

#exercise

MIN_LIKES = 500
MIN_SHARES = 100

num_likes = 300
num_shares= 550

if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
    print('Today our prizes drop 10%!')
else:
    if MIN_SHARES > num_shares:    
        print('We still need more likes to start the promotion')
    else:
        print('We still need more shares to start the promotion')      
       
# lepsze wersja 

if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
    print('Today our prizes drop 10%!')
elif num_likes <MIN_LIKES:
     print('We still need more likes to start the promotion')
else:
     print('We still need more shares to start the promotion')

#2

isPizzaOrdered = True   
isBigDrinkOrdered = True
isWeekend = True        

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('You have a burger for free')
else:
    if isWeekend:
        print('Come back on non-Weekend day')
    else:
        print('You need to order Pizza or Big drink to have a Burger coupon')
        
# lepsze wersja
if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('You have a burger for free')
elif isWeekend:      
    print('Come back on non-Weekend day') 
else:       
    print('You need to order Pizza or Big drink to have a Burger coupon')

#ternary_operator ternary_operator ternary_operator ternary_operator ternary_operator     
itRains = True
if itRains:
    print('we stay at home')
else:
    print('we go out') 

print('we stay at home') if itRains else 'we go out'          

#exercise

musclePain = True                           #1
fever = True                                #1
weakness = True                             #1

#2
if (musclePain and fever and weakness)     
    print('suspicion of influenza')        
else:                                      
    print('The flu is unlikely')           

#3
if (musclePain and fever and weakness)      
    print('suspicion of influenza')         
elif not(musclePain or fever) and weakness: 
    print('Just take a rest!')              
else:                                       
    print('you may be cold')                


isMan = True                                #4

#5
if musclePain and fever and weakness or  isMan and (musclePain or fever or weakness):
    print("suspicion of influenza")
elif not (musclePain and fever) and weakness:
    print("Just take a rest!")
else:
    print("this only cold")

#6
isCheckCompleted = False
 
print("CHECK IS COMPLETED" if isCheckCompleted else "CHECK NOT DONE YET!")



