from tkinter import *
from tkinter import Tk
import os #importing Os python module, so that our program can iteract with our operating system.
import tkinter as tk
from PIL import ImageTk, Image

#from tkinter import ttk 
#from tkcalendar import DateEntry

'''
Sign_Up_Window uses tk.Toplevel and it controls all the widgets created under this class,
but still, this window is a subwindow of the main_window.
'''
class sign_up_window(tk.Toplevel):
    def __init__(self, main):
        '''Globalizing textvariables, so they can be used as an iput value in other parts of the code.
        '''
        self.user_name=None
        self.user_gender=None
        self.user_password=None
        global cal
        self.notif=None
        
        '''Defining text_variables as stringVar(which means it will hold input values of string that can be retrieved later)
        '''
        self.user_name = StringVar()
        self.user_age = StringVar()
        self.user_gender = StringVar()
        self.user_password = StringVar()
        self.select_ent=StringVar()
        
        sign_up_window=Toplevel(main)#Defining toplevel window, and calling the class window with respect to Toplevel
        sign_up_window.configure(bg="#2FA4FF")#By using configure method, we can change the background color.
                                              #In general, configure method is used to change the options of a widget.
        sign_up_window.title("Sign_Up_Page")#Title method is used to give title to the page
        sign_up_window.geometry('300x350')#Defining the size of he window by using geometry method.
        img =ImageTk.PhotoImage(Image.open("rd.bmp"))
   
        #Labels
        
        self.txt2=Label(sign_up_window, text="please enter your registration credentials below", fg="#EE5007",bg="#2FA4FF",font=('Times New Roman',16))
        self.txt2.grid(row=0, sticky=N, pady=10)
        self.txt3=Label(sign_up_window, text="Name", fg="#EE5007", bg="#2FA4FF", font=('Times New Roman',16)).grid(row=2, sticky=W)
        self.txt5=Label(sign_up_window, text="Gender", fg="#EE5007", bg="#2FA4FF",font=('Times New Roman',16)).grid(row=4, sticky=W)
        self.txt5=Label(sign_up_window,text="Password,", fg="#EE5007",bg="#2FA4FF", font=('Times New Roman',16)).grid(row=6, sticky=W)
        self.notif=Label(sign_up_window, font=('Times New Roman',12))#This will be accessed by config in order to display texts on the page
        self.notif.grid(row=8, sticky=N, pady=20)
        self.img=Label(sign_up_window, image=img)
        self.img.grid(row=9, sticky=N, pady=20)
       
        

  #Entry/Inputs
        '''
        This will create entry boxes, and what ever the user enters in the entry boxes will be 
        used as input values by the function.
        '''
        self.ent=Entry(sign_up_window, textvariable=self.user_name)
        self.ent.grid(row=2, column=0)
        self.ent3=Entry(sign_up_window, textvariable=self.user_gender)
        self.ent3.grid(row=4, column=0)
        self.ent4=Entry(sign_up_window, textvariable=self.user_password,show="*")
        self.ent4.grid(row=6, column=0)
        #self.cal=DateEntry(sign_up_window, selectmode='day', textvariable=self.select_ent)
        #self.cal.grid(row=2, column=0, padx=15)
        #Button for registration
        '''
        The button below will call the following function, and the function will respond to the instructions.
        '''
        self.button2=Button(sign_up_window, text="Sign_up",command=self.get_user_information, font=('Times New Roman', 12), width=20,bg='#00E7FF')
        self.button2.grid(row =7, sticky=N, pady=10)
    def get_user_information(self): #(get_user_information)
        
        name=self.user_name.get()#This function will receive name from the user through textvariables from the entry box.
        gender=self.user_gender.get()#This function will receive gender from the user through textvariables from the entry box.
        password=self.user_password.get()#This function will receive password from the user through passowrd textvariable from the entry box.
        all_directories=os.listdir()#Defining os.lisrdir(methos from Os module that lists all the directories in the current directory)
    
        if name==""or password==""or gender=="": #If this condition is met(when all those fields are empty.)
        
            self.notif.config(fg="red", text="All fields required * ")#config method that helps change widget's options(displaying text if the above condition is met)
            return
        else:
            self.notif.config(fg="green", text="Successful Registration!")

    
        '''Looping through all the items in all directories(os.listdir()),
        and if name, which contains the value of the user's input is found, it will
        return a notifcation informing the new user about the existance of their username. 
        If not, the name other user_details will be saved to the file.
        '''
        for  a_folder in all_directories:
            if name == a_folder:
                self.notif.config(fg="red", text="This name already exists")
                return
            else:
                '''
                The users' name will be saved as the name entered by the user and without file extension but as a folder
                All the user_details will be intered into that folder
                '''
                with open(name, "w") as new_file:
                    
                    new_file=open(name, "w")
                    new_file.write( name+'\n')
                    new_file.write(password+ '\n')
                    new_file.write(gender+'\n')
                self.notif.config(fg="green", text="Account has been created successfully")