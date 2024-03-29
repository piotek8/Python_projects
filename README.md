# 🐍 An automated robot for posting ads (in Selenium) 

## 👨‍💻 The project 
A program that, after filling in the necessary data, automatically publishes an advertisement on the OLX, eBay portal in the category of sales of Apple phones. The software is regularly developed by me.

## 🤔 How it works in practice?
#### OLX
https://user-images.githubusercontent.com/82182989/226676476-a32d867b-4b63-435e-a936-220e7ec605e0.mp4

## 💬 Installation instruction 
At the beginning, you must install the software that is mandatory to start the project, it is presented below.
 - [Visual Studio Code](https://code.visualstudio.com/docs/setup/windows)
 - [Python 3+ version](https://realpython.com/installing-python/#how-to-install-python-on-windows)
 - [Google Chrome](https://www.google.com/intl/pl_pl/chrome/) 
 - [Chrome driver to Chrome](https://chromedriver.chromium.org/getting-started)


You need to install the necessary libraries in the terminal in your environment (visual studio code is recommended by me):

```bash
  pip install selenium
               time
               os 
               PyQt6
               sys
               js2py
               ait
  pip install pytube
              moviepy
```
![pip install instruction](https://user-images.githubusercontent.com/82182989/226630656-e2937091-8d83-48ff-9c6e-094fed5b6491.jpg)

## 📜 Selenium Python Bindings Documentation

Use this documentations for learning and finding solutions to problems.

- [Selenium with Python Documentation](https://selenium-python.readthedocs.io/)
- [Stack Overflow](https://stackoverflow.com/)



## 🔗 Run Locally

Clone the project

```
git clone https://github.com/piotek8/Python_projects.git
```
Go to the project directory

```
cd Python_projects
```
Install dependencies

```
npm install
```
Start the server

```
npm run start
```




## ⌨ Source Code
 - [OLX](https://github.com/piotek8/Python_projects/blob/main/Automation_Bot/OLX_automation_login.py)   
 - [eBay](https://github.com/piotek8/Python_projects/blob/main/Automation_Bot/eBay_automation_login_py.py)   
 
## 📁 How to entering data into the program
### Method 1
#### OLX

    username = ""
        enter your email to login account

    password = ""
        enter your password to login account

    Title = ''
        write keywords by which the customer can find the product (must be less than 70 characters)

    Descripton = '''  '''
        can write everything about product (must be more than 80 characters and less than 9000 characters)

    Price = '' 
        set price with only digits (for example: 1900)

    Location = '' 
        set location with only words (for example: Warszawa)

    Phone_Number = '' 
        set phone number with only digits (for example: 500400300)

    Negotiable = ''  
        write 'yes' when the price is negotiable , if not write 'no' (for example: yes)

    State = ''   
        set which state you want. You can use polish or english langugage : 
              ( used / new / broken ) or (Używane / Nowe / Uszkodzone)

    Phone_Model = ''                      
                            write iPhone model 
         (looks like this: 'iPhone, space buttom, which model) 
           (for example: iPhone 14 Pro or iPhone 14 Pro Max)

    Auto_Extension = ''  
        write 'yes' if you want auto extension suddenly every 30 days, if not write 'no' (for example: yes)

    Delivery =  '' 
        write 'yes' when you want delivery , if not write 'no' (for example: yes)

    Size = ''  
        write package size 'S or M or L or XL' size (for example: S)

    Option = 'S_inPost'  # write option of package size for example (S_Orlen, L_inPost, M_PocztaPolska) 
    #                                 (looks like this: 'what size , _ , which courier')
    #                                           (for example: 'L_inPost') 





#### eBay



    username = ""
        enter your email to login account

    password = ""
        enter your password to login account

    Title = ''
        write keywords by which the customer can find the product (must be less than 70 characters)

    Descripton = '''  '''
        can write everything about product (must be more than 80 characters and less than 9000 characters)

    State = ''   
        set which state you want. You can use polish or english langugage : 
              ( used / new / broken ) or (Używane / Nowe / Uszkodzone)

    Phone_Model = '' 
            write model of iPhone 
        (for example: Apple iPhone 12)

    Color = '' 
        set: bezowy, bialy, brazowy, czarny, czerwony, fioletowy, niebieski, pomaranczowy, przezroczysty, rozowy, srebrny, szary,wielokolorowy, zielony, zloty, zolty    

    Memory = '' 
        set memory of iPhone : 16,32,64,128,256,512,1000 (GB)


    ...all info will be soon



### Method 2

    ...in progress during works

![AutoApp_Advertisements](https://user-images.githubusercontent.com/82182989/226767139-61bce2be-c0e9-4775-bfa3-9a7e2cce61d2.jpg)

## 👋 QR Code to scan the project

Can use qr code to share project for others

<a href="url"><img src="https://user-images.githubusercontent.com/82182989/226750124-eecd4aab-93ad-4840-81b8-a41bda82c16e.png" align="left" height="200" width="200" ></a>
