
# print print print print  print print  print print  

pi = 3.14
r = 10
print(pi,r)
print(pi,r**2)

print(pi,r, sep= "\n") # oddziela dane - każda dana w innym wierszu
print(pi,r, sep= "\t") # odziela dane w wieszu za pomocą spacji
print(pi,r, sep= "\a") # wydaje dźwięk 

print ("\u03A3") # wyświetla znak sigma
print ("\\") # wyświetla znak backslash


print ('TVP1',';','TVP2',';','TVN',';','Polsat',';','BBC',';','HBO',';','MTV')
print ('I like computers but better is TVP1 but better is TVP2 but better is TVN but better is Polsat but better is BBC but better is HBO but better is MTV ')


ProgramName = "BBC"
Item = "News" 
Time = '18:00'

print('I am watching ', Item, ' at ', Time, ' on ', ProgramName,'.', sep= '')


# string string string string string string string 

atext = 'This is a text.'
print(atext.endswith('ext'))
print(atext.islower())
print(atext.upper())
print(atext.upper().isupper()) 
print(atext.upper().isupper())
print(atext.find ('is'))
print(atext.find ('is',3))
print(atext.replace ('a','4'))
print(atext.replace ('a','4').replace('i','l').replace('e','3'))
print(atext.split(' '))

somethingLikeNumber = '1000'
somethingLikeNumber.isdigit() #Funkcja sprawdza czy wyglada tekst jak liczba
somethingLikeNumber.isdecimal() #Funkcja sprawdza czy wyglada jak liczba z przecinkiem(np. 1.00 ; 1.25)
somethingLikeNumber.isalpha() #Funkcja sprawdza czy w tekscie sa literki
somethingLikeNumber.isalnum() #Funkcja sprawdza czy tekst sklada sie z samych literek, cyferek


#exercise

quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'
print(quote.upper()) #2
print(quote.lower()) #3
print(quote.endswith('street')) #4
print(quote.isupper()) #5
print(quote.upper().isupper()) #6
print(quote.find('one')) #7
print(quote.replace('one','f')) #8
print(quote.replace('one','1').replace('both','2')) #9
print(quote.split(' ')) #10

print(quote.isdigit())   #11
print(quote.isdecimal()) #11
print(quote.isalpha())   #11
print(quote.isalnum())   #11


###

drive = 'C:\\'
folder = 'scripts\\python\\'
file = 'myscript.py'
path = drive + folder + file
print (path)

justText =('text with\nnewline')  #\n przenosi informacje do wiersza ponizej
print (justText)

justText2= 'McDonald\'s'
print('justText2')

#exercise2
#Kasia Sowa - Mrugała    

firstName = 'Kasia'                 #1
familyName = 'Sowa'
lastName = 'Mrugała'

newName = firstName+ " "+ familyName+ " " + lastName 
print (newName)
                                    #2
music = (' "Universal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner "I\'m a Man" Steve Winwood ')
print(music)         

                                    #3
music = '"Universal Fanfare" Jerry Goldsmith\n"Happy Together" Garry Bonner\n"I\'m a Man" Steve Winwood\a'
print(music) 


print ("(\(\\")                     #4
print ('( -.-)')
print ('O_(")(")')



somethingLikeNumber = '1000' #nie jest to liczba
print(somethingLikeNumber) #1000
print(int(somethingLikeNumber)+1) #1001
print(somethingLikeNumber+str(1)) #10001
type(somethingLikeNumber)         #class 'str'
type(int(somethingLikeNumber)+1)  #class 'int'


#exercise3
                        #1,2
article = '''Monty Python (also collectively known as the Pythons) 
were a British surreal comedy troupe who created the sketch comedy television show Monty Python\'s Flying Circus, 
which first aired on the BBC in 1969. Forty-five episodes were made over four series.'
'''

print(article.upper())  #3
print(article.lower().replace ('monty', 'flying')) #4
print(article.split(' ')) #5
print('word python appears',article.lower().count('python'),'times') #6 liczba 3 -ilość wystąpień tekstu python w zmiennej article
print('to print the \ you need to put \ twice in your text like this: \\') #7
print('The best hits of \'80s!!!') #8
print("The best hits of '80s!!!")  #8

amountPLN = 234

print('cur','\texchange','amount')              #9
print('USD','\t',3.65,'\t',amountPLN/ 3.65)     #9
print('EUR','\t',4.23,'\t',amountPLN/ 4.23)     #9

ValueAsText = '123.45'
factor = 1.23
print('value is',ValueAsText, 'factor is',factor,'value*factor= ',float(ValueAsText) * factor)



