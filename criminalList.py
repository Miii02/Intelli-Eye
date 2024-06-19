from tkinter import*
from tkinter import ttk, messagebox, simpledialog
from PIL import Image, ImageTk
from ProfileCreation import ProfileCreate
from criminal_info import Criminal_info
import os
import os.path  
import tkinter.font as tkFont
import mysql.connector



class Criminal_Listing:
    def __init__(self,old_window,new_window):
        #this is to store the prev window onto the variable
        self.main_window = old_window

        #to store the current window 
        self.CriminalList=new_window
        
        #setting the ui window size
        self.CriminalList.geometry("1280x720+0+0")
        self.CriminalList.title("Intelli Eye System")
        
        #set the window size
        new_window.resizable(False,False)
        new_window.attributes('-fullscreen', False)
        #set when the window close btn is click it will stop the app
        new_window.protocol("WM_DELETE_WINDOW", new_window.quit)


         #imagepath variable
        img_path = "D:/Downloads/Intelli Eye System/UI image"

        #=====================UI variable==============================
        #fontVariable
        btn_font = tkFont.Font(family="Orbitron", size=18,weight="bold")
        list_font=tkFont.Font(family="Orbitron", size=12)
        title_font=tkFont.Font(family="Orbitron", size=22,weight="bold")

        #====================UI confi and placement ==================
        #image for bg
        img=Image.open(os.path.join(img_path,"test2.jpg"))
        img=img.resize((1290,720),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.CriminalList, image=self.photoimg)
        #set positioning for img
        bg_img.place(x=0, y=0, width=1280, height=720)

        #label for title
        lblTitle=Label(bg_img,text="Criminal Lists",font=title_font,bg="#000c32",fg="white")
        lblTitle.place(x=515, y=80,width=245,height=40)

        #for the back icon
        imgBack=Image.open(os.path.join(img_path,"previous.png"))
        imgBack=imgBack.resize((50,50),Image.LANCZOS)
        self.photoimgBk=ImageTk.PhotoImage(imgBack)

        btnBack=Button(bg_img,image=self.photoimgBk,cursor="hand2",command=self.onBackPressed ,border=0,bg="#003f9f")
        btnBack.place(x=0,y=0,width=50,height=50)

        #add criminal btn 
        create_btn=Button(bg_img,text="Create", font=btn_font, cursor="hand2",command=self.CreatePage ,bg="#f5684f",fg="white")
        create_btn.place(x=575,y=595,width=140,height=40)

        #for refresh btn
        imgRefresh=Image.open(os.path.join(img_path,"refresh.png"))
        imgRefresh=imgRefresh.resize((50,50),Image.LANCZOS)
        self.photoRefresh=ImageTk.PhotoImage(imgRefresh)
        
        
        #==============Table frame for listing criminals ===============

        table_frame = Frame(bg_img,bd=2,bg="white",relief=RIDGE,borderwidth=1)
        table_frame.place(x=30,y=120,width=1215,height=460)

        scroll_x =ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y =ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminalTable=ttk.Treeview(table_frame,columns=("CID","FName","LName", "gender","race","nric","dob","offenses"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set, selectmode='browse')
 
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.criminalTable.xview)
        scroll_y.config(command=self.criminalTable.yview)

        #==========heading for the table column==========

        #to chg the style of the heading
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font= ("Orbitron",13,"bold"))
        style.configure("Treeview", font= ("Arial",12), background="white")

        style.map('Treeview', background=[('selected','#00e0f7')])

        self.criminalTable.heading("CID",text="Criminal ID")
        self.criminalTable.column("CID", minwidth=110, width=90, anchor=CENTER)
        self.criminalTable.heading("FName",text="First Name")
        self.criminalTable.column("FName", minwidth=115, width=100, anchor=CENTER)
        self.criminalTable.heading("LName",text="Last Name")
        self.criminalTable.column("LName", minwidth=115, width=100,anchor=CENTER)
        self.criminalTable.heading("gender",text="Gender",)
        self.criminalTable.column("gender", minwidth=90, width=40,anchor=CENTER)
        self.criminalTable.heading("race",text="Race")
        self.criminalTable.column("race", minwidth=115, width=90,anchor=CENTER)
        self.criminalTable.heading("nric",text="NRIC")
        self.criminalTable.column("nric", minwidth=160, width=120,anchor=CENTER)
        self.criminalTable.heading("dob",text="DOB")
        self.criminalTable.column("dob", minwidth=80, width=60,anchor=CENTER)
        self.criminalTable.heading("offenses",text="Offenses")
        self.criminalTable.column("offenses", minwidth=150, width=150,anchor=CENTER)
        self.criminalTable["show"]="headings"
        self.criminalTable.pack(fill=BOTH,expand=1)
        self.fetch_data()

        #for refreshing the table list 
        btnRefresh=Button(bg_img,image=self.photoRefresh,cursor="hand2",command=self.fetch_data ,border=0,bg="#003f9f")
        btnRefresh.place(x=1200,y=70,width=50,height=50)

        #to bind the onclick function when the user is clicked in the list
        self.criminalTable.bind("<ButtonRelease-1>", self.handle_treeview_selection)

        #===============================================================

    def onBackPressed(self):
        # destroy current window
        self.CriminalList.destroy()
        # unhide old window
        self.main_window.deiconify()

    #when the window close btn is clicked, the root will destroy
    def quit(self):
        self.main_window.destroy()
    
    def CreatePage(self):
        #hide current window
        self.CriminalList.withdraw()
        #create new window
        self.new_window=Toplevel(self.CriminalList)
        self.app=ProfileCreate(self.CriminalList, self.new_window)

#---------------Fetching data from database#
    def fetch_data(self):
         #set connection to the db
        conn = mysql.connector.connect(host="localhost",username="root",password="admin",database="face_recog")
        #create a cursor object to interact with the database
        mycursor = conn.cursor()
        mycursor.execute("Select * from criminal_info")
        data = mycursor.fetchall()
        
        if len (data)!=0:
                self.criminalTable.delete(*self.criminalTable.get_children())
                for i in data:
                     self.criminalTable.insert("", END, i[0], text=f"CID {i[0]}",values=i)
                conn.commit()
        conn.close()
    
    #-------Cursor for selecting the user#
    #need edit here for updating 
    def handle_treeview_selection(self, event):
        # Get the selected item ID and text
        item_id = self.criminalTable.focus()
        #based on the selected row it will return the CID 
        item_text = self.criminalTable.item(item_id, "text")

        # Prompt the user to edit the selected item
        answer = messagebox.askyesno("Edit Item", f"Do you want to edit '{item_text}'?")

        if answer: #yes
            
            # Get the current value of the selected item
            CID = self.criminalTable.item(item_id, "text")
            #hide current window
            self.CriminalList.withdraw()
            #create new window
            self.new_window=Toplevel(self.CriminalList)
            self.app=Criminal_info(self.CriminalList, self.new_window, CID)


  
        
