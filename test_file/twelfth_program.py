#for for for for for for for
#exercise



#1
fibonacciIterations = 20
a1 = 0
a2 = 1
a3 = 0
for i in range(0,20):
    print('Step',i,'value',a3)
    a1=a2 # 0 = 1
    a2=a3 # 1 = 0
    a3=a1+a2 # 0 = 0 + 1
    
#2
text = """ 
Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t.   
"""
listOfWords = text.replace('\n',' ').split(' ')
for word in listOfWords:
    if word.lower().find('p') >=0:
        print (word)


