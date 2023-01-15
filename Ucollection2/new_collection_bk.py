from tkinter import *
from tkinter import Tk
import os
import tkinter as tk



class new_collection_window(tk.Toplevel):
        def __init__(self, main):
            '''
            The following variable are about defination and globalising so they can be accessed in different fucntions in this class
            and in other modules.
            '''
            
            global author
            global note
            global filepass
            global file_name
            global folder_name
            self.target_path=None
            global filepass
            self.complete_dir=None
            self.book_n = None
            self.book = None
            self.author_n=None
            self.note_n=None
            self.notification=None
            self.book_n=StringVar()#Defining the variable as an stringvariable, when entered as textvariable in the Entry Box .
            self.author_n=StringVar()#Defining the variable as an stringvariable, when entered as textvariable in the Entry Box .
            self.note_n=StringVar()#Defining the variable as an stringvariable, when entered as textvariable in the Entry Box .
            self.file_name=StringVar()#Defining the variable as an stringvariable, when entered as textvariable in the Entry Box .
            self.folder_name=StringVar()#Defining the variable as an stringvariable, when entered as textvariable in the Entry Box .
   
    
            new_collection_window=Toplevel(main)#Introducting toplevel window, which will create separate window for this module from the main_window.
            new_collection_window.config(bg="#5F9DF7")
            new_collection_window.title("New_Collection_Page")
            
            
    
            '''
            following are all Labels: widgets that can be used to make text/s displayed on the window. You can specify, text color,
            font/size, background color, and the posotions(row/column numbers). Grid()/pack() are used for positioning. 
            For absolute positioning, grid() is better and that's why I have used it.
            '''
            self.ti=Label(new_collection_window, text="Start Your Reading Journey by Listing Your Books Here", fg="#FF1E1E", bg="#009EFF",font=('Calibri', 12))
            self.ti.grid(row=0, sticky=W, pady=10)
            self.bon= Label(new_collection_window, text="Book_Name", fg="#FF1E1E", bg="#009EFF", font=('Calibri', 12))
            self.bon.grid(row=1, sticky=W, pady=20)
            self.an= Label(new_collection_window, text="Author",  fg="#FF1E1E",bg="#009EFF", font=('Calibri', 12))
            self.an.grid(row=2, sticky=W, pady=20)
            self.n=Label(new_collection_window, text="Your NOTE", fg="#FF1E1E", bg="#009EFF",font=('Calibri',12))
            self.n.grid(row=3, pady=20, sticky=W )
            self.fn=Label(new_collection_window, text="Folder Name", fg="#FF1E1E", bg="#009EFF", font=('Calibri', 12))
            self.fn.grid(row=4, pady=20, sticky=W )
            self.fin=Label(new_collection_window, text="File Name", fg="#FF1E1E", bg="#009EFF", font=('Calibri', 12))
            self.fin.grid(row=6, pady=20, sticky=W )
            self.confirmation=Label(new_collection_window, font=('Calibri', 12))
            self.confirmation.grid(row=12, sticky=N, pady=10)
    
    
    
            '''
             #Entries/inputs: as the name implies, they are Entry boxes, and the entry values they recieve are called
             textvariables. The value of the text_variable is used by the functions as input values.
            '''
    
            
            self.bn=Entry(new_collection_window, textvariable=self.book_n).grid(row=1, column=0)
            self.ae=Entry(new_collection_window, textvariable=self.author_n).grid(row=2, column=0)
            self.ne=Entry(new_collection_window, textvariable=self.note_n, width=20).grid(row=3, column=0)
            self.foe=Entry(new_collection_window,textvariable=self.folder_name, width=20 ).grid(row=4, column=0)
            self.fie=Entry(new_collection_window,textvariable=self.file_name, width=20 ).grid(row=6, column=0)
            
        
            '''
            Button: Buttons are the commanding points of the functions, when clicked, based on the instructions given, it outputs.
            '''
            self.bfolder=Button(new_collection_window, text="Create_Folder", font=('Calibri', 12), command=self.get_folder_name, width=10)
            self.bfolder.grid(row=5, column=0, sticky=N, pady=5, padx=5)
            self.bfile=Button(new_collection_window, text="Create_File", font=('Calibri', 12), command=self.get_file_txt, width=10)
            self.bfile.grid(row=7, column=0, sticky=N, pady=5, padx=5)
            
        
        
        '''
        The following function, get_folder_name is commaned by (command=self.get_folder_name)button, and when clicked 
        will create a folder to the desginated directoty path. So the folder we ill be under the parent directory.
        if entry box is empty: it will display: "folder field is required", if filled: "successfully created folder".
        '''
        def get_folder_name(self):
            self.folderpass=self.folder_name.get()
            parent_directory='/home/abas/Ucollection2'
            path=os.path.join(parent_directory, self.folderpass)#This uses the os.path.join method, which will help folder to join 
                                                                #the directory path of the  parent directory.
            
            self.target_path=self.folderpass#The self.target_path is useful when creating the file and want to know the specific folder to which the file should be saved.
            all_folders=os.listdir()#List of all directories in the current directory.
            if self.folderpass=="":
                self.confirmation.config(fg="red", bg="#00E7FF", text="Folder_filed is required")
                return
                
            if self.folderpass in all_folders:
                path=os.path.join(parent_directory, self.folderpass)
            else:
                os.mkdir(path)
            
            self.confirmation.config(fg="green", text="Successfully created folder")
            
            
            
        '''
        The following function(get_file_txt) is the function that's commanded by {command=self.get_file_txt} button,
        and if clicked, the user will create a file. If the box for the file is empty, but clicked, the user will get notification: "fieds are required",
        this includes the book_name, note_name and author_name boxes. If all the fields are filled. teh user will confirmation message:
        "You have successfully created your collection".
        '''
        def get_file_txt(self): #get file
            self.filepass=self.file_name.get()#the textvariable value of the folder entry box: Whatever the user puts in that box will be accessed 
                                                                                    #by this function as input value
            self.complete_dir = os.path.join(self.target_path, self.filepass+".txt")#This line uses Os.path.join, which helps the foldername, and filename to join 
                                                                                                    #the path directory of the operating system.
                                                                                                    #In this case, self.target_path represets, the folder created
                                                                                                    #by the user.
            self.book=self.book_n.get()#textvariable input of book name box: the value user inputs will be accessed an input by this function
            self.author=self.author_n.get() #''
            self.note=self.note_n.get()  #''
            file1 = open(self.complete_dir, "w")#This will open file in the os.path.join directory path and write book_name, author_name_note: So the file will contain
                                                                            #the the information the user enters in the entry boxes of (book, author, note)
            file1.write(self.book + "\n")
            file1.write(self.author+ "\n" )
            file1.write(self.note+ "\n" )
            file1.close()
            if self.book=="" or self.author=="":
                self.confirmation.config(fg="red", bg="#00E7FF", text="Fields required *")#If entery boxes are empty
                return
            self.confirmation.config(fg="green", bg="#00E7FF", text="You have successfully created your collection")#If entry boxes are filled
           
    