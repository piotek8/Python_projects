import random 

choices =  {'paper' : '1','scissors' : '2','stone' : '3'}

computer = random.choice(list(choices.values()))

print('''If you want to:
- play with the computer, type 'computer'
- play with someone, type 'someone'
- exit the game, type 'exit'
                  ''')
        
def start_program():    
    while True:        
        select_option = input("Write your choice: ")

        if select_option == 'computer':
            print('Playing with the computer')
            game_computer()
        elif select_option == 'someone':     
            print('Playing with someone')
            game_someone()
        elif select_option == 'exit':    
            print('Exiting the game')
            break
        else:
            print('Wrong answer. Write correct informations')

        print('')
        
def game_computer():
    while True: 
        #computer = random.choice(list(choices.values()))
        choice =input(str("Set options: paper = 1, scissors = 2, stone = 3 : "))
        if choice == computer :
            print('draw')
        elif choice == '1'and computer == '2':  
            print('you lose game') 
        elif choice == '1'and computer == '3':  
            print('you win game')             
        elif choice == '2'and computer == '3':  
            print('you lose game') 
        elif choice == '2'and computer == '1':  
            print('you win game')       
        elif choice == '3'and computer == '1':  
            print('you lose game') 
        elif choice == '3'and computer == '2':  
            print('you win game')       
        elif choice =='scissors' and computer == 'paper':
            print('you win game')
        elif choice =='exit':
            print('exit game') 
            break           
        else:
            print('Wrong answer. Write correct informations')
        
        
def game_someone():    
    while True:            
        Player_1 = input(str("Player 1 - Set( paper, scissors, stone): "))
        Player_2 = input(str("Player 2 - Set( paper, scissors, stone): "))    
        if Player_1 == 'exit' or Player_2 == 'exit' or (Player_1 == 'exit' and Player_2 == 'exit'):    
            print('exit game') 
            break
        elif Player_1 == Player_2 :
            print('draw')
        elif Player_1 == '1' and Player_2 == '2':  
            print('you lose game') 
        elif Player_1 == '1' and Player_2 == '3':  
            print('you win game')             
        elif Player_1 == '2' and Player_2 == '3':  
            print('you lose game') 
        elif Player_1 == '2' and Player_2 == '1':  
            print('you win game')       
        elif Player_1 == '3' and Player_2 == '1':  
            print('you lose game') 
        elif Player_1 == '3' and Player_2 == '2':  
            print('you win game')      
        else:
            print('Wrong answer. Write correct informations')

