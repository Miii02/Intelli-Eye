from tkinter import*
from tkinter import ttk,filedialog,messagebox
from PIL import Image, ImageTk
import tkinter.font as tkFont
import os
import os.path  
import mysql.connector
from tkcalendar import DateEntry
import cv2
import tkinter as tk


class Criminal_info:
    def __init__(self,old_window,new_window, CID):
       
        #this is to store the prev window onto the variable
        self.main_window = old_window

        #to store the current window 
        self.Criminal_info=new_window
        
        #to store the CID pass from Criminal list argument
        self.CID = CID
       
        #setting the ui window size
        self.Criminal_info.geometry("1280x720+0+0")
        self.Criminal_info.title("Intelli Eye System")

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
        btn_font2 = tkFont.Font(family="Orbitron", size=16,weight="bold")
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

        bg_img=Label(self.Criminal_info, image=self.photoimg)
        #set positioning for img
        bg_img.place(x=0, y=0, width=1280, height=720)

        #label for title
        lblTitle=Label(bg_img,text="Edit Criminal Profile ",font=title_font,bg=top_blue,fg=white)
        lblTitle.place(x=485, y=80,width=320,height=70)

        #criminal info

        #image of the criminal
        self.Mushot_Disp_position=Label(self.Criminal_info,bg="red")
        self.Mushot_Disp_position.place(x=300, y=160, width=215, height=215)

        #First Name
        FirstName_lbl=Label(bg_img,text="First Name",font=label_font,bg=top_blue,fg=white)
        FirstName_lbl.place(x=525, y=160,width=195,height=30)

        FName_Entry=ttk.Entry(bg_img,width=15,font=entry_font,textvariable=self.var_Fname)
        FName_Entry.place(x=740, y=156,width=245,height=40)

        #Last Name
        LastName_lbl=Label(bg_img,text="Last Name",font=label_font,bg=top_blue,fg=white)
        LastName_lbl.place(x=532, y=230,width=180,height=30)

        LName_Entry=ttk.Entry(bg_img,width=15,font=entry_font,textvariable=self.var_Lname)
        LName_Entry.place(x=740, y=226,width=245,height=40)

        #GEnder
        Gender_lbl=Label(bg_img,text="Gender",font=label_font,bg=mid_blue,fg=white)
        Gender_lbl.place(x=525, y=300,width=180,height=30)
        Gender_combo=ttk.Combobox(bg_img,font=cb_font,state="readonly",width=15,textvariable=self.var_Gender)
        Gender_combo["values"]=("Select Gender","Male","Female")
        Gender_combo.option_add('*TCombobox*Listbox*Font', ('Orbitron', 16))
        Gender_combo.current(0)
        Gender_combo.place(x=740, y=296,width=245,height=40)
       
        #NRIC
        NRIC_lbl=Label(bg_img,text="NRIC",font=label_font,bg=btm_blue,fg=white)
        NRIC_lbl.place(x=525, y=372,width=180,height=30)

        NRIC_Entry=ttk.Entry(bg_img,width=15,font=entry_font,textvariable=self.var_NRIC)
        NRIC_Entry.place(x=740, y=366,width=245,height=40)

        #Race
        Race_lbl=Label(bg_img,text="Race",font=label_font,bg=btm_blue,fg=white)
        Race_lbl.place(x=540, y=442,width=150,height=30)

        Race_combo=ttk.Combobox(bg_img,font=cb_font,state="readonly",width=15,textvariable=self.var_Race)
        Race_combo["values"]=("Select Race","Malay","Chinese","Indian","Orang Asli")
        Race_combo.option_add('*TCombobox*Listbox*Font', ('Orbitron', 16))
        Race_combo.current(0)
        Race_combo.place(x=740, y=436,width=245,height=40)

        #below the img
        #mugshot btn
        Upphoto_btn=Button(bg_img,text="Upload Mugshot", font=btn_font2,bg="#059FFE", cursor="hand2", command=self.addMugshot ,fg=white)
        Upphoto_btn.place(x=305,y=380,width=200,height=40)

        #DOB
        DOB_lbl=Label(bg_img,text="DOB",font=label_font,bg=btm_blue,fg=white)
        DOB_lbl.place(x=170, y=446,width=175,height=30)

        DOB_Entry = DateEntry(bg_img, width=15, font=cal_font, textvariable=self.var_DOB, state="readonly")
        DOB_Entry.configure(selectbackground="blue", selectforeground="white",  bordercolor= "blue",background="#00008B", foreground="#ededed",normalbackground="#add8e6", normalforeground="black")

        DOB_Entry.place(x=335, y=442,width=160,height=40)

        #Criminal charges
        Offence_lbl=Label(bg_img,text="Offence",font=label_font,bg=btm_blue,fg=white)
        Offence_lbl.place(x=525, y=512,width=175,height=30)

        Offence_entry=ttk.Entry(bg_img,width=15,font=entry_font,textvariable=self.var_Offenses)
        Offence_entry.place(x=740, y=506,width=245,height=40)

        #cancel btn 
        cancel_btn=Button(bg_img,text="Cancel", font=btn_font, cursor="hand2", command=self.onCancelPressed, bg=btn_color,fg=white)
        cancel_btn.place(x=400,y=570,width=140,height=40)

        #update btn 
        update_btn=Button(bg_img,text="Update", font=btn_font, command= self.Update_data,bg="#f5684f",fg="white")
        update_btn.place(x=568,y=570,width=140,height=40)

        #apprehend btn 
        apprehend_btn=Button(bg_img,text="Apprehended", font=btn_font, command= self.Apprehend_data,bg="#d43838",fg="white")
        apprehend_btn.place(x=740,y=570,width=200,height=40)

        #cont adjust the postion for cancel, update n apprehend btn
        #chg the img based on the user

        #-------Calling function to fetch data#
        self.fetch_data()

    #Moving back
    def onCancelPressed(self):
        # destroy current window
        self.Criminal_info.destroy()
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

    #for fetching data
    def fetch_data(self):
         #set connection to the db
        conn = mysql.connector.connect(host="localhost",username="root",password="admin",database="face_recog")
        #create a cursor object to interact with the database
        mycursor = conn.cursor()
        query = "SELECT * FROM criminal_info WHERE CID = %s"
        #the self.CID contain CID xx
        values = self.CID
        #remove the CID from the phrase
        values = values.replace("CID ", "")
        values = (values,)
        mycursor.execute(query, values)
        data = mycursor.fetchall()
        for i in data:
                        self.var_Fname.set(i[1])
                        self.var_Lname.set(i[2])
                        self.var_Gender.set(i[3])
                        self.var_Race.set(i[4])
                        self.var_NRIC.set(i[5])
                        self.var_DOB.set(i[6])
                        self.var_Offenses.set(i[7])
                        # retrieve the first image path from the mugshot column
                        image_paths = i[8].split(';')
                        if len(image_paths) > 0 :
                            image_path = image_paths[0]
                            try:#try to open the image based on the database 
                                Mugshot_img = Image.open(image_path)
                            except:# if no img is present in the comp then dis general
                                img_path2 = "D:/Downloads/Intelli Eye System/Mugshots/test"
                                Mugshot_img =Image.open(os.path.join(img_path2,"default.png"))
                            Mugshot_img = Mugshot_img.resize((205, 205), Image.LANCZOS)
                            self.photoimg_MugShot = ImageTk.PhotoImage(Mugshot_img)
                            self.Mushot_Disp_position.configure(image=self.photoimg_MugShot)

        conn.commit()
        conn.close()

    def Update_data(self):

        loading_font =tkFont.Font(size=11)

        #================mysql database connnection==============
        #set connection to the db
        conn = mysql.connector.connect(host="localhost",username="root",password="admin",database="face_recog")
        #create a cursor object to interact with the database
        mycursor = conn.cursor()



         # Retrieve all NRIC data from the database
        mycursor.execute("SELECT Nric FROM criminal_info")
        rows = mycursor.fetchall()

        cid = self.CID.replace("CID ", "")
        mycursor.execute("SELECT Nric FROM criminal_info WHERE cid=%s", (cid,))
        existing_nric = mycursor.fetchone()[0]

        #chck if the all entry is valid if not prompt error 
        if check_fields(self.var_Gender.get(), self.var_Fname.get(), self.var_Lname.get(), self.var_DOB.get(), self.var_Race.get(), self.var_NRIC.get(), self.var_Offenses.get())  :
             #show prompt error
             messagebox.showerror("Error", "All Fields are required", parent=self.Criminal_info)
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
        elif (is_numeric(self.var_NRIC.get()) == False):
              #show error
             messagebox.showwarning("Attention", "Please enter only numerical value for NRIC field.")
        elif (len(self.var_NRIC.get()) != 12):
             #show error
             messagebox.showwarning("Attention", "Please ensure there is 12 digit NRIC field.")
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
        elif any(row[0] == self.var_NRIC.get() for row in rows if row[0] != existing_nric):
            messagebox.showerror("Error", "NRIC already exists in the database")
        else:
            
            try:
                #show prompt yes or no
                Update= messagebox.askyesno("Update","Do you want to update this criminal details?", parent=self.Criminal_info)

                if Update > 0:#when yes is press
                    values = self.CID.replace("CID ", "")
                    if self.mugshot is None or len(self.mugshot) == 0:#when mugshot is not update
                        mycursor.execute("update criminal_info set Fname=%s, Lname=%s, Gender=%s, Race=%s, Nric=%s, Dob=%s, Offenses=%s where cid=%s", (
                        self.var_Fname.get(), self.var_Lname.get(), self.var_Gender.get(), self.var_Race.get(), self.var_NRIC.get(), self.var_DOB.get(), self.var_Offenses.get(), values
                ))
                         #make changes to db
                        conn.commit()
                        mycursor.fetchall()  # Discard the result of the previous query

                        messagebox.showinfo("Success", "Criminal info has been updated", parent= self.Criminal_info)
                        #move back to prev page
                        # destroy current window
                        self.Criminal_info.destroy()
                        # unhide old window
                        self.main_window.deiconify()

                    else:#when mughsot is updated

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

                        if has_faces == True and all_img_perfect >=10:
                            mycursor.execute("update criminal_info set Fname=%s, Lname=%s, Gender=%s, Race=%s, Nric=%s, Dob=%s, Offenses=%s, Mugshot=%s where cid=%s", (
                            self.var_Fname.get(), self.var_Lname.get(), self.var_Gender.get(), self.var_Race.get(), self.var_NRIC.get(), self.var_DOB.get(), self.var_Offenses.get(), self.mugshot, values))
                            #make changes to db
                            conn.commit()
                            mycursor.fetchall()  # Discard the result of the previous query

                            self.Generate_data()#image will only be generated when mugshot is updated
                        elif has_faces == FALSE:
                            messagebox.showerror("Error", "Database not updated please input images that has clear faces.")
                        elif all_img_perfect < 10:
                            messagebox.showerror("Error", "Database not updated, system requires a minumum of 10 images.")

                        else:
                            messagebox.showerror("Error", "Database not updated please try again.")


                else:#when no is press
                     if not Update:
                          return   
                                    
                #close db
                conn.close


            except Exception as es:
                #error for dev to see
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.Criminal_info)

    #remove criminal from database and also images locally
    def Apprehend_data(self):
              #================mysql database connnection==============
        #set connection to the db
        conn = mysql.connector.connect(host="localhost",username="root",password="admin",database="face_recog")
        #create a cursor object to interact with the database
        mycursor = conn.cursor()

        Apprehend= messagebox.askyesno("Apprehended", "Confirm suspect has been aprehended? Criminal info will be removed." , parent=self.Criminal_info)
        try:
            if Apprehend >0:

                # Retrieve mugshot paths for the criminal to be deleted
                cid = self.CID.replace("CID ", "")
                mycursor.execute("SELECT mugshot FROM criminal_info WHERE cid=%s", (cid,))
                rows = mycursor.fetchall()
                mycursor.fetchall()  # Discard the result of the previous query


                for row in rows:
                    # Split the row into separate image paths
                    mugshot_paths = row[0].split(";")

                    # Loop through each image path and delete the file
                    for mugshot_path in mugshot_paths:
                        filename = os.path.basename(mugshot_path)
                        if os.path.exists(mugshot_path):
                            os.remove(mugshot_path)
                            print(f"Deleted file: {mugshot_path}")
                        else:
                            print(f"File not found: {mugshot_path}")
                            
                values = (self.CID.replace("CID ", ""),)  # convert string to tuple
                sql = "DELETE FROM criminal_info WHERE cid = %s"
                mycursor.execute(sql, values)

            else:
                if not Apprehend: 
                    return
            conn.commit()
            conn.close()     
            
            messagebox.showinfo("Success", "Criminal has been apprehended hence will be removed from the list", parent= self.Criminal_info)

            #move back to prev page
            # destroy current window
            self.Criminal_info.destroy()
            # unhide old window
            self.main_window.deiconify()
            
            
        except Exception as es:
                #error for dev to see
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.Criminal_info)

    def Generate_data(self):

        loading_font =tkFont.Font( size=11)

        # Connect to database
        #set connection to the db
        conn = mysql.connector.connect(host="localhost",username="root",password="admin",database="face_recog")
        #create a cursor object to interact with the database
        mycursor = conn.cursor()
        cid = self.CID.replace("CID ", "")

         #for converting image into greyscale 
        mycursor.execute("SELECT mugshot FROM criminal_info WHERE cid=%s", (cid,))
        rows = mycursor.fetchall()
        mycursor.fetchall()  # Discard the result of the previous query

        img_id = 0
        face_paths = []
        # Folder containing the images
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
        progress_bar.pack(fill="x", padx=10, pady=10)


        status_label = tk.Label(loading_window, text="Image conversion in progress...",font=loading_font)
        status_label.pack(pady=5)
                
        loading_window.update()
        #==================================

        progress_counter = 0  # Counter for tracking progress used in loading


        for row in rows:
            # Split the row into separate image paths
            mugshot_paths = row[0].split(";")
                    
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

                        #Convert to grayscale
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                        # Detect faces in the image
                        # will affect the accuracy of the face detection
                        # lower scaleFactor increase accuracy but also increase detection time
                        # lower minNeighbors increase false +ve & higher increase false -ve
                        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
                        
                        # Extract faces and save as new images
                        for (x, y, w, h) in faces:
                            face = gray[y:y+h, x:x+w]
                            face_filename = f"CID_{cid}_{img_id}_gray.jpg" # use highest_img_id and img_id to generate filename
                            face_path = os.path.join(output_folder_path, face_filename)
                            cv2.imwrite(face_path, face)
                            # Increment img_id by the number of faces detected
                            img_id += 1 
                            face_paths.append(face_path)

                        mycursor.execute("UPDATE criminal_info SET mugshot=%s WHERE cid=%s", (";".join(face_paths), cid))#update the database with the latest poto
                        mycursor.fetchall()  # Discard the result of the previous query

                        # Update progress counter
                        progress_counter += 1
                        # Update progress bar
                        progress_var.set(progress_counter)
                        loading_window.update()

                    except Exception as e:
                        # Display error message
                        messagebox.showerror("Error", f"Error detecting faces in {filename}: {str(e)}")

            # Commit changes and close the database connection
            conn.commit()
            conn.close()
            # update progress bar and status
            progress_var.set(total_images)
            status_label.config(text="Image conversion completed.",font=loading_font)
            loading_window.update()
            loading_window.destroy()
            messagebox.showinfo("Success", "All images has been normalised and converted into grayscale and Criminal info has been updated.")
            self.Criminal_info.destroy()
            # unhide old window
            self.main_window.deiconify()





#now start part 5

#----------Field validation---------------
 #check if the entry field is empty 
def check_fields(*args):
    for field in args:
        if not field.strip() or field == "Select Gender" or field == "Select Race":
            return True
    return False     

#Returns True if entry_text contains only alphabetical characters
def is_alpha(entry_text):
    #return entry_text.replace(" ", "").isalpha()
    return all(c.isalpha() or c.isspace() or c == ',' for c in entry_text)

#Returns True if entry_text contains only numeric characters or contain "/"
def is_numeric(entry_text):
    return all(char.isdigit() or char == "/" for char in entry_text)

               

        
       