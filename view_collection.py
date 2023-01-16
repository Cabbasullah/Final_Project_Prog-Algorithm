
import tkinter as tk
from tkinter import *
import dashboard
import os

class ViewBooksWindow(tk.Toplevel):
    
    def __init__(self, main):
        super().__init__()
        '''
        The  following code gets Username details(name and gender) stored in a folder from the login_page and dashboard and 
        dispalys it on the top of the screen as Name: username, Gender: Female/Male
        '''
        file=open(dashboard.User_name,'r')#The file's name is the current username's name that was created when they first created their accounts
        file_data=file.read()
        user_details=file_data.split('\n')#The folder will be opened and details in the folder will be spilted eachone in a new_line
            
        details_name= user_details[0]#the indexes  of the user_name @position 0 will be accessed
        details_gender=user_details[2]#The index of the gender @position 1 will be accessed as well
        #Globlizing the function names that will be used
        self.files=None
        self.filetxt=None
        self.file=None
        self.foldername=None
        self.file_name=StringVar()#Defining filename as stringVar so that it can be accessed based on the value of the textvariable as an input value
        self.folder_name=StringVar()#defining foldername as stringvar so that it can be accessed based on the value of the textvariable as an input value
   
    
    
        collection_window = Toplevel(main)#Displaying collection window
        collection_window.title('Your Collection Details')
        collection_window.configure(bg="#009EFF") 

        #Labels for the user details and the title of the page
        Label(collection_window , text="Collection Details", bg="#0096FF", fg="#100F0F",font=('Calibri',12)).grid(row=0, sticky=N, pady=10)
        Label(collection_window, text="Name  :  "+details_name, bg="#0096FF", fg="#100F0F", font=('Calibri',12)).grid(row=1, sticky=W)

        Label(collection_window, text="gender  :  "+details_gender,bg="#0096FF", fg="#100F0F", font=('Calibri',12)).grid(row=3, sticky=W)
   
    
    
        Label(collection_window, text = "View Your Books Below", bg="#0096FF", fg="#100F0F",font=('Calibri', 14)).grid(row=4, sticky=N, pady=10)


        '''
        So this page will help the user manages their account and collection of books by reading their list of books, searching
        for specific book detail and deleting whatever book they want from the list.
        The entry boxes of for foldername, search_book name, and listbox.
        As well as the buttons for the getting_folder_name, search_files, and refreshing list
        
        '''
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
        
    '''
    This function function searches for specific book detail, so when user click on the button for this function after
    specifying the file_name will open the file and view the book details.
    '''
    
    def file_txt(self):
        self.filename=self.file_name.get()#getting the filename based on what the user entered in the entry box for the file name
        if self.filename in os.listdir(self.foldername):#If the filename is found from the listdirecories, the program will get the file_name join the direcotry path
            with open(os.path.join(self.foldername, self.filename), 'r') as f:#The filename will be opened and read and confirmation message will be displayed.
                self.book= f.read()
            self.confirmation.config(text=f'{self.filename} is found!, click on refrsh to view book_details', fg="green")
        else:
            self.confirmation.config(text=f'{self.filename} is not listed!', fg="red")
            
    '''
    This function will search for the specified filename and will remove it from the list
    '''
    def delete(self):
        #self.foldername=self.folder_name.get()
        self.path=os.getcwd()#It will first get the current directory path
        self.filename=self.file_name.get()
        if self.filename in os.listdir(self.foldername):
            os.remove(f'{self.path}/{self.foldername}/{self.filename}')#The current_directory path will joined by the fodler_name and 
                                                                        #file_name for full path and then will be deleted.
            self.confirmation.config(text=f'{self.filename} successfully deleted!, click on search_files to view others', fg="blue")
        
    '''
    This function will first check if the specified path already exists, and then will check if the folder_name
    in the list of directories,and then will give a confirmation based on whether folder_name is found or not. And the searh_function will
    be used to search files in the folder.
    '''    
    def folder_books(self):
            self.foldername=self.folder_name.get()
            if os.path.isdir(self.foldername):
            
                  self.files = os.listdir(self.foldername)
                  self.confirmation.config(text=f'{self.foldername} found, now click search_files', fg="green")
            else:
                self.confirmation.config(text=f'{self.foldername} is not in our list, try again', fg="red")
                
            
    
    
    
    '''
    This function also called, search_files will not be cliked untill the foldername is found
    and the folder_search function confirms that the folder_name is found. Only then  can this function
    be used to open the the folder and view all the files in the folder which will
    be displayed in the listbox.
    '''          
    def refresh_list(self):
        self.listbox.delete(0, "end")
        if os.path.isdir(self.foldername):
            self.files = os.listdir(self.foldername)
            for file in self.files:
                self.listbox.insert("end", file.strip())
    """
    This function, also known as the search_book details function will not be used untill the search_book function confirms 
    whether there is a valid file that contains details or not. If the search_book function displays the message 
    confirming the existanace of the file, the button for this function can be clicked and view book details.
    """          
    def refresh(self):
        self.listbox.delete(0, "end")
        if self.filename in os.listdir(self.foldername):
            with open(os.path.join(self.foldername, self.filename), 'r') as f:
                self.book = f.read()
                self.listbox.insert("end", self.book.strip())

                
                

       

       
        
        
                


   