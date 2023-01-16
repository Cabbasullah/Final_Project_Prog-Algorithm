from tkinter import *
from tkinter import Tk
import os
import tkinter as tk

#import PIL.Image
#from tkinter import ttk 
#from tkcalendar import DateEntry 
from sign_up import sign_up_window
from signin_m import *
from PIL import ImageTk, Image


#from dashboard import Dashboard
'''This will be the only class that has tk.TK as a parameter, 
and it because it is the main_class in the main_page. tk is the module 
and Tk is a the main/absolute root of the application which means, 
if the main_window gets closed none of the other windows will remain.
That's why this class has tk.TK and not tk.Toplevel.
'''
class main_collection(tk.Tk):
    
    def __init__(self,main):
        
        '''
        The following are widgets(Labels and buttons). Label widgets display texts on the screen, while Button widgets control a button,
        and when clicked displays whatever instructions was given.
        '''
        self.Label1=Label(main, text = "Organize Your Reading Here", fg="#10A19D",font=('Times New Roman', 21))
        self.Label1.grid(row=0, sticky=N, pady=10)#This is grid is a layout manager, and you can control the positioning of widgets via grid or pack()
        self.Label2=Label(main, text = "Develop Good Reading Habit and Create Your Own Collection", fg="#10A19D", font=('Times New Roman', 14))
        self.Label2.grid(row=1, sticky=N, pady=10)
        self.img=Label(main, image=img).grid(row=5, sticky=N, pady=20)#Adding image to a window(there ImageTk module that needs to be imported for this to be possible)
        #This is just the positioning of the image.
        
        '''
        The commands in the following two button widgets manage their corrosponding functions
        Each command controls the method that it contains, and when the button is clicked, whatever instructions that follow the 
        function will be called.
        '''
        self.button1=Button(main, text="Join-us", font=('Bold', 12), width=20, bg="#00E7FF",command=self.show_signup_window)
        self.button1.grid(row=3, sticky=N, pady=10)

        self.button2=Button(main, text="Signin", font=('Bold', 12), width=20, bg='#00E7FF', command=self.show_sigin_window)
        self.button2.grid(row=4, sticky=N, pady=10)
    
    def show_signup_window(self):#This function commanded by the above button displays the sign_up window as the class from the sign_up module is called.
        self.su_window=sign_up_window(main)#It takes main(Tk) as an argument, which means the sign_up window will be a sub class of the main window. 
    def show_sigin_window(self):#This function commaned by the sign_in button will also open the sign_in window.
        self.si_window=sign_in_window(main)
    

main = None#Globalizing variable window so it can be used in other modules without CIRCULAR IMPORT ERRORS




if __name__ == "__main__":   
    main=Tk()
    main.configure(bg="#C0DEFF")
    img = ImageTk.PhotoImage(Image.open("rd.bmp"))#This is the method that inserts the image into the main_page

    ma=main_collection(main)
    
    
    



    main.geometry('500x350') 
    main.title("Reading Progress App")
    main.mainloop()