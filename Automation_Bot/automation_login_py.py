# Used to import the webdriver from selenium
from selenium import webdriver 
import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver.maximize_window() # maximizing the browser windows 
 
# Get the path of chromedriver which you have install


if __name__ == '__main__': 
    def startAutoLogin(login, password, url):
        path = "C:\\Users\\hp\\Downloads\\chromedriver"

        # giving the path of chromedriver to selenium webdriver
        driver = webdriver.Chrome(path)

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
        #sleep(10) #4294967
        pass
        driver.implicitly_wait(16) # or can use sleep(16)    
    

        driver.find_element('xpath',
                            '//*[@id="onetrust-accept-btn-handler"]').click()
        driver.find_element('xpath',
                           '//*[@id="postNewAdLink"]').click()    
        pass
        driver.implicitly_wait(10)      
    

        
        driver.find_element('xpath', #set Title advertisement
                             '//*[@id="posting-form"]/main/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div/textarea').send_keys(Title)              
        
       #driver.find_element('xpath', #set Category advertisement
       #                     '//*[@id="posting-form"]/main/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div/textarea').click()      

        driver.find_element('xpath', #set Photos advertisement  PHOTOS PHOTOS PHOTOS PHOTOS PHOTOS
                            '//*[@id="photo-attachment-files"]').send_keys(P1)        

        driver.find_element('xpath', #set Description advertisement
                             '//*[@id="posting-form"]/main/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/textarea').send_keys(Description)        

        driver.find_element('xpath', #set Price advertisement
                             '//*[@id="parameters.price.price"]').send_keys(Price)        
        
        #css-11n5kse
        #print('Is negotiable ? (write yes or no)')
        yes = driver.find_element('xpath',
                             '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[1]/div/div[1]/div/div/div/div[3]/span')
        if Negotiable == 'yes':
            yes.click()
        else:
            pass   

        #iPhone_14 = '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/div'


     #  driver.find_element('xpath', #set State advertisement ######################
     #                       '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[3]/div/div/div/button[2]/svg').click()        
        driver.implicitly_wait(0.1)
        
     #  driver.find_element('xpath', #set State advertisement ######################
    #                      '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[3]/div/div/div').click()   
        
      # driver.find_element('xpath', #set model of phone advertisement ######################
      #                      '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/div/button/svg').click()   
      # 
      # driver.find_element('xpath', #set model of phone advertisement ######################
      #                      '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/div/button/svg').click()           
        
      #driver.find_element(By.ID,'Uszkodzone',).click(); # command to find element with ID, no for xpath
        #iPhone_14 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/div').click()
     #  
        driver.find_element(By.CLASS_NAME,'css-e010pl').click()  # press the select button
        driver.implicitly_wait(0.5)
        driver.find_element(By.CLASS_NAME,'css-1n05x61').click() # set state: Używane 

        driver.find_element(By.CLASS_NAME,'css-6z56jw').click()  # press the select button
        driver.implicitly_wait(0.5)     
        driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[1]/div/div/div/a').click()
        #driver.find_element(By.CLASS_NAME,'css-1n05x61').click() # set model of phone: iPhone
        #driver.find_element(By.LINK_TEXT, "iPhone 3GS")        


        #Is auto extension ? (write yes = y or no = n)
        y = driver.find_element('xpath',
                             '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[3]/div/div[1]/div/div/div/label/span')
        if Auto_Extension == 'yes':
            y.click()
        else:
            pass         
     
        Location_clear = driver.find_element(By.NAME,'city_id')
        Location_clear.send_keys(Keys.CONTROL, 'a') # this option remove the old text
        Location_clear.send_keys(Keys.BACKSPACE)    #      (written in column)
        Location_clear.send_keys(Location)          #   set Location advertisement
                            
    #   Location_clear = driver.find_element('xpath','//*[@id="posting-form"]/main/div[1]/div[5]/div/div[1]/div/div/div/div/div/div/div/div/div/div/input')     
    #   Location_clear.send_keys(Keys.CONTROL, 'a') # this option remove the old text 
    #   Location_clear.send_keys(Keys.BACKSPACE)    #      (written in column)
    #   Location_clear.send_keys(Location)          #   set Location advertisement
     
        Phone_clear = driver.find_element('xpath','//*[@id="phone"]') 
        Phone_clear.send_keys(Keys.CONTROL, 'a') # this option remove the old text 
        Phone_clear.send_keys(Keys.BACKSPACE)    #      (written in column)
        Phone_clear.send_keys(Phone_Number)      #    set Number advertisement

        driver.find_element(By.CLASS_NAME,'css-1anknvg').click()  # press the select button        
        driver.implicitly_wait(5) 

        # 'css-165srwn' - class zamawiam i place
        driver.find_element(By.CLASS_NAME,'css-18l8bp6').click()  # press the select button        
        driver.implicitly_wait(5) 
        driver.find_element('xpath', '//*[@id="root"]/div/main/div/div/div[2]/div[1]/a[2]/span/span').click()
   
    
    #    
    #    driver.find_element('xpath', # press the buttom - "Podgląd ogłoszenia"
    #                         '//*[@id="posting-form"]/main/div[1]/div[7]/div/button[1]/span/span').click()  
       
        sleep(4294967) 

        #iPhone_14 = '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/div'               
# iPhone_14_Plus = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[2]/div/div/div/a').click()
# iPhone_14_Pro = driver.find_element('xpath','//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[3]/div/div/div/a')
# iPhone_14_Pro_Max = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[4]/div/div/div/a').click()
# iPhone_13 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[5]/div/div/div/a').click()
# iPhone_13_mini = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[6]/div/div/div/a').click()
# iPhone_13_Pro = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[7]/div/div/div/a').click()
# iPhone_13_Pro_Max = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[8]/div/div/div/a').click()
# iPhone_12 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[9]/div/div/div/a').click()
# iPhone_12_mini = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[10]/div/div/div/a').click()
# iPhone_12_Pro = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[11]/div/div/div/a').click()
# iPhone_12_Pro_Max = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[12]/div/div/div/a').click()
# iPhone_11 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[13]/div/div/div/a').click()
# iPhone_11_Pro = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[14]/div/div/div/a').click()
# iPhone_11_Pro_Max = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[15]/div/div/div/a').click()
# iPhone_SE = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[16]/div/div/div/a').click()
# iPhone_X = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[17]/div/div/div/a').click()
# iPhone_XS = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[18]/div/div/div/a').click()
# iPhone_XS_Max = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[19]/div/div/div/a').click()
# iPhone_XR = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[20]/div/div/div/a').click()
# iPhone_8 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[21]/div/div/div/a').click()
# iPhone_8_Plus = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[22]/div/div/div/a').click()
# iPhone_7 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[23]/div/div/div/a').click()
# iPhone_7_Plus = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[24]/div/div/div/a').click()
# iPhone_6 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[25]/div/div/div/a').click()
# iPhone_6_Plus = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[26]/div/div/div/a').click()
# iPhone_6S = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[27]/div/div/div/a').click()
# iPhone_6S_Plus = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[28]/div/div/div/a').click()
# iPhone_5 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[29]/div/div/div/a').click()
# iPhone_5C = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[30]/div/div/div/a').click()
# iPhone_5S = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[31]/div/div/div/a').click()
# iPhone_4  = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[32]/div/div/div/a').click()
# iPhone_3  = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[33]/div/div/div/a').click()
# iPhone_3G  = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[34]/div/div/div/a').click()
# iPhone_3GS  = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[35]/div/div/div/a').click()
# iPhone_1gen = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[36]/div/div/div/a').click()
# Inne_modele = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[37]/div/div/div/a').click()


# iPhone_14 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/div').click()                 
# iPhone_14_Plus = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[2]/div/div/div/a').click()
# iPhone_14_Pro = driver.find_element('xpath','//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[3]/div/div/div/a')
# iPhone_14_Pro_Max = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[4]/div/div/div/a').click()
# iPhone_13 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[5]/div/div/div/a').click()
# iPhone_13_mini = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[6]/div/div/div/a').click()
# iPhone_13_Pro = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[7]/div/div/div/a').click()
# iPhone_13_Pro_Max = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[8]/div/div/div/a').click()
# iPhone_12 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[9]/div/div/div/a').click()
# iPhone_12_mini = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[10]/div/div/div/a').click()
# iPhone_12_Pro = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[11]/div/div/div/a').click()
# iPhone_12_Pro_Max = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[12]/div/div/div/a').click()
# iPhone_11 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[13]/div/div/div/a').click()
# iPhone_11_Pro = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[14]/div/div/div/a').click()
# iPhone_11_Pro_Max = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[15]/div/div/div/a').click()
# iPhone_SE = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[16]/div/div/div/a').click()
# iPhone_X = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[17]/div/div/div/a').click()
# iPhone_XS = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[18]/div/div/div/a').click()
# iPhone_XS_Max = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[19]/div/div/div/a').click()
# iPhone_XR = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[20]/div/div/div/a').click()
# iPhone_8 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[21]/div/div/div/a').click()
# iPhone_8_Plus = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[22]/div/div/div/a').click()
# iPhone_7 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[23]/div/div/div/a').click()
# iPhone_7_Plus = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[24]/div/div/div/a').click()
# iPhone_6 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[25]/div/div/div/a').click()
# iPhone_6_Plus = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[26]/div/div/div/a').click()
# iPhone_6S = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[27]/div/div/div/a').click()
# iPhone_6S_Plus = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[28]/div/div/div/a').click()
# iPhone_5 = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[29]/div/div/div/a').click()
# iPhone_5C = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[30]/div/div/div/a').click()
# iPhone_5S = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[31]/div/div/div/a').click()
# iPhone_4  = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[32]/div/div/div/a').click()
# iPhone_3  = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[33]/div/div/div/a').click()
# iPhone_3G  = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[34]/div/div/div/a').click()
# iPhone_3GS  = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[35]/div/div/div/a').click()
# iPhone_1gen = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[36]/div/div/div/a').click()
# Inne_modele = driver.find_element('xpath', '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/div/div[1]/div[4]/div/div/ul/li[37]/div/div/div/a').click()

#    D  E  S  C  R  I  P  T  O  N
 
    # Driver Code
    # Enter below your login credentials
    username = ""
    password = ""
        
    # Data in the advertisement  
    Title = 'iPhone 14 Pro Max Deep Purple 1TB' #must be less than 70 characters
    Description = 'I have a brand new iPhone 14 Pro Max for sale. The box is unopened. The phone has all the necessary original seals. Included is the purchase invoice from the Apple store.' #must be more than 80 characters and less than 9000 characters
    Price = '8000'
    Location = 'Warszawa'
    Phone_Number = '500400300'
    Negotiable = 'yes'  #write 'yes' when the price is negotiable , if not write 'no'
    Auto_Extension = 'yes'  #write 'yes' if you want auto extension suddenly every 30 days, if not write 'no'
    #State =  # (Używane / Nowe / Uszkodzone)
    
   # State_press = {'Używane' : 1 , 'Nowe' : 2, 'Uszkodzone' : 3}
   # State_press = State()

 
   #Używane = driver.find_element(By.CLASS_NAME,'css-1n05x61')
   #Nowe = driver.find_element(By.CLASS_NAME,'css-lihuun')
   #Uszkodzone = driver.find_element(By.CLASS_NAME,'css-lihuun')
#       state = 
    #options
    
    # The photos to load #C:\Users\Piotr\Desktop\kurs\py coursera google crash\OLX_Bot\Photos
    P1 = 'C:/Users/Piotr/Desktop/kurs/py coursera google crash/OLX_Bot/Photos' 
    #P2 =
    #P3 =
    #P4 =
    #P5 =
    #P6 =
    #P7 =
    #P8 =

    
    # URL of the login page of site
    # which you want to automate login.
    url = 'https://pl.login.olx.com/?client_id=b0lcnbsn82kvrtk767nn8pg1k&code_challenge=Ze_PviRH2j_CfriWXlcfaEmhtVm_7eTXiwm81ukc1lc&code_challenge_method=S256&redirect_uri=https%3A%2F%2Fwww.olx.pl%2Fkonto%2Fcallback%2F&st=eyJzbCI6IjE4NWZhY2FmMTljeDVhYTMxOWY3IiwicyI6IjE4NjMzMmZlYmUxeDNjYTMxZDE1IiwiY2MiOjF9&state=eyJyZWZlcnJlciI6Imh0dHBzOlwvXC93d3cub2x4LnBsXC9tb2pvbHhcLyJ9'
    
    # Call the function
    startAutoLogin(username, password, url)

    
    
    #url1 = 'https://www.olx.pl/konto/'
    #driver = webdriver.Chrome(path)
    #driver.get(url1)
    #
    #driver.find_element('xpath','//*[@id="onetrust-accept-btn-handler"]').click()
    
#   ############################################
#   def CreateAdvButtom(): 
#       path = "C:\\Users\\hp\\Downloads\\chromedriver" 
#       driver = webdriver.Chrome(path) 
#       sleep(5)
#       driver.find_element('xpath',
#                           '//*[@id="onetrust-accept-btn-handler"]').click()
#       driver.find_element('xpath',
#                           '//*[@id="postNewAdLink"]').click()    
#   ll = CreateAdvButtom()
#   ll.demo_exp_wait

    #wait =
    #
    #ulr2 = 'https://www.olx.pl/konto/'
    #if url2 == True:
    #    CreateAdvButtom()