# Used to import the webdriver from selenium
from selenium import webdriver 
import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import js2py
import ait

 
# Get the path of chromedriver which you have install


if __name__ == '__main__': 
    def startAutoLogin(login, password, url):
        path = "C:\\Users\\hp\\Downloads\\chromedriver"

        # giving the path of chromedriver to selenium webdriver
        driver = webdriver.Chrome(path)

        # opens the program in the maximum web window
        driver.maximize_window() # maximizing the browser windows 

        # opening the website  in chrome.
        driver.get(url)

        # find the id or name or class of
        # username by inspecting on username input
        driver.find_element('xpath',
                         '//*[@id="__next"]/div/div/div/div/main/div/div[2]/div/form/div[1]/div/div/input').send_keys(login)

        # find the password by inspecting on password input
        driver.find_element('xpath',
                             '//*[@id="__next"]/div/div/div/div/main/div/div[2]/div/form/div[2]/div/div/div/input').send_keys(password)


        # click on submit
        driver.find_element('xpath',
                             '//*[@id="__next"]/div/div/div/div/main/div/div[2]/div/form/button[2]/div').click()



# TRY TRY TRY TRY TRY TRY

        #open("C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/main",'a')
        #with open('C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/main', 'r+') as f:
        #f = open ('C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/main.js')
        # czyli otworz plik albo dodaj go do konsoli w np. chrome  u mnie driverr
        # plik lokalizuje, musi jakby go zaimportowac do konsoli, do przegladarki
        #f.readline()
        #f.close()
        
        
        #f = open ('C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/main.js')
        #zawartosc = f.read()
        #f.close()
        
        #js2py.run_file (f)
        #js2py.run_file('C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/jsmain')
#        with open("C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/main", 'a') as file:
#        file.write("if [CUID] = -1 then"
#            "function GetCUID() { return 0; }"
#        "else"
#            "function GetCUID() { return [CUID] });")

       # f = get ('C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/main.js')
       # driver.execute_script(f)

# TRY TRY TRY TRY TRY TRY

      
        pass
        driver.implicitly_wait(26) # or can use sleep(16)    
    

        driver.find_element('xpath',
                            '//*[@id="onetrust-accept-btn-handler"]').click() #accept cookies files   
        driver.find_element('xpath',
                           '//*[@id="postNewAdLink"]').click()  #press Add announcement option  
        pass
        driver.implicitly_wait(10)      
    

        
        driver.find_element('xpath', #set Title advertisement
                             '//*[@id="posting-form"]/main/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div/textarea').send_keys(Title)              
        
       #driver.find_element('xpath', #set Category advertisement
       #                     '//*[@id="posting-form"]/main/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div/textarea').click()      
       # I didn't set category because 

        def photos(): #creating a function that adds images to cells
            c1 = driver.find_element(By.CSS_SELECTOR, #set Photos jpg in cell 1
                                'body > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > main:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)')
            c1.send_keys(allPhotos)

           #c1.send_keys('C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/iPhone 12 mini zielony/1.jpeg \n C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/iPhone 12 mini zielony/2.jpeg \n C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/iPhone 12 mini zielony/3.jpeg \n C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/iPhone 12 mini zielony/4.jpeg ')  


           #c1 = driver.find_element(By.CSS_SELECTOR, #set Photos jpg in cell 1
           #                    'body > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > main:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)')
           #c1.send_keys(P1)

           #c2 = driver.find_element('xpath', #set Photos jpg in cell 2
           #                    '(//input[@id="photo-attachment-files"])[2]')
           #c2.send_keys(P2)  

           #c3 = driver.find_element(By.XPATH, #set Photos jpg in cell 3
           #                    '(//input[@id="photo-attachment-files"])[3]')
           #c3.send_keys(P3)    

           #c4 = driver.find_element('xpath', #set Photos jpg in cell 4
           #                    '/html[1]/body[1]/div[1]/div[1]/form[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/input[1]')
           #c4.send_keys(P4)
            
           #c5 = driver.find_element(By.CSS_SELECTOR, #set Photos jpg in cell 5
           #                    'body > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > main:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > input:nth-child(2)')
           #c5.send_keys(P5)     
           #c6 = driver.find_element(By.XPATH, #set Photos jpg in cell 6
           #                    '(//input[@id="photo-attachment-files"])[6]')
           #c6.send_keys(P6)
           
           #c7 = driver.find_element(By.XPATH, #set Photos jpg in cell 7
           #                    '(//input[@id="photo-attachment-files"])[7]')
           #c7.send_keys(P7)                 
           #c8 = driver.find_element(By.XPATH, #set Photos jpg in cell 8
           #                    '(//input[@id="photo-attachment-files"])[8]')
           #c8.send_keys(P8)
                    
       # SOLVED PROBLEM - WHEN I TRY TO ADD FIFTH PHOTO UNFORTUNATELY MY PROGRAM UPLOAD DUPLICATE: FIRST PHOTO AND THIS ONE WHICH I PICKED 
        photos()


        driver.find_element('xpath', #set Description advertisement
                             '//*[@id="posting-form"]/main/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/textarea').send_keys(Description)        

        driver.find_element('xpath', #set Price advertisement
                             '//*[@id="parameters.price.price"]').send_keys(Price)        

        #print('Is negotiable ? (write yes or no)')
        yes = driver.find_element('xpath',      #set negotiable option
                             '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[1]/div/div[1]/div/div/div/div[3]/span')
        if Negotiable == 'yes':  # In this function, if the price is negotiable, 
            yes.click()          #              press the button
        else:       
            pass                 #             if not, go further
           
        driver.implicitly_wait(0.1)
        

        driver.find_element(By.CLASS_NAME,'css-e010pl').click()  # press the select button
        driver.implicitly_wait(0.5)
     

        Uzy = driver.find_element('xpath',
                                  '(//a[contains(text(),"Używane")])[1]')     # set state: Używane         
        Now = driver.find_element('xpath',
                                  '//a[normalize-space()="Nowe"]')            # set state: Nowe  
        Usz = driver.find_element('xpath',
                                  '(//a[normalize-space()="Uszkodzone"])[1]') # set state: Uszkodzone
        
        
        # in this function, depending on the value of the State variable,
        #           enters the data from the commands above,
        #   if write something other you can see information ERROR
        if State == 'uzywane' or State == 'używane' or State == 'used' :        # | can be like or
            Uzy.click()                          
        elif State == 'nowe' or State == 'new':  
            Now.click()
        elif State == 'uszkodzone' or State == 'broken':
            Usz.click()
        else:
            print('APPLICATION ERROR. You need to set the status of the announcement')             


        driver.find_element(By.CLASS_NAME,'css-6z56jw').click()  # press the select button
        driver.implicitly_wait(0.5)     

        iPhone_14 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/div')               
        iPhone_14_Plus = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[2]/div/div/div/a')
        iPhone_14_Pro = driver.find_element('xpath','//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[3]/div/div/div/a')
        iPhone_14_Pro_Max = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[4]/div/div/div/a')
        iPhone_13 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[5]/div/div/div/a')
        iPhone_13_mini = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[6]/div/div/div/a')
        iPhone_13_Pro = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[7]/div/div/div/a')
        iPhone_13_Pro_Max = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[8]/div/div/div/a')
        iPhone_12 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[9]/div/div/div/a')
        iPhone_12_mini = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[10]/div/div/div/a')
        iPhone_12_Pro = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[11]/div/div/div/a')
        iPhone_12_Pro_Max = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[12]/div/div/div/a')
        iPhone_11 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[13]/div/div/div/a')
        iPhone_11_Pro = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[14]/div/div/div/a')
        iPhone_11_Pro_Max = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[15]/div/div/div/a')
        iPhone_SE = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[16]/div/div/div/a')
        iPhone_X = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[17]/div/div/div/a')
        iPhone_XS = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[18]/div/div/div/a')
        iPhone_XS_Max = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[19]/div/div/div/a')
        iPhone_XR = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[20]/div/div/div/a')
        iPhone_8 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[21]/div/div/div/a')
        iPhone_8_Plus = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[22]/div/div/div/a')
        iPhone_7 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[23]/div/div/div/a')
        iPhone_7_Plus = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[24]/div/div/div/a')
        iPhone_6 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[25]/div/div/div/a')
        iPhone_6_Plus = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[26]/div/div/div/a')
        iPhone_6S = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[27]/div/div/div/a')
        iPhone_6S_Plus = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[28]/div/div/div/a')
        iPhone_5 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[29]/div/div/div/a')
        iPhone_5C = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[30]/div/div/div/a')
        iPhone_5S = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[31]/div/div/div/a')
        iPhone_4  = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[32]/div/div/div/a')
        iPhone_3  = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[33]/div/div/div/a')
        iPhone_3G  = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[34]/div/div/div/a')
        iPhone_3GS  = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[35]/div/div/div/a')
        iPhone_1gen = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[36]/div/div/div/a')
        Inne_modele = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[37]/div/div/div/a')

        match Phone_Model:

            case 'iPhone 14':
                iPhone_14.click()

            case 'iPhone 14 Plus':
                iPhone_14_Plus.click()

            case 'iPhone 14 Pro':           
                iPhone_14_Pro.click()

            case 'iPhone 14 Pro Max':        
                iPhone_14_Pro_Max.click() 

            case 'iPhone 13':               
                iPhone_13.click()

            case 'iPhone 13 mini':
                iPhone_13_mini.click()     

            case 'iPhone 13 Pro':        
                iPhone_13_Pro.click()

            case 'iPhone 13 Pro Max':        
                iPhone_13_Pro_Max.click()

            case 'iPhone 12':           
                iPhone_12.click()

            case 'iPhone 12 mini':        
                iPhone_12_mini.click()

            case 'iPhone 12 Pro':        
                iPhone_12_Pro.click()

            case 'iPhone 12 Pro Max':        
                iPhone_12_Pro_Max.click()

            case 'iPhone 11':             
                iPhone_11.click()

            case 'iPhone 11 Pro':        
                iPhone_11_Pro.click()   

            case 'iPhone 11 Pro Max':        
                iPhone_11_Pro_Max.click()

            case 'iPhone SE':        
                iPhone_SE.click()     

            case 'iPhone X':        
                iPhone_X.click()

            case 'iPhone XS':        
                iPhone_XS.click()

            case 'iPhone XS Max':             
                iPhone_XS_Max.click()

            case 'iPhone XR':        
                iPhone_XR.click()     

            case 'iPhone 8':        
                iPhone_8.click()

            case 'iPhone 8 Plus':        
                iPhone_8_Plus.click() 

            case 'iPhone 7':            
                iPhone_7.click()

            case 'iPhone 7 Plus':         
                iPhone_7_Plus.click()     

            case 'iPhone 6':         
                iPhone_6.click()

            case'iPhone 6 Plus':         
                iPhone_6_Plus.click()     

            case 'iPhone 6S':         
                iPhone_6S.click()

            case 'iPhone 6S Plus':         
                iPhone_6S_Plus.click()     

            case 'iPhone 5':         
                iPhone_5.click()

            case 'iPhone 5C':         
                iPhone_5C.click()     

            case 'iPhone 5S':         
                iPhone_5S.click()

            case 'iPhone 4':         
                iPhone_4.click()     

            case 'iPhone 3':         
                iPhone_3.click()

            case 'iPhone 3G':         
                iPhone_3G.click()

            case 'iPhone 3GS':         
                iPhone_3GS.click()

            case 'iPhone 1':         
                iPhone_1gen.click()

            case 'Inne modele':         
                Inne_modele.click()



        y = driver.find_element('xpath',        #set auto extension option
                             '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[3]/div/div[1]/div/div/div/label/span')
        if Auto_Extension == 'yes': # In this function, if you need auto extension for 30 days,
            y.click()               #              press the button
        else:                       
            pass                    #             if not, go further
        
        
        #This function is designed to search at the beginning, depending on the entered field of the parcel - (S, M, L, XL), 
        #                      and additionally, which is different (inPost, Orlen, Poczta Polska)           
        def PackageSizes():                   
            if Size == 'S' :
                S = driver.find_element('xpath','(//*[name()="svg"][@class="css-pyu9k9"])[1]')
                S.click()
                driver.implicitly_wait(1.5)
            else:
                pass        
            if Option == 'S_Orlen':
                S_Orlen = driver.find_element('xpath','//div[@data-testid="S-RUCH-false"]')
                S_Orlen.click()
            elif Option == 'S_inPost':
                S_inPost = driver.find_element('xpath','(//div[@data-testid="S-INPOST-false"])[1]')
                S_inPost.click()
            elif Option == 'S_PocztaPolska':
                S_PocztaPolska = driver.find_element('xpath','//div[@data-testid="S-POCZTA-false"]')
                S_PocztaPolska.click()    
            else:
                pass   
            
        
            if Size == 'M' :
                M = driver.find_element('xpath','(//*[name()="svg"][@class="css-pyu9k9"])[2]')
                M.click()
                driver.implicitly_wait(1.5)
            else:
                pass
            if Option == 'M_Orlen':
                M_Orlen = driver.find_element('xpath','(//div[@data-testid="M-RUCH-false"])[1]')   
                M_Orlen.click()
            elif Option == 'M_inPost':
                M_inPost =  driver.find_element('xpath','(//div[@data-testid="M-INPOST-false"])[1]')
                M_inPost.click()
            elif Option == 'M_PocztaPolska':
                M_PocztaPolska = driver.find_element('xpath','(//div[@data-testid="M-POCZTA-false"])[1]')
                M_PocztaPolska.click()    
            else:
                pass
            
        
            if Size == 'L' :
                L = driver.find_element('xpath','(//*[name()="svg"][@class="css-pyu9k9"])[3]')
                L.click()  
                driver.implicitly_wait(1.5)
            else:
                pass
            if Option == 'L_Orlen':
                L_Orlen = driver.find_element('xpath','(//div[@data-testid="L-RUCH-false"])[1]')   
                L_Orlen.click()
            elif Option == 'L_inPost':
                L_inPost = driver.find_element('xpath','(//div[@data-testid="L-INPOST-false"])[1]')
                L_inPost.click()
            elif Option == 'L_PocztaPolska':
                L_PocztaPolska = driver.find_element('xpath','(//div[@data-testid="L-POCZTA-false"])[1]')
                L_PocztaPolska.click()    
            else:
                pass
        
        
            if Size == 'XL' :
                XL = driver.find_element('xpath','(//*[name()="svg"][@class="css-pyu9k9"])[4]') 
                XL.click()
                driver.implicitly_wait(1.5)
            else:
                pass
            if Option == 'XL_PocztaPolska':
                XL_PocztaPolska = driver.find_element('xpath','(//div[@data-testid="XL-POCZTA-false"])[1]')
                XL_PocztaPolska.click()    
            else:
                pass                    
            
        driver.implicitly_wait(1.5)          
         

        D = driver.find_element(By.CSS_SELECTOR,   # this option find OLX button 
                             '.switch__toggle.css-2tc5k6')
        if Delivery == 'no':     # In this function, if you don't need delivery ,                  
            D.click()            #              press the button                     
            pass
        else:
            PackageSizes()       #             if yes, go to packageSizes function      
                
        Location_clear = driver.find_element(By.NAME,'city_id')
        Location_clear.send_keys(Keys.CONTROL, 'a') # this option remove the old text
        Location_clear.send_keys(Keys.BACKSPACE)    #      (written in column)
        Location_clear.send_keys(Location)          #   set Location advertisement
                            
     
        Phone_clear = driver.find_element('xpath','//*[@id="phone"]') 
        Phone_clear.send_keys(Keys.CONTROL, 'a') # this option remove the old text 
        Phone_clear.send_keys(Keys.BACKSPACE)    #      (written in column)
        Phone_clear.send_keys(Phone_Number)      #    set Number advertisement

        driver.find_element(By.CLASS_NAME,'css-1anknvg').click()  # press the select button        
        driver.implicitly_wait(5) 


        driver.find_element(By.CLASS_NAME,'css-18l8bp6').click()  # press the select button        
        driver.implicitly_wait(5) 
        driver.find_element('xpath', '//*[@id="root"]/div/main/div/div/div[2]/div[1]/a[2]/span/span').click()
   
    
    #    
    #    driver.find_element('xpath', # press the buttom - "Podgląd ogłoszenia"
    #                         '//*[@id="posting-form"]/main/div[1]/div[7]/div/button[1]/span/span').click()  
       
        sleep(4294967) 

                


#    D  E  S  C  R  I  P  T  O  N
 
    # Driver Code
    # Enter below your login credentials
    username = ""
    password = ""
        
    # Data in the advertisement  
    Title = 'Apple iPhone 12 mini 91 % kondycja baterii ładowarka kabel lightning' #must be less than 70 characters
    Description = ''' Sprzedam telefon marki Apple iPhone 12 mini w zielonym kolorze. 
    Wszystko sprawne - bez pęknięć czy uszczerbień.
    Kondycja baterii wynosi 91%.
    Funkcje w 100% działają - Face ID, jak i inne opcje.
    Jest on wylogowany z iCloud'a, przygotowany do użytkowania.
     
    W zestawie znajduje się z :
    - iPhone 12 mini 
    - pudełko
    - ładowarka
    - przewód Lightning
    - kluczyk karty SIM
    - etui '''    
    #                       must be more than 80 characters and less than 9000 characters
   
    Price = '1900' # set price
    Location = 'Warszawa' # set location
    Phone_Number = '500400300' # set phone number
    Negotiable = 'yes'  # write 'yes' when the price is negotiable , if not write 'no'
    State = 'new'   # Set which state you want.You can use polish or english langugage : ( used / new / broken ) or (Używane / Nowe / Uszkodzone)
    Phone_Model = 'iPhone 12 mini'                       # write iPhone model:  
    #                                (looks like this: 'iPhone, space buttom, which model) 
    #                                (for example: iPhone 14 Pro   or  iPhone 14 Pro Max)
    Auto_Extension = 'yes'  # write 'yes' if you want auto extension suddenly every 30 days, if not write 'no'
    Delivery =  'yes' #write 'yes' when you want delivery , if not write 'no'
    Size = 'S'  # write package size 'S or M or L or XL' size
    Option = 'S_inPost'  # write option of package size for example (S_Orlen, L_inPost, M_PocztaPolska) 
    #                                 (looks like this: 'what size , _ , which courier')
    #                                           (for example: 'L_inPost') 

 
   #Używane = driver.find_element(By.CLASS_NAME,'css-1n05x61')
   #Nowe = driver.find_element(By.CLASS_NAME,'css-lihuun')
   #Uszkodzone = driver.find_element(By.CLASS_NAME,'css-lihuun')
#       state = 
    #options
    
    # The photos to load #C:\Users\Piotr\Desktop\kurs\py coursera google crash\OLX_Bot\Photos
    P1 = 'C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/iPhone 12 mini zielony/1.jpeg' 
    P2 = 'C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/iPhone 12 mini zielony/2.jpeg'
    P3 = 'C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/iPhone 12 mini zielony/3.jpeg'
    P4 = 'C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/iPhone 12 mini zielony/4.jpeg'
    P5 = 'C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/iPhone 12 mini zielony/5.jpeg'
    P6 = 'C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/iPhone 12 mini zielony/6.jpeg'
    #P7 = 'C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/iPhone 12 mini zielony/7.jpeg'
    #P8 = 'C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/iPhone 12 mini zielony/8.jpeg'
    allPhotos = P1 + " \n " + P2 + " \n " + P3 + " \n " + P4 + " \n " + P5 + " \n " + P6    
    # URL of the login page of site
    # which you want to automate login.
    url = 'https://pl.login.olx.com/?client_id=b0lcnbsn82kvrtk767nn8pg1k&code_challenge=Ze_PviRH2j_CfriWXlcfaEmhtVm_7eTXiwm81ukc1lc&code_challenge_method=S256&redirect_uri=https%3A%2F%2Fwww.olx.pl%2Fkonto%2Fcallback%2F&st=eyJzbCI6IjE4NWZhY2FmMTljeDVhYTMxOWY3IiwicyI6IjE4NjMzMmZlYmUxeDNjYTMxZDE1IiwiY2MiOjF9&state=eyJyZWZlcnJlciI6Imh0dHBzOlwvXC93d3cub2x4LnBsXC9tb2pvbHhcLyJ9'
    
    # Call the function
    startAutoLogin(username, password, url)

    
