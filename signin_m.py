from tkinter import *
from tkinter import Tk
import os #importing Os python module, so that our program can iteract with our operating system.
import tkinter as tk
from dashboard import Dashboard
import Driver#importing Driver module to access variable main in Driver module.






class sign_in_window(tk.Toplevel):
    
    def __init__(self, main):
         #globalize variables
    
        '''Globalizing variables so they can be used in other module.
        This pages/ign_in page will take two inputs from the user: Username and Password
        Textvariables in Entry boxes are, so that the input values of what the user entered will be 
        treated as input values.
        '''
        global loginpassword
        global loginname
        global lnotif
        global sign_in_window
        #define variables for login
        loginname= StringVar()
        loginpassword= StringVar()
        sign_in_window=Toplevel(main)##Defining toplevel window, and calling the class window with respect to Toplevel
        sign_in_window.configure(background='#2FA4FF')
        sign_in_window.title("Login Page")
    
        #Labels for login
        '''Label widgets and Entry widgets have been used here. Then Entry boxes will receive the user's 
        input values and hold it as string and later can be used.
        The button widget controls the dashboard function.
        '''

        self.lbll1=Label(sign_in_window, text="Please sign in to your account", fg="#EE5007", bg="#2FA4FF",font=('Times New Roman', 15))
        self.lbll1.grid(row=0, sticky=N, pady=10)
        self.lbll2=Label(sign_in_window, text="Username", fg="#EE5007",  bg="#2FA4FF",font=('Times New Roman', 15) )
        self.lbll2.grid(row=1, sticky=N, )
        self.lbll3=Label(sign_in_window, text="Password", fg="#EE5007",  bg="#2FA4FF",font=('Times New Roman', 15))
        self.lbll3.grid(row=2, sticky=N, )
        self.lbll4=lnotif=Label(sign_in_window, font=('Times New Roman',15))
        self.lbll4=lnotif.grid(row=6, sticky=N, pady=10)
        #Enteries/Inputs for login
 
        self.ent1=Entry(sign_in_window, textvariable=loginname)
        self.ent1.grid(row=1, column=0, pady=20)
        self.ent2=Entry(sign_in_window, textvariable=loginpassword, show="*")
        self.ent2.grid(row=2, column=0, pady=20)
    
 # Button for login
 
        #Button(sign_in_window, text="Signin", command=ma.sign_in_session, font=('Calibri', 12), width=15).grid(row=3, column=0, sticky=N, pady=5, padx=5)
        self.button1=Button(sign_in_window, text="sign_in", font=('Times New Roman', 15), width=10, bg="#2192FF",command=self.dashboard_show)
        self.button1.grid(row=4, sticky=N)
    '''Since, this dashboard window will not be directly managed by the main_window, instead it will be
    managed by the sign_in page. The dashboard function takes Driver.main as an argument. The Driver modula as has been imported into this page.
    '''
    def dashboard_show(self):
        self.goto_dashboard=Dashboard(Driver.main)
    
    
        
        
        
        
