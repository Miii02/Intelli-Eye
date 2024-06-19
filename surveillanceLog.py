from tkinter import*
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import os
import os.path  
import tkinter.font as tkFont
import csv
import fileinput
#for listing out info based on csv
mydata=[]

class surveillance_Log:
    def __init__(self,old_window,new_window):
        #this is to store the prev window onto the variable
        self.main_window = old_window

        #to store the current window 
        self.surveillanceLog=new_window
        
        #setting the ui window size
        self.surveillanceLog.geometry("1280x720+0+0")
        self.surveillanceLog.title("Intelli Eye System")
        
        #set the window size
        new_window.resizable(False,False)
        new_window.attributes('-fullscreen', False)
        #set when the window close btn is click it will stop the app
        new_window.protocol("WM_DELETE_WINDOW", new_window.quit)


         #imagepath variable
        img_path = "D:/Downloads/Intelli Eye System/UI image"

        #gui color
        white = "white"
        btn_color ="#f5684f"

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

        bg_img=Label(self.surveillanceLog, image=self.photoimg)
        #set positioning for img
        bg_img.place(x=0, y=0, width=1280, height=720)

        #label for title
        lblTitle=Label(bg_img,text="Surveillance Log",font=title_font,bg="#000c32",fg="white")
        lblTitle.place(x=500, y=80,width=290,height=40)

        #for the back icon
        imgBack=Image.open(os.path.join(img_path,"previous.png"))
        imgBack=imgBack.resize((50,50),Image.LANCZOS)
        self.photoimgBk=ImageTk.PhotoImage(imgBack)

        btnBack=Button(bg_img,image=self.photoimgBk,cursor="hand2",command=self.onBackPressed ,border=0,bg="#003f9f")
        btnBack.place(x=0,y=0,width=50,height=50)

        #import btn 
        import_btn=Button(bg_img,text="Import CSV", font=btn_font, cursor="hand2", command=self.importCsv, bg=btn_color,fg=white)
        import_btn.place(x=440,y=590,width=180,height=40)

        #export btn 
        export_btn=Button(bg_img,text="Export CSV", font=btn_font,cursor="hand2",command=self.exportCsv, bg=btn_color,fg=white)
        export_btn.place(x=660,y=590,width=180,height=40)

         #==============Table frame for listing criminals ===============

        table_frame = Frame(bg_img,bd=2,bg="white",relief=RIDGE,borderwidth=1)
        table_frame.place(x=30,y=120,width=1215,height=460)

        scroll_x =ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y =ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.surveillanceTable=ttk.Treeview(table_frame,columns=("CID","FName","LName", "offense","time","date","latitude","longtitude", "confidence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set, selectmode='none')
 
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.surveillanceTable.xview)
        scroll_y.config(command=self.surveillanceTable.yview)

        #==========heading for the table column==========

        #to chg the style of the heading
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font= ("Orbitron",13,"bold"))
        style.configure("Treeview", font= ("Arial",12), background="white")

        style.map('Treeview', background=[('selected','#00e0f7')])

        self.surveillanceTable.heading("CID",text="Criminal ID")
        self.surveillanceTable.column("CID", minwidth=110, width=40, anchor=CENTER)
        self.surveillanceTable.heading("FName",text="First Name")
        self.surveillanceTable.column("FName", minwidth=115, width=100, anchor=CENTER)
        self.surveillanceTable.heading("LName",text="Last Name")
        self.surveillanceTable.column("LName", minwidth=115, width=100,anchor=CENTER)
        self.surveillanceTable.heading("offense",text="Offense")
        self.surveillanceTable.column("offense", minwidth=160, width=120,anchor=CENTER)
        self.surveillanceTable.heading("time",text="Time")
        self.surveillanceTable.column("time", minwidth=80, width=60,anchor=CENTER)
        self.surveillanceTable.heading("date",text="Date")
        self.surveillanceTable.column("date", minwidth=95, width=50,anchor=CENTER)
        self.surveillanceTable.heading("latitude",text="Latitude")
        self.surveillanceTable.column("latitude", minwidth=80, width=60,anchor=CENTER)
        self.surveillanceTable.heading("longtitude",text="Longtitude")
        self.surveillanceTable.column("longtitude", minwidth=80, width=60,anchor=CENTER)
        self.surveillanceTable.heading("confidence",text="Similarity")
        self.surveillanceTable.column("confidence", minwidth=80, width=60,anchor=CENTER)
        self.surveillanceTable["show"]="headings"
        self.surveillanceTable.pack(fill=BOTH,expand=1)

        
        #to bind the onclick function when the user is clicked in the list
        #self.surveillanceTable.bind("<ButtonRelease-1>", self.handle_treeview_selection)

        self.defaultCSV()#to automatically display the default csv

        #=====================================

    def fetchData(self ,rows):
        self.surveillanceTable.delete(*self.surveillanceTable.get_children())
        for i in rows:
            self.surveillanceTable.insert("", END,values=i)

    # automatically display its default csv
    def defaultCSV(self):
        global mydata,fln
        #clear prev data in treeview
        mydata.clear()
        #default file location n name
       
        fln="D:/Downloads/Intelli Eye System/CriminalLog.csv"
        # check if file exists
        if os.path.isfile(fln):
            pass
        else:
            #file does not exist, create it
            with open(fln, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)

        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=";")
            for i in csvread:
                # Remove leading/trailing whitespace from full name
                name = i[1].strip()
                # Split full name into first name and last name
                name_parts = name.split(" ")
                # Replace full name with first name and last name in the data list
                if len(name_parts) == 2:
                    fname, lname = name_parts
                    # is used to add an xtra index so that longtitude can be insert into it
                    i.append("")
                    # Replace full name with first name and last name in the data list
                    i[1], i[2], i[3],i[4], i[5], i[6], i[7] ,i[8]= fname, lname, i[2], i[3], i[4], i[5], i[6] , i[7]
                mydata.append(i)
            self.fetchData(mydata)

    # function for importing the csv
    def importCsv(self):
        
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"),("ALL File","*.*")), parent=self.surveillanceLog)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=";")
            for i in csvread:
                # Remove leading/trailing whitespace from full name
                name = i[1].strip()
                # Split full name into first name and last name
                name_parts = name.split(" ")
                # Replace full name with first name and last name in the data list
                if len(name_parts) == 2:
                    fname, lname = name_parts
                    # is used to add an xtra index so that longtitude can be insert into it
                    i.append("")
                    # Replace full name with first name and last name in the data list
                    i[1], i[2], i[3],i[4], i[5], i[6], i[7] , i[8]= fname, lname, i[2], i[3], i[4], i[5], i[6], i[7]
                mydata.append(i)
            self.fetchData(mydata)

    # function for exporting csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No data found to export",parent=self.surveillanceLog)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV File", "*.csv"),("ALL File","*.*")),parent=self.surveillanceLog, defaultextension='.csv')
            if fln: # Check if file name is not empty (user clicked "Save")    
                with open(fln,mode="w", newline="")as myfile:
                    exp_write=csv.writer(myfile,delimiter=";")
                    for i in mydata:
                        exp_write.writerow(i)
                    messagebox.showinfo("Data Export", "Your data has been successfully exported to "+os.path.basename(fln))
        except Exception as es:
            messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.surveillanceLog)    

   

    def onBackPressed(self):
        # destroy current window
        self.surveillanceLog.destroy()
        # unhide old window
        self.main_window.deiconify()

    #when the window close btn is clicked, the root will destroy
    def quit(self):
        self.main_window.destroy()

     #-------Cursor for selecting the user#
    #need edit here for updating 
    def handle_treeview_selection(self, event):
        # Get the selected item ID and text
        item_id = self.surveillanceTable.focus()
        # based on the selected row it will return the CID where the user clicked
        item_text = self.surveillanceTable.item(item_id, "values")[0]
        item_text_time = self.surveillanceTable.item(item_id, "values")[4]
        

        # Prompt the user to edit the selected item

        answer = messagebox.askyesno("Delete Item", f"Do you want to delete '{item_text}' at time '{item_text_time}'?")

        if answer: #yes
            
            # Get the current value of the selected item
            CID = int(self.surveillanceTable.item(item_id,"values")[0])#get the CID from the user click value
            time = self.surveillanceTable.item(item_id,"values")[4]#get the time value from the user click 

            # Delete the selected row from the TreeView
            self.surveillanceTable.delete(item_id)
            # Delete the selected row from the CSV file
            with fileinput.FileInput(fln, inplace=True) as f:
                for line in f:
                    line_CID = int(line.split(';')[0])
                    line_time = line.split(';')[4]
                    if CID == line_CID and time == line_time:
                        continue
                    print(line.strip(), end='')
            messagebox.showinfo("Deleted", f"The CID of '{item_text}' at time '{item_text_time} ' has been deleted.")
#delete the row of data based on time and cid is successful


#stop at part 9
# havent populate the new log page yet 
# or i shud jz let them delete it so no need edit
