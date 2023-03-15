# logical types and operators
"""
IsWeekend = True
print('Is weekend =', IsWeekend)

Temperature = 25
print('Temperature =', Temperature)

ToDoList = 'Shopping,Gym'
print('ToDoList =',ToDoList)

IsHappy = IsWeekend and Temperature >= 20 and ToDoList == ''
print('IsHappy=',IsHappy)

IsHappy = IsWeekend and Temperature >= 20 and ToDoList == '' \
or not IsWeekend and Temperature < 20 and ToDoList !=''
print('IsHappy =',IsHappy)    

IsHappy = IsWeekend and Temperature >= 20 and ToDoList == '' \
or not IsWeekend and Temperature < 20 and ToDoList != ''
print ('IsHappy =',IsHappy)

#exercise

isAutomaticMode = True
is80PercentLight = False
isDirectLight = False
isRainy = False
# światła powinny się świecić

isAutomaticMode = True
is80PercentLight = True
isDirectLight = False
isRainy = True
# światła powinny się świecić

isAutomaticMode = True
is80PercentLight = True
isDirectLight = True
isRainy = False
# światła powinny się świecić

isAutomaticMode = True
is80PercentLight = False
isDirectLight = False
isRainy = True
# światła powinny się świecić

isAutomaticMode = False
is80PercentLight = True
isDirectLight = False
isRainy = True
# światła powinny się NIE świecić


# Kierowca ustawił pokrętło sterujące światłem na tryb automatyczny
isAutomaticMode = True

# To poziom światła dziennego powyżej 80%
is80PercentLight = True

# Czy słońce świeci bezpośrednio na twarz kierowcy
isDirectLight = False

# Czy jest deszcz, mgła lub inne warunki pogodowe
isRainy = False


turnLightsOn = isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy)

print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)



from ensurepip import version


Title = 'Python' #str
print('Title is', type(Title))

Version = 3 #int
print('Version is', type(Version))

Progress = 0.21 #float
print('Progress is', type(Progress))

print('This expression is', type(Progress * Version))
print('This expression is', type(Title * Version))
# print('This expression is', type(Progress * Title))

# tips&tricks tips&tricks tips&tricks tips&tricks
x=1
y=1
z=1
print(x,y,z)

a=b=c=2
print(a,b,c)

c=3 
print(a,b,c)


print(6/2*(1+2))

print(4**3**2)

x+=1
print(x)
"""
#exercise

v1 = 126                  #1 

v2 = '126'                #1 

v3 = 126.0                #1 

v4 = '126.0'              #1 

print(type(v1))           #2,3  int
print(type(v2))           #2,3  str   
print(type(v3))           #2,3  float
print(type(v4))           #2,3  str

print(v1+v3,type(v1+v3))  #4
print(v2+v4,type(v2+v4))  #4

print (7-1*0+3+3)         #5

print(4**5/2**3)          #6

print(99+9/9)             #7 

