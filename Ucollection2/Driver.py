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

class main_collection(tk.Tk):
    
    def __init__(self,main):
        
        frame = Frame(main, width=600, height=400)
        frame.grid()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        self.Label1=Label(main, text = "Organize Your Reading Here", fg="#10A19D",font=('Times New Roman', 21))
        self.Label1.grid(row=0, sticky=N, pady=10)
        self.Label2=Label(main, text = "Develop Good Reading Habit and Create Your Own Collection", fg="#10A19D", font=('Times New Roman', 14))
        self.Label2.grid(row=1, sticky=N, pady=10)
        self.img=Label(main, image=img).grid(row=5, sticky=N, pady=20)
        #self.img=Label(main, photo=img).grid(row=4, sticky=N, pady=15)
        #Buttons
        self.button1=Button(main, text="Join-us", font=('Bold', 12), width=20, bg="#00E7FF",command=self.show_signup_window).grid(row=3, sticky=N, pady=10)

        self.button2=Button(main, text="Signin", font=('Bold', 12), width=20, bg='#00E7FF', command=self.show_sigin_window).grid(row=4, sticky=N, pady=10)
        
        
    def show_signup_window(self):
        self.su_window=sign_up_window(main)
    def show_sigin_window(self):
        self.si_window=sign_in_window(main)
    

main = None




if __name__ == "__main__":   
    main=Tk()
    main.configure(bg="#C0DEFF")
    img = ImageTk.PhotoImage(Image.open("rd.bmp"))

    ma=main_collection(main)
    
    
    



    main.geometry('500x350') 
    main.title("Reading Progress App")
    main.mainloop()