from tkinter import *
import Driver #import Driver#importing Driver module so that the variable main in Driver can be accessed in this module
import os #importing Os python module, so that our program can iteract with our operating system.
import tkinter as tk
from view_collection import ViewBooksWindow
from new_collection_bk import new_collection_window


import signin_m #importing sigin_m module so that variables in that module can be accessed in this module


class Dashboard(tk.Toplevel):
    def __init__(self, main):
        '''Defining and accessing varibles; loginname, loginpassword, and lnotif so that they can be used here.
          Since you can not just enherit attributes in another class in TKinete, you access variable in other module by calling the module to the variable
          that should be accessed.
        '''
        new_log=signin_m.loginname
        new_pass=signin_m.loginpassword
        new_lnof=signin_m.lnotif
        #globalizing variable user_name
        global User_name
        all_folders=os.listdir()#introducing os.listdir method to access are the directories in the current directory
        User_name=new_log.get()#getting the the user_name from the sign_in page
        Login_Password=new_pass.get()#getting the password from the sign_in page
        for list_check in all_folders:#Looping through all the directories
            '''
            If the following condition is met, 
            The folder that was created as the user_name of the user in the sign_up page will be opened, and the 
            and only the password will be accessed. If the password is equal to the same password that was created by the user, then
            the login_window will be destroyed since we will not needed it anymore. And the Dashboard_window will be 
            opened automatically.
            '''
            if User_name==list_check:
                file = open(list_check,'r')
                file_data=file.read()
                file_data=file_data.split("\n")
                password=file_data[1]#accessing the index of the password value
                #Account Dashboard
                if Login_Password==password:
                #Screen Destroy
                    signin_m.sign_in_window.destroy()
                    '''
                    This is where the dashboard_window starts, after the sign_in_window gets destroyed.
                    '''
                    Dashboard=Toplevel(main)
                    Dashboard.config(bg="#009EFF")
                    Dashboard.title("Dashboard")
                    #Labels
                    self.dash1=Label(Dashboard, text="Dhashboard", fg="#CF0A0A", bg="#00E7FF", font=('Times New Roman', 12))
                    self.dash1.grid(row=0, sticky=N,pady=10)
                    self.dash2=Label(Dashboard, fg="#CF0A0A", bg="#00E7FF", text="Welcome "+list_check, font=('Times New Roman', 12))#This will dispaly
                                                                                                                                        #welcome + whatever the name
                                                                                                                                        #of that user
                    self.dash2.grid(row=1, sticky=N,pady=5)
                    
                    #Buttons for dhashboard page
                    self.button2=Button(Dashboard,text="Your Collection", fg="#CF0A0A",command=self.your_collection, bg="#00E7FF", font=('Times New Roman',12), width=30)
                    self.button2.grid(row=2, sticky=N, padx=10)
                    self.dash3=Label(Dashboard)
                    self.dash3.grid(row=5,sticky=N, pady=10)
                    
                    self.button4=Button(Dashboard,text="Create_New_Collection", fg="#CF0A0A", command=self.create_collection,bg="#00E7FF", font=('Times New Roman',12), width=30)
                    self.button4.grid(row=3, sticky=N, padx=10)
                    
                    
                    return
                
                else:
                    new_lnof.config(fg="red", bg="#0096FF", text="Your Password is incorrect")#If the condition above is not met, the user will be noitified about their incorrect password
                    return
            new_lnof.config(fg="red", bg="#0096FF", text="No account found")#If the user_name is incorrect, the user will be notified
    
    
        '''If the username and passoword fields left empty, the user
         will be alerted: "All fields are required"
         '''
        if User_name==""or Login_Password=="":
        
            new_lnof.config(fg="red", bg="#0096FF",text="All fields required *")
        else:
         return 
    
    
           # Label(collection_window, text = "Your List Books", font=('Calibri', 14)).grid(row=4, sticky=N, pady=10)
        
        '''
        The dashboard hosts the functions and button that will display the view_collection window and the create_collection window
        The following are the two function controlled by the button in the dashboard and they will open the window each one represents.
        '''
    def create_collection(self):
        self.new_coll=new_collection_window(Driver.main)
    def your_collection(self):
        self.viewbooks=ViewBooksWindow(Driver.main)
        
        
    