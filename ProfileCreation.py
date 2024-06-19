from tkinter import*
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import os
import os.path  
import tkinter.font as tkFont
import mysql.connector
from tkcalendar import DateEntry
import cv2
import tkinter as tk

class ProfileCreate:
    def __init__(self,old_window,new_window):
        #this is to store the prev window onto the variable
        self.main_window = old_window

        #to store the current window 
        self.ProfileCreate=new_window

        #setting the ui window size
        self.ProfileCreate.geometry("1280x720+0+0")
        self.ProfileCreate.title("Intelli Eye System")

        #  #set the window size
        new_window.resizable(False,False)
        new_window.attributes('-fullscreen', False)
        #set when the window close btn is click it will stop the app
        new_window.protocol("WM_DELETE_WINDOW", new_window.quit)

        #imagepath variable
        img_path = "D:/Downloads/Intelli Eye System/UI image"

        #===================UI variable======================
        #fontVariable
        btn_font = tkFont.Font(family="Orbitron", size=18,weight="bold")
        label_font=tkFont.Font(family="Orbitron", size=18)
        entry_font=tkFont.Font(family="Orbitron", size=16)
        cal_font=tkFont.Font(family="Orbitron", size=14)
        title_font=tkFont.Font(family="Orbitron", size=22,weight="bold")
        cb_font=tkFont.Font(family="Orbitron", size=16)

        #color variable
        top_blue="#000c32"
        mid_blue="#030f43"
        btm_blue="#03124d"
        white = "white"
        btn_color ="#f5684f"

        #criminal data variable
        self.var_Fname = StringVar()
        self.var_Lname = StringVar()
        self.var_Gender = StringVar()
        self.var_NRIC = StringVar()
        self.var_DOB = StringVar()
        self.var_Race = StringVar()
        self.var_Offenses = StringVar()
        #store multiple images path
        self.mugshot=[]
        self.fileIsSelect=False

         #====================UI related configuration n placement ==============================       

        #image for bg
        img=Image.open(os.path.join(img_path,"test2.jpg"))
        img=img.resize((1290,720),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.ProfileCreate, image=self.photoimg)
        #set positioning for img
        bg_img.place(x=0, y=0, width=1280, height=720)

        #label for title
        lblTitle=Label(bg_img,text="Create Criminal \nProfile ",font=title_font,bg=top_blue,fg=white)
        lblTitle.place(x=495, y=80,width=280,height=80)

        #criminal info
        #First Name
        FirstName_lbl=Label(bg_img,text="First Name",font=label_font,bg=mid_blue,fg=white)
        FirstName_lbl.place(x=150, y=205,width=195,height=30)

        FName_Entry=ttk.Entry(bg_img,width=15,font=entry_font,textvariable=self.var_Fname)
        FName_Entry.place(x=350, y=200,width=245,height=40)

         #Last Name
        LastName_lbl=Label(bg_img,text="Last Name",font=label_font,bg=mid_blue,fg=white)
        LastName_lbl.place(x=150, y=281,width=180,height=30)

        LName_Entry=ttk.Entry(bg_img,width=15,font=entry_font,textvariable=self.var_Lname)
        LName_Entry.place(x=350, y=276,width=245,height=40)
        
        #GEnder
        Gender_lbl=Label(bg_img,text="Gender",font=label_font,bg=btm_blue,fg=white)
        Gender_lbl.place(x=150, y=357,width=180,height=30)
        Gender_combo=ttk.Combobox(bg_img,font=cb_font,state="readonly",width=15,textvariable=self.var_Gender)
        Gender_combo["values"]=("Select Gender","Male","Female")
        Gender_combo.option_add('*TCombobox*Listbox*Font', ('Orbitron', 16))
        Gender_combo.current(0)
        Gender_combo.place(x=350, y=352,width=245,height=40)

        #NRIC
        NRIC_lbl=Label(bg_img,text="NRIC",font=label_font,bg=btm_blue,fg=white)
        NRIC_lbl.place(x=150, y=437,width=180,height=30)

        NRIC_Entry=ttk.Entry(bg_img,width=15,font=entry_font,textvariable=self.var_NRIC)
        NRIC_Entry.place(x=350, y=430,width=245,height=40)
        placeholder_text = "e.g: 000012340411"
        NRIC_Entry.insert(0, placeholder_text)

        # Bind the entry field to an event to remove the placeholder text when clicked
        def on_entry_click(event):
            if NRIC_Entry.get() == placeholder_text:
                NRIC_Entry.delete(0, tk.END)
        NRIC_Entry.bind("<Button-1>", on_entry_click)


        #DOB
        DOB_lbl=Label(bg_img,text="DOB",font=label_font,bg=top_blue,fg=white)
        DOB_lbl.place(x=620, y=205,width=150,height=30)

        DOB_Entry = DateEntry(bg_img, width=15, font=cal_font, textvariable=self.var_DOB, state="readonly")
        #chg calendar color
        DOB_Entry.configure(selectbackground="blue", selectforeground="white",  bordercolor= "blue",background="#00008B", foreground="#ededed",normalbackground="#add8e6", normalforeground="black")
        DOB_Entry.place(x=800, y=200, width=245, height=40)

        #Race
        Race_lbl=Label(bg_img,text="Race",font=label_font,bg=mid_blue,fg=white)
        Race_lbl.place(x=610, y=281,width=175,height=30)

        Race_combo=ttk.Combobox(bg_img,font=cb_font,state="readonly",width=15,textvariable=self.var_Race)
        Race_combo["values"]=("Select Race","Malay","Chinese","Indian","Orang Asli")
        Race_combo.option_add('*TCombobox*Listbox*Font', ('Orbitron', 16))
        Race_combo.current(0)
        Race_combo.place(x=800, y=275,width=245,height=40)

        #Criminal charges
        Offence_lbl=Label(bg_img,text="Offence",font=label_font,bg=btm_blue,fg=white)
        Offence_lbl.place(x=610, y=357,width=175,height=30)

        Offence_entry=ttk.Entry(bg_img,width=15,font=entry_font,textvariable=self.var_Offenses)
        Offence_entry.place(x=800, y=353,width=245,height=40)

        #mugshot btn
        mugshot_lbl=Label(bg_img,text="Mughsot",font=label_font,bg=btm_blue,fg=white)
        mugshot_lbl.place(x=610, y=425,width=175,height=40)

        Upphoto_btn=Button(bg_img,text="Upload", font=btn_font,bg="#059FFE", cursor="hand2", command=self.addMugshot ,fg=white)
        Upphoto_btn.place(x=800,y=426,width=140,height=40)

          #cancel btn 
        cancel_btn=Button(bg_img,text="Cancel", font=btn_font, cursor="hand2", command=self.onCancelPressed, bg=btn_color,fg=white)
        cancel_btn.place(x=440,y=525,width=140,height=40)

        #create btn 
        create_btn=Button(bg_img,text="Create", font=btn_font,cursor="hand2",command=self.add_Criminal, bg=btn_color,fg=white)
        create_btn.place(x=690,y=525,width=140,height=40)

    #Moving back
    def onCancelPressed(self):
        # destroy current window
        self.ProfileCreate.destroy()
        # unhide old window
        self.main_window.deiconify()
        
    
    #when the window close btn is clicked, the root will destroy
    def quit(self):
        self.main_window.destroy()
    
    #for selecting image when btn clik 
    def addMugshot(self):
        #select more than 1 file
        files = filedialog.askopenfilenames(
            title="Select Images", 
            filetypes=( 
            ("JPEG files", "*.jpg"),
            ("PNG files", "*.png"),
            ("SVG files", "*.svg*")
            )
        )
        
        # Store the selected image file paths as a list in a class variable
        if len(files) > 0:
            self.mugshot= ';'.join(list(files))
            #set to true for when a file is selected else false
            self.fileIsSelect =TRUE

       
    def add_Criminal(self):

        loading_font =tkFont.Font(size=11)

        #================mysql database connnection==============
        #set connection to the db
        conn = mysql.connector.connect(host="localhost",username="root",password="admin",database="face_recog")
        #create a cursor object to interact with the database
        mycursor = conn.cursor()

        # Retrieve all NRIC data from the database
        mycursor.execute("SELECT Nric FROM criminal_info")
        rows = mycursor.fetchall()
        
        #chck if the all entry is valid if not prompt error 
        if check_fields(self.var_Gender.get(), self.var_Fname.get(), self.var_Lname.get(), self.var_DOB.get(), self.var_Race.get(), self.var_NRIC.get(), self.var_Offenses.get()):
             #show prompt error
             messagebox.showerror("Error", "All Fields are required", parent=self.ProfileCreate)
         #check if the field is input     
        elif (is_alpha(self.var_Fname.get())== False): 
             #show error
             messagebox.showwarning("Attention", "Please enter only alphabets in first name field.")
        elif (is_alpha(self.var_Lname.get())== False): 
             #show error
             messagebox.showwarning("Attention", "Please enter only alphabets in last name field.")
        elif (is_alpha(self.var_Offenses.get())== False): 
             #show error
             messagebox.showwarning("Attention", "Please enter only alphabets in offense field.")
        elif(is_numeric(self.var_DOB.get())== False):
              #show error
             messagebox.showwarning("Attention", "Please enter only numerical value for DOB field")
        elif (self.var_NRIC.get() == "e.g: 000012340411"):
              #show error
             messagebox.showwarning("Attention", "NRIC field is empty.")
        elif (is_numeric(self.var_NRIC.get()) == False):
              #show error
             messagebox.showwarning("Attention", "Please enter only numerical value for NRIC field.")
        elif (len(self.var_NRIC.get()) != 12):
             #show error
             messagebox.showwarning("Attention", "Please ensure there is 12 digit NRIC field.")
        elif( self.fileIsSelect==False):
             messagebox.showwarning("Attention", "Please upload mugshot images")
        #check if there is trailing or leading whitespace
        elif self.var_Fname.get().strip() != self.var_Fname.get():
            messagebox.showwarning("Attention", "Please remove leading or trailing whitespace in the first name fields")
        elif self.var_Lname.get().strip() != self.var_Lname.get():
            messagebox.showwarning("Attention", "Please remove leading or trailing whitespace in the last name fields")
        elif self.var_Offenses.get().strip() != self.var_Offenses.get(): 
            messagebox.showwarning("Attention", "Please remove leading or trailing whitespace in the offense fields")
        elif self.var_NRIC.get().strip() != self.var_NRIC.get(): 
            messagebox.showwarning("Attention", "Please remove leading or trailing whitespace in the nric fields")
        #check for duplicated nric
        # Check if the input NRIC matches any existing NRIC in the database
        elif any(row[0] == self.var_NRIC.get() for row in rows):
            messagebox.showerror("Error", "NRIC already exists in the database")
        else:
            
            #=======Check if img has face if no wont update db==========

            has_faces = True #flag for checking if all img has face
            total_images = 0
            all_img_perfect = 0  #  count the total num of img that has faces


            # Split the mugshot paths into separate image paths
            mugshot_paths = self.mugshot.split(";")
            total_images += len(mugshot_paths)#count total img of the criminal

            #==========Loading widgets===========
            loading_window1 = tk.Toplevel()
            loading_window1.title("Image face checking")
            loading_window1.geometry("400x100+450+320")
            loading_window1.resizable(False, False)
            
            progress_var = tk.DoubleVar()
            progress_var.set(0)
            # Create a custom style for the Progressbar
            style = ttk.Style()
            style.configure("Custom.Horizontal.TProgressbar",
                                        troughcolor='#e6e6e6',  # Set the color of the progress bar background
                                        background='#06b025',   # Set the color of the progress bar itself
                                        )

            progress_bar = ttk.Progressbar(loading_window1, variable=progress_var, maximum=total_images,style="Custom.Horizontal.TProgressbar")
            progress_bar.pack(fill="x", padx=10, pady=10)


            status_label = tk.Label(loading_window1, text="Checking each image for clear face...",font=loading_font)
            status_label.pack(pady=5)
                                
            loading_window1.update()
            #==================================

            progress_counter = 0  # Counter for tracking progress used in loading

            # Iterate over each image path
            for mugshot_path in mugshot_paths:
                if mugshot_path.strip() != "":
                    try:
                        # Load the image
                        img = cv2.imread(mugshot_path)
                        if img is None:
                            raise ValueError(f"Failed to read image file: {mugshot_path}")
                        
                        # Convert to grayscale
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


                        # Detect faces in the image
                        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
                        
                        if len(faces) == 0: #detect if the face is present in each img
                            # If no faces are detected, reject the image
                            messagebox.showerror("Error", f"No face detected in {mugshot_path}")
                            has_faces = False 
                            break
                        else:
                            has_faces =True
                            all_img_perfect += 1
                            # Update progress counter
                            progress_counter += 1
                            # Update progress bar
                            progress_var.set(progress_counter)
                            loading_window1.update()
                            pass

                    except Exception as e:
                        # Display error message
                        messagebox.showerror("Error", f"Error processing image {mugshot_path}: {str(e)}")

            # update progress bar and status
            progress_var.set(total_images)
            status_label.config(text="Face checking completed.",font=loading_font)
            loading_window1.update()
            loading_window1.destroy()

            try:
                if has_faces == True and all_img_perfect >=10:
                    mycursor.execute("insert into criminal_info (Fname, Lname, Gender, Race, Nric, Dob, Offenses, Mugshot) values(%s, %s, %s,%s, %s, %s,%s,%s)",(
                        self.var_Fname.get(),self.var_Lname.get(), self.var_Gender.get(), self.var_Race.get(), self.var_NRIC.get(), self.var_DOB.get(), self.var_Offenses.get(),self.mugshot
                    ))
                    #make changes to db
                    conn.commit()  
                    mycursor.fetchall()  # Discard the result of the previous query

                    # Retrieve the CID of the new criminal profile
                    mycursor.execute("SELECT cid FROM criminal_info WHERE gender=%s AND nric =%s", (self.var_Gender.get(),self.var_NRIC.get()))
                    row = mycursor.fetchone()
                    mycursor.fetchall()  # Discard the result of the previous query

                    if row is not None:
                        cid = row[0]
                    else:
                        raise ValueError("Failed to retrieve CID of new criminal profile")
                    
                    #for converting image into greyscale 
                    mycursor.execute("SELECT mugshot FROM criminal_info WHERE cid=%s", (cid,))
                    rows = mycursor.fetchall() #select all the enrollment img

                    img_id = 0
                    face_paths = []
                    # Folder whr it should store
                    folder_path = "D:/Downloads/Intelli Eye System/Mugshots/test"
                     # Face detection cascade classifier
                    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    # Create the output folder if it doesn't exist
                    output_folder_path = os.path.join(folder_path, 'faces')
                    os.makedirs(output_folder_path, exist_ok=True)
                    total_images = 0
                
                    #to get the total number of image 
                    for row in rows:
                        # Split the row into separate image paths and get the total img
                        mugshot_paths = row[0].split(";")
                        total_images += len(mugshot_paths)#count total img of the criminal

                    #==========Loading widgets===========
                    loading_window = tk.Toplevel()
                    loading_window.title("Grayscale image conversion")
                    loading_window.geometry("400x100+450+320")
                    loading_window.resizable(False, False)

                    progress_var = tk.DoubleVar()
                    progress_var.set(0)

                    # Create a custom style for the Progressbar
                    style = ttk.Style()
                    style.configure("Custom.Horizontal.TProgressbar",
                                            troughcolor='#e6e6e6',  # Set the color of the progress bar background
                                            background='#06b025',   # Set the color of the progress bar itself
                                            )

                    progress_bar = ttk.Progressbar(loading_window, variable=progress_var, maximum=total_images,style="Custom.Horizontal.TProgressbar")
                    progress_bar.pack(fill="x", padx=20, pady=10)


                    status_label = tk.Label(loading_window, text="Image conversion in progress...",font=loading_font)
                    status_label.pack(pady=5)
                    

                    loading_window.update()
                    #==================================

                    progress_counter = 0  # Counter for tracking progress used in loading

                    for row in rows:
                        # Split the row into separate image paths
                        mugshot_paths = row[0].split(";")
                        row_face_paths = []

                        
                        # Loop through each image path 
                        for mugshot_path in mugshot_paths:
                            filename = os.path.basename(mugshot_path)
                            if filename.endswith(".jpg") or filename.endswith(".png"):
                                try:
                                    # Load the image
                                    img = cv2.imread(mugshot_path)
                                    print("Loaded image from:", mugshot_path)

                                    if img is None:
                                        raise ValueError(f"Failed to read image file: {mugshot_path}")

                                    # Convert to grayscale
                                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                                    # Detect faces in the image
                                    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

                                    # Update progress counter
                                    progress_counter += 1

                                    # Update progress bar
                                    progress_var.set(progress_counter)
                                    loading_window.update()

                                    
                                    # Extract faces and save as new images
                                    for (x, y, w, h) in faces:
                                        face = gray[y:y+h, x:x+w]
                                        face_filename = f"CID_{cid}_{img_id}_gray.jpg"#images will be saved as CID_?_?
                                        face_path = os.path.join(output_folder_path, face_filename)
                                        cv2.imwrite(face_path, face)
                                        img_id += 1
                                        face_paths.append(face_path)  # Append the current face path to the list of all face paths
                                        row_face_paths.append(face_path)  # Append the current face path to the list of face paths for the current row
                                        
                                    # Display success message for each images
                                    #messagebox.showinfo("Success", f"Faces detected in {filename}")
                                except Exception as e:
                                    # Display error message
                                    messagebox.showerror("Error", f"Error detecting faces in {filename}: {str(e)}")
                                 # Update the database with the face paths for the current row
                            mycursor.execute("UPDATE criminal_info SET mugshot=%s WHERE cid=%s", (";".join(row_face_paths), cid))
                        mycursor.execute("UPDATE criminal_info SET mugshot=%s WHERE cid=%s", (";".join(face_paths), cid))#update the database with the latest poto

                    # Commit changes and close the database connection
                    conn.commit()
                    conn.close()

                    # update progress bar and status
                    progress_var.set(total_images)
                    status_label.config(text="Image conversion completed.",font=loading_font)
                    loading_window.update()
                    loading_window.destroy()

                    messagebox.showinfo("Success", "Criminal details has successfully been added and all images has been normalised and converted into grayscale.", parent=self.ProfileCreate)

                    #move back to prev page
                    # destroy current window
                    self.ProfileCreate.destroy()
                    # unhide old window
                    self.main_window.deiconify()
                elif has_faces == FALSE:
                    messagebox.showerror("Error", "Database not updated please input images that has clear faces.")
                elif all_img_perfect < 10:
                    messagebox.showerror("Error", "Database not updated, system requires a minumum of 10 images.")
                else:
                    messagebox.showerror("Error", "Database not updated please try again.")
                    
            except Exception as es:
                #error for dev to see
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.ProfileCreate)
         
#check if the entry field is empty 
def check_fields(*args):
    for field in args:
        if not field.strip() or field == "Select Gender" or field == "Select Race":
            return True
    return False     

#Returns True if entry_text contains only alphabetical characters
def is_alpha(entry_text):
    return all(c.isalpha() or c.isspace() or c == ',' for c in entry_text)

#Returns True if entry_text contains only numeric characters or contain "/"
def is_numeric(entry_text):
    return all(char.isdigit() or char == "/" for char in entry_text)



        
