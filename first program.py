
from datetime import date
print ("Today is",date.today().strftime("%A"))
print ("Have a nice day!")
input ("Press enter to continue")


text = "This is a text"
print (text)
anotherText = "this is a text"
print(text == anotherText)

#START - zadanie zadanie zadanie zadanie
#ilosc mrugniec okiem na minute
blinksPerMin = 20
#ilosc minut na godzine i ilosc godzin w dobie
minInHour = 60
hoursInDay = 16
daysInYear = 365
#ilosc lat
years = 50
#ilosc mrugniec w ciagu X lat
print(blinksPerMin*minInHour*hoursInDay*daysInYear*years)

#definitionOfVariables
daysOfWorkPermonth = 20
monthsInYear = 12
vacation = 26
yearsOfWOrk = 40
#result
print ((daysOfWorkPermonth * monthsInYear - vacation)*yearsOfWOrk)
#KONIEC - zadanie zadanie zadanie zadanie


print("Hello,what day is today?")
from datetime import date
print("Today is:")
print(date.today().strftime("%A"))
date.today

classroom = "English:104"
print (classroom.lower())



#W pole kola
WartoscPi = 3.14
PromienOkregu = 5
PoleKola = int(WartoscPi * PromienOkregu)
print("Pole kola wynosi" , PoleKola)

#W pole okregu
WartoscPi = 3.14
PromienOkregu = 5
ObwodOkregu = int(2 * WartoscPi * PromienOkregu)
print("Pole okregu wynosi" , ObwodOkregu)

# pole prostokata
dl_boku_a = 6
dl_boku_b = 8
Pprostokata = dl_boku_a * dl_boku_b
print("Pole trapezu wynosi" , Pprostokata)

# pole trapezu
dl_boku_a = 6
dl_boku_b = 8
wysokosc = 4
Ptrapezu = int(1/2 * (dl_boku_a + dl_boku_b) * wysokosc)
print ("Pole trapezu wynosi" , Ptrapezu)



 