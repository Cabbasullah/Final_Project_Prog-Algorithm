
import tkinter as tk
from tkinter import *
import dashboard
import os

class ViewBooksWindow(tk.Toplevel):
    
    def __init__(self, main):
        super().__init__()
        file=open(dashboard.User_name,'r')
        file_data=file.read()
        user_details=file_data.split('\n')
            
        details_name= user_details[0]
        details_gender=user_details[2]
        self.files=None
        self.filetxt=None
        self.file=None
        self.foldername=None
        self.file_name=StringVar()
        self.folder_name=StringVar()
   
    
    
        collection_window = Toplevel(main)
        collection_window.title('Your Collection Details')
        collection_window.configure(bg="#009EFF")
        #collection_window.geometry('500x350') 


        Label(collection_window , text="Collection Details", bg="#0096FF", fg="#100F0F",font=('Calibri',12)).grid(row=0, sticky=N, pady=10)
        Label(collection_window, text="Name  :  "+details_name, bg="#0096FF", fg="#100F0F", font=('Calibri',12)).grid(row=1, sticky=W)

        Label(collection_window, text="gender  :  "+details_gender,bg="#0096FF", fg="#100F0F", font=('Calibri',12)).grid(row=3, sticky=W)
   
    
    
        Label(collection_window, text = "View Your Books Below", bg="#0096FF", fg="#100F0F",font=('Calibri', 14)).grid(row=4, sticky=N, pady=10)

        #self.btn_e=Button(collection_window, text="Search",fg="#100F0F", font=("Calibri", 12),bg="#00E7FF",command=self.search)
        #self.btn_e.grid()
        #self.notif=Label(collection_window, font=('Calibri',12))
        #self.notif.grid()
        self.enn=Entry(collection_window,textvariable=self.folder_name, width=20 )
        self.enn.grid(row=6)
        self_btn_file=Button(collection_window, text="search_folder", font=('Calibri', 12), command=self.folder_books, width=10)
        self_btn_file.grid(row=7)
        self.btn_lis=Button(collection_window, text="search_files", fg="#100F0F",font=('Calibri',12), bg="#00E7FF", command=self.refresh_list)
        self.btn_lis.grid(row=8, column=0, pady=50)
        self.listbox = Listbox(collection_window, width=50,font=("Arial", 12))
        self.listbox.grid(row=5)
        self.enn=Entry(collection_window,textvariable=self.file_name, width=20 )
        self.enn.grid(row=9, sticky=N)
        self_btn_file=Button(collection_window, text="search_Book", font=('Calibri', 12), command=self.file_txt, width=10)
        self_btn_file.grid(row=10, column=0)
    
        self.btn_lis=Button(collection_window, text="Refresh", fg="#100F0F",font=('Calibri',12), bg="#00E7FF", command=self.refresh)
        self.btn_lis.grid(row=12)
        self.btn_rm=Button(collection_window, text="delete", fg="#100F0F",font=('Calibri',12),bg="#00E7FF", command=self.delete)
        self.btn_rm.grid(row=13, column=0)
        self.confirmation=Label(collection_window, font=('Calibri', 12))
        self.confirmation.grid(row=14, sticky=N, pady=10)
        
        
    def file_txt(self):
        self.filename=self.file_name.get()
        if self.filename in os.listdir(self.foldername):
            with open(os.path.join(self.foldername, self.filename), 'r') as f:
                text = f.read()
            self.confirmation.config(text=f'{self.filename} is found!, click on refrsh to view book_details', fg="green")
        else:
            self.confirmation.config(text=f'{self.filename} is not listed!', fg="red")
            
            
    def delete(self):
        #self.foldername=self.folder_name.get()
        self.filename=self.file_name.get()
        if self.filename in os.listdir(self.foldername):
            os.remove(f'/home/abas/Ucollection2/{self.foldername}/{self.filename}')
            self.confirmation.config(text=f'{self.filename} successfully deleted!, click on search_files to view others', fg="blue")
        
        
           
            
    def folder_books(self):
            self.foldername=self.folder_name.get()
            if os.path.isdir(self.foldername):
            
                  self.files = os.listdir(self.foldername)
                  self.confirmation.config(text=f'{self.foldername} found, now click search_files', fg="green")
            else:
                self.confirmation.config(text=f'{self.foldername} is not in our list, try again', fg="red")
                
            
    
    
    
                
    def refresh_list(self):
        self.listbox.delete(0, "end")
        if os.path.isdir(self.foldername):
            self.files = os.listdir(self.foldername)
            for file in self.files:
                self.listbox.insert("end", file.strip())
                
    def refresh(self):
        self.listbox.delete(0, "end")
        if self.filename in os.listdir(self.foldername):
            with open(os.path.join(self.foldername, self.filename), 'r') as f:
                self.book = f.read()
                self.listbox.insert("end", self.book.strip())

        #with open(self.filename, "r") as f:
            #for line in f:
                
        #with open(self.filename, 'r') as f:
                    #self.book_data = f.read()
                        

        #with open(self.filename, "r") as f:
            #for line in f:
                #self.listbox.insert("end", line.strip())
                
                

       

       
        
        
                


   