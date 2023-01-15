from tkinter import *
from tkinter import Tk
import os
import tkinter as tk
from dashboard import Dashboard
import Driver






class sign_in_window(tk.Toplevel):
    
    def __init__(self, main):
         #globalize variables
    
        
        global loginpassword
        global loginname
        global lnotif
        global sign_in_window
        #define variables for login
        loginname= StringVar()
        loginpassword= StringVar()
        sign_in_window=Toplevel(main)
        sign_in_window.configure(background='#2FA4FF')
        sign_in_window.title("Login Page")
    
        #Labels for login
        self.lbll1=Label(sign_in_window, text="Please sign in to your account", fg="#EE5007", bg="#2FA4FF",font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
        self.lbll2=Label(sign_in_window, text="Username", fg="#EE5007",  bg="#2FA4FF",font=('Calibri', 12) ).grid(row=1, sticky=N, )
        self.lbll3=Label(sign_in_window, text="Password", fg="#EE5007",  bg="#2FA4FF",font=('Calibri', 12)).grid(row=2, sticky=N, )
        self.lbll4=lnotif=Label(sign_in_window, font=('Calibri',12))
        self.lbll5=lnotif.grid(row=6, sticky=N, pady=10)
        #Enteries/Inputs for login
 
        self.ent1=Entry(sign_in_window, textvariable=loginname).grid(row=1, column=0, pady=20)
        self.ent2=Entry(sign_in_window, textvariable=loginpassword, show="*").grid(row=2, column=0, pady=20)
    
 # Button for login
 
        #Button(sign_in_window, text="Signin", command=ma.sign_in_session, font=('Calibri', 12), width=15).grid(row=3, column=0, sticky=N, pady=5, padx=5)
        self.button1=Button(sign_in_window, text="sign_in", font=('Calibri', 12), width=10, bg="#2192FF",command=self.dashboard_show).grid(row=4, sticky=N)
    def dashboard_show(self):
        self.goto_dashboard=Dashboard(Driver.main)
    
    
        
        
        
        
