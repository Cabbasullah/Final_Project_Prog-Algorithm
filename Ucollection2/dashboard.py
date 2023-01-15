from tkinter import *
from tkinter import Tk
import os
import tkinter as tk
from new_collection_bk import new_collection_window
from view_collection import ViewBooksWindow

import signin_m
import Driver

class Dashboard(tk.Toplevel):
    def __init__(self, main):
        new_log=signin_m.loginname
        new_pass=signin_m.loginpassword
        new_lnof=signin_m.lnotif
        
        global User_name
        all_accounts=os.listdir()
        User_name=new_log.get()
        Login_Password=new_pass.get()
        for list_check in all_accounts:
            if User_name==list_check:
                file = open(list_check,'r')
                file_data=file.read()
                file_data=file_data.split("\n")
                password=file_data[1]
                #Account Dashboard
                if Login_Password==password:
                #Screen Destroy
                    signin_m.sign_in_window.destroy()
                    Dashboard=Toplevel(main)
                    Dashboard.config(bg="#009EFF")
                    Dashboard.title("Account Management Page")
                    #Labels
                    self.dash1=Label(Dashboard, text="Dhashboard", fg="#CF0A0A", bg="#00E7FF", font=('Calibri', 12)).grid(row=0, sticky=N,pady=10)
                    self.dash2=Label(Dashboard, fg="#CF0A0A", bg="#00E7FF", text="Welcome "+list_check, font=('Calibri', 12)).grid(row=1, sticky=N,pady=5)
                
                    #Buttons for dhashboard page
                    self.button2=Button(Dashboard,text="Your Collection", fg="#CF0A0A",command=self.your_collection, bg="#00E7FF", font=('Calibri',12), width=30).grid(row=2, sticky=N, padx=10)
                    self.dash3=Label(Dashboard).grid(row=5,sticky=N, pady=10)
                    
                    self.button4=Button(Dashboard,text="Create_New_Collection", fg="#CF0A0A", command=self.create_collection,bg="#00E7FF", font=('Calibri',12), width=30).grid(row=3, sticky=N, padx=10)
                    
                    
                    return
                else:
                    new_lnof.config(fg="red", bg="#0096FF", text="Your Password is incorrect")
                    return
            new_lnof.config(fg="red", bg="#0096FF", text="No account found")
    
    
    
        if User_name==""or Login_Password=="":
        
            new_lnof.config(fg="red", bg="#0096FF",text="All fields required *")
        else:
         return 
    
    
           # Label(collection_window, text = "Your List Books", font=('Calibri', 14)).grid(row=4, sticky=N, pady=10)
               
    def create_collection(self):
        self.new_coll=new_collection_window(Driver.main)
    def your_collection(self):
        self.your_list=ViewBooksWindow(Driver.main)