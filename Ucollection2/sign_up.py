from tkinter import *
from tkinter import Tk
import os
import tkinter as tk
#from tkinter import ttk 
from tkcalendar import DateEntry


class sign_up_window(tk.Toplevel):
    def __init__(self, main):
        
        global temp_name
        global temp_gender
        global temp_password
        global cal
        global notif
    
    #defining variables
        self.temp_name = StringVar()
        self.temp_age = StringVar()
        self.temp_gender = StringVar()
        self.temp_password = StringVar()
        self.select_ent=StringVar()
        sign_up_window=Toplevel(main)
        sign_up_window.configure(bg="#2FA4FF")
        sign_up_window.title("Sign_Up_Page")
        sign_up_window.geometry('400x350') 
    # Labels for register
    
        self.txt2=Label(sign_up_window, text="please enter your registration credentials below", fg="#EE5007",bg="#2FA4FF",font=('Calibri',12)).grid(row=0, sticky=N, pady=10)
        self.txt3=Label(sign_up_window, text="Name", fg="#EE5007", bg="#2FA4FF", font=('Calibri',12)).grid(row=1, sticky=W)
        self.txt4=Label(sign_up_window, text="Date of Birth", fg="#EE5007",bg="#2FA4FF",font=('Calibri',12)).grid(row=2, sticky=W)
        self.txt5=Label(sign_up_window, text="Gender", fg="#EE5007", bg="#2FA4FF",font=('Calibri',12)).grid(row=3, sticky=W)
        self.txt5=Label(sign_up_window,text="Password,", fg="#EE5007",bg="#2FA4FF", font=('Calibri',12)).grid(row=4, sticky=W)
        self.notif=Label(sign_up_window, font=('Calibri',12))
        self.notif.grid(row=7, sticky=N, pady=20)
       
        
 #Entries
  #Entry/Inputs
        self.ent=Entry(sign_up_window, textvariable=self.temp_name).grid(row=1, column=0)
        self.ent3=Entry(sign_up_window, textvariable=self.temp_gender).grid(row=3, column=0)
        self.ent4=Entry(sign_up_window, textvariable=self.temp_password,show="*").grid(row=4, column=0)
        self.cal=DateEntry(sign_up_window, selectmode='day', textvariable=self.select_ent)
        self.cal.grid(row=2, column=0, padx=15)
        #Button for registration
        
        #self.grid(row=5, column=0,sticky=N,pady=10)
        self.button2=Button(sign_up_window, text="Sign_up",command=self.get_user_information, font=('Calibri', 12), width=20,bg='#00E7FF').grid(row =5, sticky=N, pady=10)
    def get_user_information(self): #(get_user_information)
        name=self.temp_name.get()
        self.cal.get()
        gender=self.temp_gender.get()
        password=self.temp_password.get()
        all_accounts=os.listdir()
    
        if name==""or password==""or gender=="":
        #using confidg to access the object's attributes after initialisation
            self.notif.config(fg="red", text="All fields required * ")
            return
        else:
            self.notif.config(fg="green", text="Successful Registration!")

    
    
        for name_check in all_accounts:
            if name == name_check:
                self.notif.config(fg="red", text="This name already exists")
                return
            else:
                new_file=open(name, "w")
                new_file.write( name+'\n')
                new_file.write(password+ '\n')
                new_file.write(gender+'\n')

                new_file.close()
                self.notif.config(fg="green", text="Account has been created successfully")