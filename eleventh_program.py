#break break break break break break break break break 

for candidate in range(2,31):
    for divider in range(2,candidate):
        if candidate % divider == 0 :
            print('%2d is not a prime number - divider is %2d' % (candidate, divider))
            break 


# First way
for candidate in range(2,31):
    isPrime = True
    for divider in range(2,candidate):
        if candidate % divider == 0 :
            isPrime = False
            print('%2d is not a prime number - divider is %2d' % (candidate, divider))
            break 
if isPrime:
    print('%2d is prime!' % (candidate))

# Second way
for candidate in range(2,31):
    for divider in range(2,candidate):
        if candidate % divider == 0 :
            print('%2d is not a prime number - divider is %2d' % (candidate, divider))
            break 
else:
    print('%2d is prime!' % (candidate))


#exercise
#1
text = 'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.'


short_text = ''
 
words = text.split(' ')
counter = 0
 
for word in words:
    
    short_text += word+' '
    counter += 1
 
    if counter>=20:
        print(short_text)
        break
    

#2
definitions = [
    'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.',
    'Ein Kraftwandler ist eine mechanische Anordnung zur Veränderung einer Kraft in Bezug auf ihren Angriffspunkt, ihre Richtung oder ihren Betrag. Die einfachsten Kraftwandler sind Seile, Stangen, Rollen, schiefe Ebenen und Hebel. Dies sind gleichzeitig die grundlegenden einfachen Maschinen.',
    'La ventaja mecánica es una magnitud adimensional que indica cuánto se amplifica la fuerza aplicada usando un mecanismo (ya sea una máquina simple, una herramienta o un dispositivo mecánico más complejo) para contrarrestar una carga de resistencia.',
    'Cette notion s\'applique de manière évidente dans les systèmes de poulies et de leviers. Elle est centrale dans les systèmes de freinage : on applique une petite force sur un parcours important et l\'on obtient une force importante transmise au système de freinage pour une course de faible distance.'  
    ]


for definition in definitions:
    words = definition.split(' ')
    short_text = ''
    counter = 0
    
    for word in words:
        short_text += word + ' '
        counter += 1
        
        if counter>=20:
            print(short_text)
            break
         
#continue continue continue continue continue continue continue 
 
from cmath import cos


persons = ['Elizabeth', 'Steven@sales.mycompany.com','Sebastian','Margaret','Svetlana.mycompany.eu','Raphael']

domain = 'mycompany.com'

emails = []

for person in persons:
    if '@'in person:
        emails.append(person)
        continue
    email = person + '@' + domain
    emails.append(email)

for email in emails:
    print(email)  


for person in persons:
    if '@' in person:
        emails.append(person)
    else:
        email=person + '@'+domain
        emails.append(email)
  
for email in emails:
    print(email)        


#exercise

menu = '''
Choose what you want me to do for you:
1 - COFFEE
2 - TEA
3 - MAKE ME SMILE
---------------
To stop this script select 0
'''
smile = '''
 
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
   "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
 """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
            "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
              $$$o          "$$""$$$$$$""""           o$$$
               $$$$o                                o$$$"
                "$$$$o      o$$$$$$o"$$$$o        o$$$$
                  "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
                     ""$$$$$oooo  "$$$o$$$$$$$$$"""
                        ""$$$$$$$oo $$$$$$$$$$
                                """"$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$"
                                      "$$$""""
'''

#1
while True:
    print(menu)
    letter = input ('Enter your choice')
#1
    if letter == '1':
        print('Function COFFEE not implemented')    
        input('Press Enter')
        continue #wraca na początek programu
#2  
    if letter == '2':
        print('Function TEA not implemented')        
        input('Press Enter')
        continue
#3 
    if letter == '3':
        print(smile)
        input('Press Enter')
        continue
#4
    if letter == '0':
        break            
    input('You need to make a valid choice. Press ENTER and try again!')                

#exercise again

#1                              LICZONE RĘCZNIE  
initialCapital = 20000 #kwota na koncie
percent = 0.03 # oprocentowanie
maxTimeYears = 10 #klient postanawia trzymac kwote przez 10 lat

#po każdym roku oszczędzania zarobiona kwota jest dodawana do oszczędności 
# i zarabia odsetki przez pozostały czas.

first_year =  round(initialCapital * (percent+ 1),2)
second_year = round( first_year * (percent+ 1),2)
third_year =  round(second_year * (percent+ 1),2)
fourth_year = round( third_year * (percent+ 1),2)
fifth_year =  round(fourth_year * (percent+ 1),2)
sixth_year =  round(fifth_year * (percent+ 1),2)
seventh_year= round( sixth_year * (percent+ 1),2)
eighth_year = round( seventh_year * (percent+ 1),2)
ninth_year =  round(eighth_year * (percent+ 1),2)
tenth_year =  round(ninth_year * (percent+ 1),2)

print('The bank amount after',1,'year is', first_year)
print('The bank amount after',2,'years is', second_year )
print('The bank amount after',3,'years is', third_year )
print('The bank amount after',4,'years is', fourth_year )
print('The bank amount after',5,'years is', fifth_year )
print('The bank amount after',6,'years is', sixth_year )
print('The bank amount after',7,'years is', seventh_year)
print('The bank amount after',8,'years is', eighth_year )
print('The bank amount after',9,'years is', ninth_year )
print('The bank amount after',10,'years is', tenth_year )

print('After ten years, the amount earned will be', tenth_year-initialCapital)


#1                                      PĘTLA 
initialCapital = 20000
percent = 0.03
maxTimeYears = 10
year=0
capital=initialCapital
while year<maxTimeYears:
    year+=1
    capital=round((1+percent)*capital,2)
    print('after this year:', year,  'you will have:',capital)
else:
    print('the total revenue is', capital-initialCapital)

#2

number = 20730906    

number1 = number % 10
print(number1)
number2 = number - number1
number3 = number2 // 10
print(number3)

number4 = number3 % 10
number5 = number3 - number4
number6 = number5 // 10
print(number6)

number7 = number6 % 10
number8 = number6 - number7
number9 = number8 // 10
print(number9)

number10 = number9 % 10
number11 = number9 - number10
number12 = number11 // 10
print(number12)

number13 = number12 % 10
number14 = number12 - number13
number15 = number14 // 10
print(number15)

number16 = number15 % 10
number17 = number15 - number16
number18 = number17 // 10
print(number18)

number19 = number18 % 10
number20 = number18 - number19
number21 = number20 // 10
print(number21)


number=20730906
tmpnumber = number
sumOfDigits = 0
while tmpnumber >0:
    digit = tmpnumber % 10
    sumOfDigits += digit
    tmpnumber = tmpnumber//10
else:
    print('the sum of digits of ', number, ' is',sumOfDigits)

  
    
    
#3



text = '''United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.'''

     
        
listOfWords = text.replace('\n',' ').split(' ')
wordLength = 6
i=0
shortWords = 0
longWords = 0
while i< len(listOfWords):
    if len(listOfWords[i])>wordLength:
        longWords+=1
        
    else:
        shortWords+=1
    

print("Words shorter than ",wordLength,":",shortWords)
print("Words longer than ",wordLength,":",longWords)        