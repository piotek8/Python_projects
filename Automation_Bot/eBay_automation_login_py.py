# Used to import the webdriver from selenium
from selenium import webdriver 
import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import js2py
# driver.maximize_window() # maximizing the browser windows 
 
# Get the path of chromedriver which you have install


if __name__ == '__main__': 
    def startAutoLogin(login, password, url):
        path = "C:\\Users\\hp\\Downloads\\chromedriver"

        # giving the path of chromedriver to selenium webdriver
        driver = webdriver.Chrome(path)

        # opens the program in the maximum web window
        #driver.maximize_window()

        # opening the website  in chrome.
        driver.get(url)

        # find the id or name or class of
        # username by inspecting on username input
        driver.implicitly_wait(25) 
        
        driver.find_element('xpath',#e-mail
                         '(//input[@id="userid"])[1]').send_keys(login)
         
        driver.find_element('xpath', #e-mail buttom
                         "//button[@id='signin-continue-btn']").click()
                
        driver.implicitly_wait(25) 
        
        # find the password by inspecting on password input
        driver.find_element('xpath',#password
                             "//input[@id='pass']").send_keys(password)
       
        driver.implicitly_wait(5) 
       
        driver.find_element('xpath',#password buttom
                             "//button[@id='sgnBt']").click()      


        
        driver.implicitly_wait(5)  # or can use sleep(16)    
    

        driver.find_element(By.CSS_SELECTOR,
                            ".gh-p").click() # sprzedaj buttom 
      
        driver.implicitly_wait(2.5)
        driver.find_element(By.CSS_SELECTOR,
                           "div[class='image-banner-card white-background'] a[class='textual-display image-banner-card__action fake-btn fake-btn--fluid fake-btn--primary']").click() # wystaw przedmiot buttom 
        
        driver.implicitly_wait(2.5)   
    
        driver.find_element(By.CSS_SELECTOR,
                           "body > div:nth-child(2) > div:nth-child(2) > main:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)").send_keys(Title) # Title ustaw
  
        
        driver.find_element('xpath', # Title find buttom
                             "/html[1]/body[1]/div[2]/div[2]/main[1]/div[1]/div[1]/div[1]/button[1]").click()             
        
        driver.implicitly_wait(2.5)
                
       # MUST HAVE  
       
        driver.find_element(By.CSS_SELECTOR, #set (Telefony i Akcesoria) in category
                             "button[name='15032'] span[class='se-field-card__container']").click()            


        driver.find_element(By.CSS_SELECTOR, #set Title advertisement
                             "button[name='9355'] span[class='se-field-card__content-value']").click()  

        driver.implicitly_wait(5)

        driver.find_element(By.CSS_SELECTOR, #set Title advertisement
                             "button[class='textual-display btn btn--secondary prelist-radix__next-action']").click()          
        
        

        def category(): 
            Now = driver.find_element('xpath',
                                       "//input[@id='s0-1-1-24-10-@prelist-radix-body-0-1-1-0-14-5-2-6-condition-1000']")      # set state: Nowy 
            NowInny = driver.find_element('xpath',
                                       "//input[@id='s0-1-1-24-10-@prelist-radix-body-0-1-1-0-14-5-2-6-condition-1500']")      # set state: Nowy: inny             
            Uzy = driver.find_element('xpath',
                                       "//input[@id='s0-1-1-24-10-@prelist-radix-body-0-1-1-0-14-5-2-6-condition-3000']")      # set state: Używany                 
            Usz = driver.find_element('xpath',
                                       "(//input[@id='s0-1-1-24-10-@prelist-radix-body-0-1-1-0-14-5-2-6-condition-7000'])[1]") # set state: Na części lub nie działa


            if State == 'nowy' or State == 'new':       # | can be like or
                Now.click()                           
            elif State == 'nowy: inny' or State == 'new: other':
                NowInny.click() 
            elif State == 'uzywany' or State == 'używany' or State == 'used' :   
                Uzy.click()                        
            elif State == 'Na części lub nie działa' or State == 'broken':
                Usz.click()                
            else:
                print('APPLICATION ERROR. You need to set the status of the announcement')             
        category()
        

#        def category(): 
#            Now = driver.find_element('xpath',
#                                       "//input[@id='s0-1-1-24-10-@prelist-radix-body-0-1-1-0-14-5-2-6-condition-1000']")      # set state: Nowy 
#            NowInny = driver.find_element('xpath',
#                                       "//input[@id='s0-1-1-24-10-@prelist-radix-body-0-1-1-0-14-5-2-6-condition-1500']")      # set state: Nowy: inny             
#            Uzy = driver.find_element('xpath',
#                                       "//input[@id='s0-1-1-24-10-@prelist-radix-body-0-1-1-0-14-5-2-6-condition-3000']")      # set state: Używany                 
#            Usz = driver.find_element('xpath',
#                                       "(//input[@id='s0-1-1-24-10-@prelist-radix-body-0-1-1-0-14-5-2-6-condition-7000'])[1]") # set state: Na części lub nie działa
#
#
#            State= ''
#            
#            actions = { 'nowy' or 'new': Now.click(), 'nowy: inny' or 'new: other' : NowInny.click(),  'uzywany' or 'używany' or 'used': Uzy.click(), 'Na części lub nie działa' or 'broken' : Usz.click()  }           
#            action = actions.get(State, print('APPLICATION ERROR. You need to set the status of the announcement'))            
#            action(State)       
#        category()

        
        driver.find_element('xpath', # press the buttom 'Przejdź do wystawiania oferty'
                                 "(//button[@class='textual-display btn btn--primary condition-dialog-radix__continue-btn'])[1]").click()              
        driver.implicitly_wait(5)
        
        def Phone_mark():    
            driver.implicitly_wait(5)
            
            driver.find_element(By.ID, #press buttom mark
                                 "wc0-w0-LIST_PAGE_WRAPPER__-OCS_DESCRIBE_SECTION__-ATTRIBUTES__-ATTRIBUTES_GH__-ATTRIBUTES_DIY_VIEW__-REQUIRED_GROUP__-REQUIRED_ATTRIBUTE_GRID__-requiredAttrList.1__-valueSelect-inlineSelect").click()        
           
            driver.implicitly_wait(1)
           
            driver.find_element(By.CSS_SELECTOR, #set Apple mark 
                                 "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > span:nth-child(1)").click()        
        Phone_mark()
       
              
        #def Color_Phone():
        driver.implicitly_wait(5)
        
        driver.find_element(By.XPATH, # press the buttom 'Przejdź do wystawiania oferty'
                             "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[4]/div[2]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[3]/button[1]").click()                    
        
        if Color == 'beżowy' or Color == 'bezowy' or Color == 'beige':       # | can be like or
            driver.find_element('xpath',"//li[@data-value='Beżowy']").click()                           
        elif Color == 'biały' or Color == 'bialy' or Color == 'white': 
            driver.find_element('xpath',"//li[@data-value='Biały']").click()                  
        elif Color == 'brązowy' or Color == 'brazowy' or Color == 'brown': 
            driver.find_element('xpath',"//li[@data-value='Brązowy']").click() 
        elif Color == 'czarny' or Color == 'black': 
            driver.find_element('xpath',"//li[@data-value='Czarny']").click() 
        elif Color == 'czerwony' or Color == 'red': 
            driver.find_element('xpath',"//li[@data-value='Czerwony']").click() 
        elif Color == 'fioletowy' or Color == 'purpurowy' or Color == 'Violet' or Color == 'Magenta': 
            driver.find_element('xpath',"//li[@data-value='Fioletowy/purpurowy']").click() 
        elif Color == 'niebieski' or Color == 'blue': 
            driver.find_element('xpath',"//li[@data-value='Niebieski']").click()                
        elif Color == 'pomarańczowy' or Color == 'pomaranczowy' or Color == 'orange': 
            driver.find_element('xpath',"//li[@data-value='Pomarańczowy']").click()                
        elif Color == 'przezroczysty' or Color == 'transparent': 
            driver.find_element('xpath',"//li[@data-value='Przezroczysty']").click() 
        elif Color == 'różowy' or Color == 'rose': 
            driver.find_element('xpath',"//li[@data-value='Różowy']").click()                                
        elif Color == 'srebrny' or Color == 'silver': 
            driver.find_element('xpath',"//li[@data-value='Srebrny']").click()               
        elif Color == 'szary' or Color == 'gray': 
            driver.find_element('xpath',"//li[@data-value='Szary']").click()                    
        elif Color == 'wielokolorowy' or Color == 'multicolour': 
            driver.find_element('xpath',"//li[@data-value='Wielokolorowy']").click()                     
        elif Color == 'zielony' or Color == 'green': 
            driver.find_element('xpath',"//li[@data-value='Zielony']").click()
        elif Color == 'zloty' or Color == 'złoty' or Color == 'gold': 
            driver.find_element('xpath',"//li[@data-value='Złoty']").click()
        elif Color == 'zolty' or Color == 'żółty' or Color == 'yellow': 
            driver.find_element('xpath',"//li[@data-value='Żółty']").click()
        else:
            print('APPLICATION ERROR. You need to set the status of the announcement')                
        #Color_Phone()
         
        driver.implicitly_wait(2)
         
        def Memory_capacity():
            driver.find_element(By.CSS_SELECTOR, # press the buttom 'Przejdź do wystawiania oferty'
                                 "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(2)").click()                       
            
            driver.implicitly_wait(2) 
            
            if Memory == '16 GB' or Memory == '16' :       # | can be like or
                driver.find_element('xpath',"(//li[@role='menuitem radio'])[1260]").click()
            elif Memory == '32 GB' or Memory == '32': 
                driver.find_element('xpath',"(//li[@role='menuitem radio'])[1261]").click() 
            elif Memory == '64 GB' or Memory == '64': 
                driver.find_element('xpath',"(//li[@role='menuitem radio'])[1262]").click() 
            elif Memory == '128 GB' or Memory == '128': 
                driver.find_element('xpath',"(//li[@role='menuitem radio'])[1263]").click() 
            elif Memory == '256 GB' or Memory == '256': 
                driver.find_element('xpath',"(//li[@role='menuitem radio'])[1264]").click() 
            elif Memory == '512 GB' or Memory == '512': 
                driver.find_element('xpath',"(//li[@role='menuitem radio'])[1265]").click() 
            elif Memory == '1000 GB' or Memory == '1000' or Memory == '1 TB':  
                driver.find_element('xpath',"(//li[@role='menuitem radio'])[1266]").click() 
            else:
                print('APPLICATION ERROR. You need to set the ad memory capacity')                                                                                       
        Memory_capacity()     
        
        

        
        # C:/TextFile1.txt \n C:/TextFile2.txt \n C:/TextFile3.txt
#        driver.find_element(By.CSS_SELECTOR, # press the buttom 'Przejdź do wystawiania oferty'
#                                 "button[class='jsPhotoUploaderButton needsclick']").send_keys('C:\Users\Piotr\Desktop\kurs\py coursera google crash\OLX_Bot\iPhone 12 mini zielony\1 \n C:\Users\Piotr\Desktop\kurs\py coursera google crash\OLX_Bot\iPhone 12 mini zielony\2')                       

#        def photos():
#            c1 = driver.find_element('xpath', 
#                                "//button[normalize-space()='Dodaj z komputera']")
#            
#            driver.implicitly_wait(10)
#            
#            c1.send_keys('C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/iPhone 12 mini zielony/1.jpeg \n C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/iPhone 12 mini zielony/2.jpeg \n C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/iPhone 12 mini zielony/3.jpeg \n C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/iPhone 12 mini zielony/4.jpeg ')  
#        photos()



#P1 = 'C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/iPhone 12 mini zielony/1.jpeg' 
#P2 = 'C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/iPhone 12 mini zielony/2.jpeg'
#P3 = 'C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/iPhone 12 mini zielony/3.jpeg'
#P4 = 'C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/iPhone 12 mini zielony/4.jpeg'
#P5 = 'C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/iPhone 12 mini zielony/5.jpeg'
#P6 = 'C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/iPhone 12 mini zielony/6.jpeg'

#        def photos(): #creating a function that adds images to cells
#            c1 = driver.find_element(By.CSS_SELECTOR, #set Photos jpg in cell 1
#                                'body > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > main:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)')
#            c1.send_keys(P1)  
#
#            c2 = driver.find_element('xpath', #set Photos jpg in cell 2
#                                '(//input[@id="photo-attachment-files"])[2]')
#            c2.send_keys(P2)  
#
#            c3 = driver.find_element(By.XPATH, #set Photos jpg in cell 3
#                                '(//input[@id="photo-attachment-files"])[3]')
#            c3.send_keys(P3)    
#
#            c4 = driver.find_element('xpath', #set Photos jpg in cell 4
#                                '/html[1]/body[1]/div[1]/div[1]/form[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/input[1]')
#            c4.send_keys(P4)        



              
#        def photos(): #creating a function that adds images to cells
#            c1 = driver.find_element(By.CSS_SELECTOR, #set Photos jpg in cell 1
#                                'body > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > main:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)')
#            c1.send_keys(P1)  
#
#            c2 = driver.find_element('xpath', #set Photos jpg in cell 2
#                                '(//input[@id="photo-attachment-files"])[2]')
#            c2.send_keys(P2)  
#
#            c3 = driver.find_element(By.XPATH, #set Photos jpg in cell 3
#                                '(//input[@id="photo-attachment-files"])[3]')
#            c3.send_keys(P3)    
#
#            c4 = driver.find_element('xpath', #set Photos jpg in cell 4
#                                '/html[1]/body[1]/div[1]/div[1]/form[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/input[1]')
#            c4.send_keys(P4)
            
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
                    
       # PROBLEM - WHEN I TRY TO ADD FIFTH PHOTO UNFORTUNATELY MY PROGRAM UPLOAD DUPLICATE: FIRST PHOTO AND THIS ONE WHICH I PICKED 
#        photos()

        #print('Is negotiable ? (write yes or no)')

        driver.find_element('xpath', #set Description advertisement
                             "//div[@contenteditable='true']").send_keys(Description)     


        def PriceAuction():
            Price_Auction = float()
            yes = driver.find_element('xpath',      #set auction option
                                 "//label[@for='wc0-w0-LIST_PAGE_WRAPPER__-PRICE_VIEW__-PRICE_DETAIL_VIEW__-w0-auctionDiyPriceGroup__-auctionSelection__-checkbox']")
            if Auction == 'no':  
                yes.click()       
                pass               
            elif Auction == 'yes' :   
                driver.find_element('xpath',     
                    "(//input[@id='wc0-w0-LIST_PAGE_WRAPPER__-PRICE_VIEW__-PRICE_DETAIL_VIEW__-w0-auctionDiyPriceGroup__-auctionDiyPriceGroupNew__-startPrice__-textbox'])[1]").send_keys(Price_Auction)
            else :
                print('Error! You have to set "yes" or "no" option')
 
        def BuyNow():
            yes = driver.find_element('xpath',      #set buy option
                                 "//input[@id='wc0-w0-LIST_PAGE_WRAPPER__-PRICE_VIEW__-PRICE_DETAIL_VIEW__-w1-binDiyPriceGroup__-binPriceSelection__-checkbox']")
            if Buy_Auction == 'yes':  
                yes.click()           

                driver.implicitly_wait(2)

                driver.find_element('xpath',     
                    "(//input[@id='wc0-w0-LIST_PAGE_WRAPPER__-PRICE_VIEW__-PRICE_DETAIL_VIEW__-w0-auctionDiyPriceGroup__-auctionDiyPriceGroupNew__-startPrice__-textbox'])[1]").send_keys(Price_Buy_Auction)
            else:  
                pass
        PriceAuction()
        BuyNow()

        def Shipping():
            Standard_services = driver.find_element('xpath,' "//div[@id='wc0-w0-LIST_PAGE_WRAPPER__-SHIPPING_PRIMARY_SERVICE_OVERLAY__-shippingPrimaryServiceDetails__-0-w1-w0']//span[@class='listShippingServiceSelect__groupContentCell serviceName']")
            Expedited_services = driver.find_element('xpath,' "//div[@id='wc0-w0-LIST_PAGE_WRAPPER__-SHIPPING_PRIMARY_SERVICE_OVERLAY__-shippingPrimaryServiceDetails__-0-w3-w0']//span[@class='listShippingServiceSelect__groupContentCell serviceName']")
            Other_services = driver.find_element('xpath,' "//div[@id='wc0-w0-LIST_PAGE_WRAPPER__-SHIPPING_PRIMARY_SERVICE_OVERLAY__-shippingPrimaryServiceDetails__-0-w5-w0']//span[@class='listShippingServiceSelect__groupContentCell serviceName']")
        
            yes = driver.find_element('xpath',      #set shipping option
                                 "//label[@for='wc0-w0-LIST_PAGE_WRAPPER__-SHIP_VIEW__-shipYourItem__-checkbox']")
            if Auction == 'no':  
                yes.click()                      
            else:  
                driver.find_element('xpath',     
                    "//button[@id='wc0-w0-LIST_PAGE_WRAPPER__-SHIP_VIEW__-SHIP_GRID_VIEW_PRIMARY_WRAPPER__-SHIP_GRID_VIEW_PRIMARY__-SHIP_DIY_SERVICES_GROUP__-shippingAvailableNotSelected__-shippingPrimaryServiceSelectService__']").click()
        
            driver.implicitly_wait(2)

            if Delivery == 'standard':       
                Standard_services.click()
            elif Delivery == 'priority':
                Expedited_services.click()
            elif Delivery == 'abroad':
                Other_services.click()  
            elif Delivery == 'no':
                pass                       
            else:
                print('ERROR')

            driver.implicitly_wait(1)

            driver.find_element('xpath',      #set 'Ty płacisz' option
                                 "//input[@id='wc0-w0-LIST_PAGE_WRAPPER__-SHIP_VIEW__-SHIP_GRID_VIEW_PRIMARY_WRAPPER__-SHIP_GRID_VIEW_PRIMARY__-SHIP_DIY_SERVICES_GROUP__-SHIP_PRIMARY_SERVICES_COST__-w1-SHIP_PRIMARY_DIY_COST__-shippingPrimaryServicePaymentType__-SP']")        
        Shipping()


   






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
    username = "piotrusiek200@gmail.com"
    password = "Sprzedam1249"
        
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
    
    
    State = 'new'   # Set which state you want.You can use polish or english langugage : ( used / new / broken ) or (Używane / Nowe / Uszkodzone)

    Phone_Model = 'Apple iPhone 12 mini' #write like this - Apple iPhone 12
    Color = 'gold' # set: bezowy, bialy, brazowy, czarny, czerwony, fioletowy, niebieski, pomaranczowy, przezroczysty, rozowy, srebrny, szary, wielokolorowy, zielony, zloty, zolty    
    Memory = '64 GB' # set: 16,32,64,128,256,512,1000 (GB)
    
    
    
        
    Price = '1900' # set price
    Location = 'Warszawa' # set location
    Phone_Number = '500400300' # set phone number
    
    Auction = 'no'  # write 'no' when you don't want add auction, if nywrite 'yes'
    #Price_Auction = '100'  # if you want to have option auction = 'yes' set a minimum price
    Buy_Auction = 'yes' #set the price at which you can buy the phone using the buy now function
    Price_Buy_Auction = '1700' #set the price at which you want to sell the phone using the buy now function
    Delivery = '' # set shipping: 'standard' or 'priority' or 'abroad'
    
    
    State = 'new'   # Set which state you want.You can use polish or english langugage : ( used / new / broken ) or (Używane / Nowe / Uszkodzone)
    Phone_Model = 'iPhone 12 mini'                       # write iPhone model:  
    #                                (looks like this: 'iPhone, space buttom, which model) 
    #                                (for example: iPhone 14 Pro   or  iPhone 14 Pro Max)
    Auto_Extension = 'yes'  # write 'yes' if you want auto extension suddenly every 30 days, if not write 'no'

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
    
    # URL of the login page of site
    # which you want to automate login.
    url = 'https://signin.ebay.pl/ws/eBayISAPI.dll?SignIn&ru=https%3A%2F%2Fwww.ebay.pl%2Fmys%2Fhome%3Fsource%3DGBH'
    
    # Call the function
    startAutoLogin(username, password, url)

    
