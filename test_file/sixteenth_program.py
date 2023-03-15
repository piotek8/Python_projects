#random random random random
#lotto_program
import numbers
import random
from turtle import position, width

my_Numbers = [] # lista

while len(my_Numbers) <7:
    new_Number = random.randint(1,49)
    if new_Number in my_Numbers:
        print ('Eliminated:', new_Number)
        continue
    my_Numbers.append(new_Number)
    
print ('Those numbers will win:', my_Numbers)    

#exercise
#1
colors = ['Hearts','Diamonds','Clubs','Spades']

figures = ['Ace','King','Queen','Jack','10','9']

#2
allCards = []

#3
for c in colors:
    for f in figures:
        allCards.append("%s - %s" % (c, f))

#4
print(allCards)

#5
import random

#6
random.shuffle(allCards)
print(allCards)

#7
player1 = []
player2 = []

#8

max = len(allCards)

for i in range(max):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])
 
print('-------PLAYER 1--------')
print(player1)
 
print('-------PLAYER 2--------')
print(player2)              
 
player1 = allCards[:12]
player2 = allCards[12:]
 
 
print('-------PLAYER 1--------')
print(player1)
 
print('-------PLAYER 2--------')
print(player2)    



#Pascal's_triangle Pascal's_triangle Pascal's_triangle Pascal's_triangle

numbers = [1]
 
print (numbers)
for i in range(5):
    newNumbers = [1]
    position = 0
    while position < len(numbers) -1:
        newNumbers.append(numbers[position] + numbers[position+1])
        position +=1
    newNumbers.append(1)
    numbers = newNumbers.copy()
    print(numbers)        
    
#exercise

aCard = {"Figure":"King", "Power":12}
print(aCard)
print(aCard['Figure'])
print(aCard['Power'])
    
    
    
colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]


#1    
allCards = []

for c in colors:
    for f in figures:
      aCard = f.copy()
      aCard['Color'] = c
      allCards.append(aCard)

#2      
import random
random.shuffle(allCards)
print(allCards)  

#3
player1 = allCards[:12]
player2 = allCards[12:]

#4
print (player1)
print (player2)   

#5    
while len(player1) > 0 and len(player2) > 0:

#6
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    
    if card1["Power"] == card2["Power"]:
        player1.append(card1)
        player2.append(card2)
        #print('=EQUAL \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('=EQUAL \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
    elif card1["Power"] > card2["Power"]:
        player1.append(card1)
        player1.append(card2)
        #print('PLAY-1 \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
    else:
        player2.append(card2)
        player2.append(card1)
        #print('PLAY-2 \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
 
if len(player1) > 0:
    print('PLAYER 1 WON!!!!')
else:
    ptint('PLAYER 2 WON!!!!')


#Pascal's_triangle2 Pascal's_triangle2 Pascal's_triangle2 Pascal's_triangle2

width = 60
height = 7
line = ''
for n in numbers:
    line += '%3d' % (n)
print(line.center(width))    

print (numbers)
for i in range(height-1): #poziomy trójkąta
    newNumbers = [1]
    position = 0
    while position < len(numbers) -1:
        newNumbers.append(numbers[position] + numbers[position+1])
        position +=1
    newNumbers.append(1)
    numbers = newNumbers.copy()
    print(numbers)   


    line = ''
    for n in numbers:
        line += '%3d' % (n)
    print(line.center(width))    

 
 
       
#exercise

colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]
 
allCards = []
for c in colors:
    for f in figures:
        aCard = f.copy()
        aCard['Color'] = c
        allCards.append(aCard)
 
import random
 
random.shuffle(allCards)
print(allCards)
 
player1 = []
player2 = []
 
player1 = allCards[:12]
player2 = allCards[12:]
 
 
print('-------PLAYER 1--------')
print(player1)
 
print('-------PLAYER 1--------')
print(player2)    
 
while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
 
    stock = []  
 
    if card1["Power"] == card2["Power"]:
        while card1["Power"] == card2["Power"]:

            print('WAR',card1['Power'],card2['Power'])
            stock.append(card1)
            stock.append(card2)
 
            if len(player1)<2:
                player2.extend(stock)    
                player2.extend(player1)
                player1 = []
                print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2)*'*')
                break
            elif len(player2)<2:
                player1.extend(stock)    
                player1.extend(player2)
                player2 = []
                print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
                break
            else:
                card1 = player1.pop(0)
                card2 = player2.pop(0)
                stock.append(card1)
                stock.append(card2)
                caod1 = player1.pop(0)
                card2 = player2.pop(0)
        else:
            if card1["Power"] > card2["Power"]:
                stack.append(card1)
                stack.append(card2)
                player1.extend(stack)
                print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
            else:
                stack.append(card1)
                stack.append(card2)
                player2.extend(stack)
                print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2)*'*')
            
 
    elif card1["Power"] > card2["Power"]:
        player1.append(card1)
        player1.append(card2)
        #print('PLAY-1 \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
    else:
        player2.append(card2)
        player2.append(card1)
        #print('PLAY-2 \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2)*'*')
 
if len(player1) > 0:
    print('PLAYER 1 WON!!!!')
else:
    print('PLAYER 2 WON!!!!')       
    
    



    