from tkinter import*
from tkinter import messagebox, ttk
import tkinter.font as tkFont
import tkinter as tk
from PIL import Image, ImageTk
from criminalList import Criminal_Listing
from surveillanceLog import surveillance_Log
from dashboard import Dashboard
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

class Face_Recognition_Sys:
    def __init__(self,root):
                self.root=root
                #setting the ui window size
                self.root.geometry("1280x720+0+0")
                self.root.title("Intelli Eye System")
                #imagepath variable
                img_path = "D:/Downloads/Intelli Eye System/UI image"

                #UI variable
                #fontVariable
                time_font =tkFont.Font(family="Orbitron", size=14, weight="bold")
                btn_font = tkFont.Font(family="Orbitron", size=18,weight="bold")
                label_font=tkFont.Font(family="Orbitron", size=18)
                entry_font=tkFont.Font(family="Orbitron", size=16)
                #wordbgVariable
                fontBG="#020d43"
                #fontcolorVariable
                fontColor="white"
                
                #criminal data variable
                self.var_Uname = StringVar()
                self.var_Pwd = StringVar()

                # function to change properties of button on hover
                def changeOnHover(button, colorOnHover, colorOnLeave):
        
                        # adjusting backgroung of the widget
                        # background on entering widget
                        button.bind("<Enter>", func=lambda e: button.config(
                                background=colorOnHover))
                        
                        # background color on leving widget
                        button.bind("<Leave>", func=lambda e: button.config(
                                background=colorOnLeave))
                
                #background img declare
                img=Image.open(os.path.join(img_path,"login.png"))
                img=img.resize((1290,720),Image.LANCZOS)
                self.photoimg=ImageTk.PhotoImage(img)

                bg_img=Label(self.root, image=self.photoimg)
                #set positioning for bg img
                bg_img.place(x=0, y=0, width=1280, height=720)

                #ui for username
                Username_Entry=ttk.Entry(bg_img,width=15,font=entry_font,textvariable=self.var_Uname)
                Username_Entry.place(x=427, y=360,width=400,height=40)

                #ui for password
                Pwd_Entry=ttk.Entry(bg_img,width=15,font=entry_font, show="*",textvariable=self.var_Pwd)
                Pwd_Entry.place(x=427, y=460,width=400,height=40)
                

                #create btn 
                login_btn=Button(bg_img,text="Sign In", font=btn_font,cursor="hand2", bg="#f5684f",fg="white",command=self.Login)
                login_btn.place(x=576,y=525,width=140,height=40)
                changeOnHover(login_btn, "#00008B", "#f5684f")

                #=======Time========
                def time():
                        string =strftime('%H:%M:%S %p')
                        lblTime.config(text = string)
                        lblTime.after(1000, time)

                lblTime=Label(bg_img, font=time_font,bg="#021a60",fg=fontColor)
                lblTime.place(x=560,y=610,width=160,height=30)
                time()

              


 #=======================open new window function for criminal list & alert ===============================================
    def Dashboard(self):
                #hide current window
                self.root.withdraw()
                #create new window
                self.new_window=Toplevel(self.root)
                self.app=Dashboard(self.root, self.new_window)
    def Login(self):
            username=self.var_Uname.get()
            pwd= self.var_Pwd.get()
            if username == "admin" and pwd == "admin":
                self.Dashboard()
                self.var_Uname.set('')  # Clear the username entry field
                self.var_Pwd.set('')  # Clear the password entry field
            elif username == "" and pwd == "":
                messagebox.showwarning("Invalid credentials", "Username and password field is emptry.")
            elif username == "":
                messagebox.showwarning("Invalid credentials", "Username field is emptry.")
            elif pwd == "":
                messagebox.showwarning("Invalid credentials", "Password field is emptry.")
            else:
                messagebox.showwarning("Invalid credentials", "Credentials are invalids.")


# create the main window and start the tkinter event loop
if __name__=="__main__":
    root=Tk()
    root.resizable(False,False)
    root.attributes('-fullscreen', False)
    obj=Face_Recognition_Sys(root)
    root.mainloop()
        
#additional task
# accuracy need to edit 
# Status code 429 from http://ipinfo.io/json: ERROR - 429 Client Error: Too Many Requests for url: http://ipinfo.io/json -> geocode lat and long hpns when spam too much
# delete data in log error (maybe remove consult wif supervisor first cz its unstable) (omit it)
# explain in why it happens n the limiation of using the geo ip
# check create criminal (error is due to i retrieve the cid from db based on nric n gender)

##add notes
# can detect multiple ppl at once & detection can differentiatea
# enroll img i chg to 720 res and the conf is up to 81 >

#not neccessary
# xtra haarcascade like eye mouth etc (not neccessary)
# in the csv file snap a pic of the criminal (no purpose)adad

# progres
# i had increase enroll res to 720
# person image in stil limg can be recorded as well
# now it will record more than 1 person CID if there are present in the frame into csv 
# default csv can export
# each criminal profile img is successfully display
# not all images of the criminal is deleted only the one store in db (file path) other is not Hvent verify due to the update function (solved)
# data will only be generate when new img is updated in criminal profile, if not it wil remains
# when there is space in offense field, the output on the log will hv error  (solved by chging the delimeter to ';' n chg the reading method in surveilance log)
# similarity rate is in the log file as well
# loading for training data set is done
# train data remove the img process instead show loading screen (done (loading havent remove process) )
# in profie creation n update, it will check if img has faces anmd must has faces or at least 99 img or else it wont update (inc loading)
# when an error encounter in create n udpate the database will still b update (solved)
# chg nationality to race due to the myriad of passport number
# input validation (done for update n for create) do place holder for create criminal prof [done]
# chg the the date entry to only readonly state so user cant input
# calendar colr chg n size
# race input has chg to combo box
# added time in main
# login page
# multi thread for notification n writtin into file ele will cause system to freeze and slow down record time respectively