#array of characters

s = 'A Python script'
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[2:8]) # znaki od 2 do 7
print(s[:8])  # znaki do 8
print(s[8:])  # znaki od 8

message = 'Document "cv.doc" was printed on printex: XEROX'
print(message.find(':'))
print(message[message.find(':'):])
print(message[message.find(':')+2:])
print(message[message.find('"')+1:])
tmp = message[message.find('"')+1:]
print(tmp[:tmp.find('"')])


#exercise
q = 'THE EYES'                                 #1                              
print(q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7]) # 
print(q[0:])

q = 'a gentleman'
print(q[3],q[6],q[7],q[2],q[0],q[4],q[5],q[1],q[8:])

    #012345678910111213 
n = 'THE MORSE CODE'
print(n[1],n[2],n[6],n[2],n[3],n[10],n[11],n[4],n[2],n[9],n[12],n[11],n[0],n[7])

line ='Program "Kropka nad i" nadamy o: 22:00'
time = line[line.find(':')+2:]
print(time)
tmp = line[line.find('"')+1:]
print(tmp)
title = tmp[:tmp.find('"')]
print(title)

line ='Program "Pytanie na śniadanie" nadamy o: 6:00'
time = line[line.find(':')+2:]
print(time)
tmp = line[line.find('"')+1:]
print(tmp)
title = tmp[:tmp.find('"')]
print(title)


#exercise2
ShoeSize = 42.5                                         #1                                    
number = (((ShoeSize*5+50)*20 )+1017)-2000              #1                    
print(number)                                           #1                            

number2 = (15*2+10)/2-15                                #2                   
print(number2)                                          #2                        

s= 2+2*2                                                #3        
s1 = 7+7/7+7*7-7                                        #3                    
print(s1)
print(s)

presence = 0.85                                                             #4        
note = 3.5                                                                  #4   
term_paper = False                                                          #4          
print('you need to be present and have good notes or do the final work',    #4                                                               
      presence >= 0.8 and (note >= 3.0 or term_paper) )                     #4                                              
print('you need to be present and have good notes and do the final work',   #4                                                                
      presence >= 0.8 and note >= 3.0 and term_paper )                      #4                                             
student =  ()                                                               #4    
# 80% obecności, żeby zaliczyć semestr
# >= 3.0 średnia,żeby zaliczyć semestr  
    

presence = 0.80                                                                
note = 3.0                                                              
term_paper = False
print('you need to be present and have good notes or do the final work',
      presence >= 0.8 and note >= 3.0 or term_paper)
print('you need to be present and have good notes and do the final work',
      presence >= 0.8 and note >= 3.0 and term_paper)


presence = 0.40                                                            #6                                                           
note = 2.5                                                                 #6                                                    
term_paper = True                                                          #6                                                     
print('you need to be present and have good notes or do the final work',   #6                                                    
      presence >= 0.8 and note >= 3 or term_paper)                         #6                                
print('you need to be present and have good notes and do the final work',  #6                                                     
      presence >= 0.8 and note >= 3 and term_paper)                        #6        
      
#letters letters letters  letters  letters  letters 

from itertools import count


countries = ['FR','US','DE','RU']
print(countries)
countries[1]='GB'

countries.append('PL') # komenda dodaje do listy PL
countries.insert(2,'ES') # 2 oznacza na której pozycji ma się znaleźć w liście,'ES' to konkretna informacja
countries.remove('RU') #usuwa 'RU' z listy
countries.sort() # sortuje liste alfabetycznie
countries.reverse() # odwraca w liście wszystkie informacje
print(countries.pop(2))# funkcja ta zwroci wartosc 2 i usunie z listy
print(countries.index('PL')) # funkcja poda informacje na którym miejscu listy znajdzie się 'PL'
print(countries.count('DE')) # funkcja poda informacje ile razy w liscie znajduje sie 'DE'


newList = 'FI', 'SE'
countries.extend(newList) # dodaje wartosci z newList do aktualnej listy - countries

print(countries)

countriesCopy = countries


#exrcise
hitsTitles = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE'] #1
hitsTitles.append('CHILD IN TIME')               #2
hitsTitles.append('AGAIN')                       #2

hitsTitles.insert(3,'HOTEL CALIFORNIA')          #3   

hitsTitles.insert (0,'THE SOUND OF SILENCE')     #4   

print(hitsTitles.index('HOTEL CALIFORNIA'))      #5

hitsTitles.remove('HOTEL CALIFORNIA')            #6

hitsTitles[0]='ENJOY THE SILENCE'                #7
print(hitsTitles)                                #7     

hitsToRead = hitsTitles.copy()                   #8                                         

hitsToRead.reverse()                             #9

hitsToRead.sort                                  #10

hitsTitles.pop(0)                                #11
hitsTitles.pop(0)                                #11

additionalSongs = ['NOTHING COMPARES 2 U','WISH YOU WERE HERE'] #12

hitsToRead.extend(additionalSongs)               #13
print(hitsToRead)                                #13       

hitsToRead.count('WISH YOU WERE HERE')           #14
hitsToRead.count('RIDERS ON THE STORM')          #14


hitsToRead.clear()                               #15
print(hitsToRead)                                #15                                          












