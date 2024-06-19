from tkinter import*
from tkinter import messagebox, ttk
import tkinter.font as tkFont
import tkinter as tk
from PIL import Image, ImageTk
from criminalList import Criminal_Listing
from surveillanceLog import surveillance_Log
import os
import os.path  
import cv2
import numpy as np
import mysql.connector
from plyer import notification
import time
from time import strftime
from threading import Thread
from datetime import datetime, timedelta, date
import geocoder

class Dashboard:
    def __init__(self,old_window,new_window):
                #this is to store the prev window onto the variable
                self.main_window = old_window

                #to store the current window 
                self.Dashboard=new_window
                #setting the ui window size
                self.Dashboard.geometry("1280x720+0+0")
                self.Dashboard.title("Intelli Eye System")
                 #set when the window close btn is click it will stop the app
                new_window.protocol("WM_DELETE_WINDOW", new_window.quit)
                #imagepath variable
                img_path = "D:/Downloads/Intelli Eye System/UI image"

                #UI variable
                #fontVariable
                my_font = tkFont.Font(family="Orbitron", size=12, weight="bold")
                time_font =tkFont.Font(family="Orbitron", size=14, weight="bold")

                #wordbgVariable
                fontBG="#020d43"
                #fontcolorVariable
                fontColor="white"

                #for notification when there is criminal
                self.last_notification_time = 0 


                # function to change properties of button on hover
                def changeOnHover(button, colorOnHover, colorOnLeave):
        
                        # adjusting backgroung of the widget
                        # background on entering widget
                        button.bind("<Enter>", func=lambda e: button.config(
                                background=colorOnHover))
                        
                        # background color on leving widget
                        button.bind("<Leave>", func=lambda e: button.config(
                                background=colorOnLeave))
                
                #image for ui
                img=Image.open(os.path.join(img_path,"test4.png"))
                img=img.resize((1290,720),Image.LANCZOS)
                self.photoimg=ImageTk.PhotoImage(img)

                bg_img=Label(self.Dashboard, image=self.photoimg)
                #set positioning for img
                bg_img.place(x=0, y=0, width=1280, height=720)

                #criminal details btn
                img4=Image.open(os.path.join(img_path,"folder9.png"))
                img4=img4.resize((160,120),Image.LANCZOS)
                self.photoimg4=ImageTk.PhotoImage(img4)

                b1=Button(bg_img,image=self.photoimg4,command=self.ListingPage, cursor="hand2",border=0,bg="#00e0f7")
                b1.place(x=245, y=180,width=168,height=128)
                #btn chg on hover
                changeOnHover(b1, "red", "#00e0f7")
                
                #surveillance log btn
                img6=Image.open(os.path.join(img_path,"record6.png"))
                img6=img6.resize((160,120),Image.LANCZOS)
                self.photoimg6=ImageTk.PhotoImage(img6)

                b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command= self.Surveillance,border=0,bg="#00e0f7")
                b3.place(x=245,y=400,width=168,height=128)
                #btn chg on hover
                changeOnHover(b3, "red", "#00e0f7")
                
                #real time surveliance btn
                img7=Image.open(os.path.join(img_path,"recog6.png"))
                img7=img7.resize((160,120),Image.LANCZOS)
                self.photoimg7=ImageTk.PhotoImage(img7)

                b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.monitoring,border=0,bg="#00e0f7")
                b4.place(x=870,y=140,width=168,height=128)
                #btn chg on hover
                changeOnHover(b4, "red", "#00e0f7")

                #ai btn
                img8=Image.open(os.path.join(img_path,"ai8.png"))
                img8=img8.resize((160,120),Image.LANCZOS)
                self.photoimg8=ImageTk.PhotoImage(img8)

                b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_classifier,border=0,bg="#00e0f7")
                b5.place(x=1020,y=300,width=168,height=128)
                #btn chg on hover
                changeOnHover(b5, "red", "#00e0f7")

                #logout btns
                img9=Image.open(os.path.join(img_path,"power5.png"))
                img9=img9.resize((160,120),Image.LANCZOS)
                self.photoimg9=ImageTk.PhotoImage(img9)

                b6=Button(bg_img,image=self.photoimg9,cursor="hand2",border=0,bg="#00e0f7",command=self.Logout)
                b6.place(x=870,y=450,width=168,height=128)
                #btn chg on hover
                changeOnHover(b6, "red", "#00e0f7")

                #label for detail btn
                lbl1=Label(bg_img,text="Criminal Details",font=my_font,bg=fontBG,fg=fontColor)
                lbl1.place(x=260, y=312,width=145,height=15)

                #label for alert btn
                lbl3=Label(bg_img,text="Surveillance",font=my_font,bg=fontBG,fg=fontColor)
                lbl3.place(x=264, y=532,width=135,height=15)

                #label for face recog btn
                lbl4=Label(bg_img,text="Real-Time Monitoring",font=my_font,bg=fontBG,fg=fontColor)
                lbl4.place(x=870, y=270,width=190,height=20)

                #label for ai btn
                lbl5=Label(bg_img,text="Train AI",font=my_font,bg=fontBG,fg=fontColor)
                lbl5.place(x=1038, y=432,width=135,height=15)

                #label for logout btn
                lbl6=Label(bg_img,text="Logout",font=my_font,bg=fontBG,fg=fontColor)
                lbl6.place(x=885, y=580,width=135,height=20)

                #=======Time========
                def time():
                        string =strftime('%H:%M:%S %p')
                        lblTime.config(text = string)
                        lblTime.after(1000, time)

                lblTime=Label(bg_img, font=time_font,bg="#021a60",fg=fontColor)
                lblTime.place(x=560,y=610,width=160,height=30)
                time()

 #=======================open new window function for criminal list & alert ===============================================
    def ListingPage(self):
                #hide current window
                self.Dashboard.withdraw()
                #create new window
                self.new_window=Toplevel(self.Dashboard)
                self.app=Criminal_Listing(self.Dashboard, self.new_window)
    def Surveillance(self):
                #hide current window
                self.Dashboard.withdraw()
                #create new window
                self.new_window=Toplevel(self.Dashboard)
                self.app=surveillance_Log(self.Dashboard, self.new_window)

    def Logout(self):
                 #move back to prev page
                 # destroy current window
                 self.Dashboard.destroy()
                 # unhide old window
                 self.main_window.deiconify()
#========================function to train the ai===============================================
    def train_classifier(self):
        
        loading_font =tkFont.Font( size=11)
        # set folder path
        data_dir = "D:/Downloads/Intelli Eye System/Mugshots/test/faces"

        # get path for each image in folder
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        total_images = len(path) # count total images

        #==========Loading widgets===========
        loading_window = tk.Toplevel()#create new window
        loading_window.title("Training Classifier")
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

        status_label = tk.Label(loading_window, text="Training in progress...",font=loading_font)
        status_label.pack(pady=5)
        

        loading_window.update()
        #==================================

        faces = []
        ids = []

        # iterate over each image and extract features
        for i, image in enumerate (path):
                img = Image.open(image).convert('L')  # gray scale image
                imageNP = np.array(img, 'uint8')
                id = int(os.path.split(image)[1].split('_')[1])  # split the img name to select the CID

                faces.append(imageNP)
                ids.append(id)
                #cv2.imshow("Training", imageNP)#display the processing img
                cv2.waitKey(1) == 13
                
                 # update progress bar
                progress_var.set(i+1)
                loading_window.update()

        ids = np.array(ids)

        # Train classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        
        # update progress bar and status
        progress_var.set(total_images)
        status_label.config(text="Training completed.",font=loading_font)
        loading_window.update()
        loading_window.destroy()

        messagebox.showinfo("Result", "Training datasets completed.")

        

#===============surveillance log==============================
    def criminalLogs(self, id, full_name, ofen,confidence):
        with open("CriminalLog.csv", "r+", newline="\n") as f:
                myDataList = f.readlines()
                name_list = []
                last_recorded_times = {}

                for line in myDataList:
                        entry = line.split(";")
                        name = entry[0].strip()
                        name_list.append(name)
                        last_recorded_time_str = entry[3].strip()
                        last_recorded_time = datetime.strptime(last_recorded_time_str, "%H:%M:%S").time()
                        last_recorded_times[name] = last_recorded_time

                current_time = datetime.now().time()
                Date = datetime.now().strftime("%d/%m/%Y")
                Time = datetime.now().strftime("%H:%M:%S")

                g = geocoder.ip('me')

                if str(id) in name_list:
                        # Check if the time difference is greater than or equal to 1 minute for the last recorded time of the same criminal
                        last_recorded_time = last_recorded_times[str(id)]
                        diff = datetime.combine(date.today(), current_time) - datetime.combine(date.today(), last_recorded_time)
                        if diff >= timedelta(minutes=1):
                                # Write the new record with the current time
                                f.write(f"{id}; {full_name}; {ofen}; {Time}; {Date}; {g.lat}; {g.lng}; {confidence}\n")
                                print("Criminal is update to file.")
                        else:
                                print("Criminal already exists in the file and has been recorded less than 1 minute ago.")
                else:
                        # Write the new record if the criminal is not present in the file
                        f.write(f"{id}; {full_name}; {ofen}; {Time}; {Date}; {g.lat}; {g.lng}; {confidence}\n")
                        print("New data written to file.")
        

#==============real time monitoring face recog================================
    def monitoring(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

                coordinate=[]
                id = 0  # Initialize id with default value

               
                #loop for webcam
                for (x,y,w,h)in features:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                        confidence=int((100*(1-predict/300)))

                        # Connect to database
                        #set connection to the db
                        conn = mysql.connector.connect(host="localhost",username="root",password="admin",database="face_recog")
                        #create a cursor object to interact with the database
                        mycursor = conn.cursor()
                        #obtain the fname and lname then concatenate them
                        mycursor.execute("select Fname, Lname from criminal_info where CID="+str(id)) 
                        result = mycursor.fetchone()
                        full_name = result[0] + ' ' + result[1]
                        
                        #try this
                        # if result is not None:
                        #        full_name = result[0] + ' ' + result[1]
                        #else:
                        #        full_name = "Unknown"

                        #obtain offense info
                        mycursor.execute("select offenses from criminal_info where CID="+str(id))
                        ofen=mycursor.fetchone()
                        #try remove this
                        ofen="+".join(ofen)

                        #similarity threshold (ROI) 
                        if confidence>77:
                                #display the criminal info
                                cv2.putText(img,f"Name:{full_name}",(x,y-65),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)
                                cv2.putText(img,f"Offense:{ofen}",(x,y-40),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)
                                cv2.putText(img,f"CID:{id}",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)
                                
                                #run a separate thread for writing into file or else very lag
                                Thread(target=self.criminalLogs, args=(id, full_name, ofen, confidence)).start()
                                
                                #alert toast on window using new thread or else program crash
                                current_time = time.time()
                                # check if 1 minute has passed since last notification
                                if current_time - self.last_notification_time >= 60: 
                                        def show_notification():
                                                notification.notify(
                                                        title='Criminal Alert!',
                                                        message='Criminal has been detected',
                                                        timeout=10
                                                )
                                        Thread(target=show_notification).start()
                                        self.last_notification_time = current_time # update flag variable with current time
                        else:
                                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                                cv2.putText(img,f"Clear records",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)

                        coordinate=[x,y,w,y]
                return coordinate
        
        def recognize(img,clf,faceCascade):
                #adjust accuracy  of algo
                coordinate = draw_boundary(img,faceCascade,1.2,10,(255,25,255),"Face",clf)
                #def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
                return img
        
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)

        while True:
               ret,img=video_cap.read()
               img=recognize(img,clf,face_cascade)
               cv2.imshow("Monitoring video feed in real-time", img)

               if cv2.waitKey(1) == 13 or cv2.waitKey(10) == 27:#exit on enter key or esc key
                        break
               elif cv2.getWindowProperty("Monitoring video feed in real-time", cv2.WND_PROP_VISIBLE) < 1:
                        break
        video_cap.release()
        cv2.destroyAllWindows()


