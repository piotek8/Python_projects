#generate password


#for i in range(32,127):
#    print(i,chr(1))
import random

ints = range(32,127)
password = ''

for i in range(16):
    password += chr(random.choice(ints))

print('Password is:', password)

#exercise

#1
import random

min = 1
max = 6
dice = random.randint(min,max)

if dice == 1:
    print ('')
    print ('o')
    print ('')

elif dice == 2:
    print (' o')
    print ('')
    print ('o')

elif dice == 3:
    print ('  o')
    print (' o')
    print ('o')

elif dice == 4:
    print ('o o')
    print ('')
    print ('o o')

elif dice == 5:
    print ('o o')
    print (' o ')
    print ('o o')

else:
    print ('o o')
    print ('o o')
    print ('o o')

#2

import random 

dices = []

for i in range[5]:
    dices.append(random.randint(min,max))

dices.sort()
print(dices)


#text_function text_function text_function text_function text_function

line = 'this IS a very STRANGE text'

line.capitalize() # tekst rozpoczyna się dużą literą

line.title() # każde słowo rozpoczyna się od wielkiej litery

line.upper() # same duze literki

line.lower() # same małe literki

line.swapcase() # każdą małą literke zamienia na duza i na odwrot

line.casefold() # konwertuje znaki narodowe (np. niemieckie)

line.count('e') # liczy ilosc literek e

line.find('e') # podaje na ktorym miejscu znajduje sie literka e od lewej strony

line.rfind('e') # podaje na ktorym miejscu znajduje sie literka e od prawej strony
  
line.index('e') # jak find, tylko roznica jest jak znak nie wystepuje w napisie    

line.rindex('e') # jak rfind, tylko roznica jest jak znak nie wystepuje w napisie

line.find('p') # literka p nie wystepuje zwraca wartosc -1 
line.index('p') # literka p nie wystepuje zwraca blad

'e' in line #True - zwraca wartość, ponieważ literka 'e' występuje
'p' in line #False - zwraca wartość, ponieważ literka 'p' nie występuje 

line.startswith('this') # sprawdza czy dany tekst rozpoczyna i posługuje się danym ciągiem znaków

line.endswith('this')  # sprawdza czy dany tekst kończy i posługuje się danym ciągiem znaków

line = #' ' ' ... ' ' '(bez spacji) gdy tekst jest długi

line.split(' ') # rozbija napis na liste, tutaj spacja

' '.join(list) # łączy wyrazy w liscie, tutaj spacja

#exercise

poem = '''
1.Runą i w łunach spłoną pożarnych 
Krzyże kościołów, krzyże ofiarne 
I w bezpowrotnym zgubi się szlaku 
W lechickiej ziemi Orzeł Polaków. 
2.O, jasne słońce- wodzu Stalinie! 
Niech sława twoja nigdy nie zginie 
Niechaj jak orły powiedzie z gniazda 
Rosja i z Kremla płonąca gwiazda. 
3.Na ziemskim globie flagi czerwone 
Będą na wiatrach grały jak dzwony 
Czerwona Armia i wódz jej Stalin 
Odwiecznych wrogów na zawsze obali! 
4.Zaćmisz się rychło w czarnej godzinie 
Polsko- Twe córy i syny, 
Wiara i każdy krzyż na mogile, 
U stóp am legą w prochu i pyle! 
'''

lines = poem.split('\n')
 
for i in range(8):
    print(lines[i])
    print(lines[i+8])


for i in range(5,0,-1):
    if i > 1:
        print('wpis pojawi się za {} dni'.format(i))
    elif i == 1:
        print('wpis pojawi się za {} dnień'.format(i))
    else:
        print('wpis pojawi się dzisiaj.')        


 
 
 
 import time
 
# sprawdzenie wersji pythona
import sys
print(sys.version)
 
# zamiast
# print(time.clock(), time.localtime(time.clock()))
# korzystaj z funkcji time.perf.counter():
print(time.perf_counter(), time.localtime(time.perf_counter()))
 
 
 
 
 
 
 
 
 