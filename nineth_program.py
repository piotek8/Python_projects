
"""#if_in_while if_in_while if_in_while if_in_while if_in_while 
values = [10,43,12,48,12,11,18,98,57,28,19,27,49,19,74]    
i = 0
max = len(values) 

while i<max:
    print(i,values[i])
    i+=1
 


values = [10,43,12,48,12,11,18,98,57,28,19,27,49,19,74]    
i = 0
max = len(values) -2 # -2 poniewaz chcemy wyciagnac 3 liczby z rzedu, a moze zatrzymac na 3 od konca max

while i<max:
    print(i,values[i],values[i+1],values[i+2])
    i+=1
    if values[i]<values[i+1] and values[i+1]<values[i+2]:
        print('\tFound:', values[i],values[i+1],values[i+2])   
        
#exercise

#1        
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

i = 0
max = len(numbers)-1

while i< max:
    print(i, numbers[i],numbers[i+1])
    if numbers[i]**2 == numbers[i+1]:
        print("\tFOUND!")
    i+=1

#2
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

i = 0
max = len(numbers)-2

while i< max:
    print(i, numbers[i],numbers[i+1], numbers[i+2])
    if numbers[i]**2 == numbers[i+1] and numbers[i+1]**2 == numbers[i+2]:
        print("\tFOUND!")
    i+=1

#3
texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

i = 0
max = len(texts)-1

while i< max:
    print(i, texts[i],texts[i+1])
    if len(texts[i]) == len(texts[i+1]):
        print("\tFOUND!")
    i+=1 
     


#while while while while while while while while 

cargo = [40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]
cargo.sort()
cargo.reverse()
print('The cargo list is:',cargo)

boxCapacity = 90
box = []
i = 0

while i<len(cargo) and (boxCapacity)-sum(box) >= min(cargo):
    if (boxCapacity - sum(box)) >= cargo[i]:
        box.append(cargo[i])
    i+=1
    
    
print('The collected items sum is:', sum(box))
print('The elements are:',box)


#exercise

#1
number = 1
previous_Number = 0
max_Number = 50

while number <= max_Number:
    print(previous_Number + number)
    previous_Number = number
    number += 1



#2
import random
my_number = random.randint(0,20)
guess = -1

print('Guess my number')

while guess != my_number:
    guess = int(input())

    if guess == my_number:
        print('Congratulations')
    elif guess > my_number:
        print('Sorry- my number is smaller than your', guess, 'Try again!')
    else:
        print('Sorry- my number is greater than your', guess, 'Try again')
"""
#3
import random
my_number = random.randint(0,20)
guess = -1
trials = 0 
print('Guess my number')

while guess != my_number:
   
    guess = int(input())
    trials += 1
    
    if guess == my_number:
        print('Congratulations! You guessed the number for', trials, 'trials')
    elif guess > my_number:
        print('Sorry- my number is smaller than your', guess, 'Try again!')
    else:
        print('Sorry- my number is greater than your', guess, 'Try again')
        