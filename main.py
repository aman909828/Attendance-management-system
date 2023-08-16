import os
from time import strftime
from tkinter import *
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from face_recognition import Face_Recognition
from train import Train
from chat import chatbot
from help import Help
from attendance import Attendance, speak_va


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x700+0+0")
        self.root.title("Face Recognition System")

        
        # first
        img = Image.open(r"college_images\u.jpg")
        img = img.resize((467, 90), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=467, height=90)

        # second
        img1 = Image.open(r"college_images\college.png")
        img1 = img1.resize((467, 90), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=467, y=0, width=467, height=90)

        # third
        img2 = Image.open(r"college_images\u.jpg")
        img2 = img2.resize((466, 90), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=934, y=0, width=466, height=90)

        # background image
        img3 = Image.open(r"college_images\5.jpg")
        img3 = img3.resize((1400, 610), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=90, width=1400, height=610)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 25, "bold"),
                          bg="teal", fg="black")
        title_lbl.place(x=0, y=0, width=1400, height=40)

        
        def time():
            string=strftime('%H:%M:%S:%p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl= Label(title_lbl,font=("times new roman",10,"bold"),bg='teal',fg='black')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        
        # student button
        img4 = Image.open(r"college_images\details.jpg")
        img4 = img4.resize((180, 180), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,command=self.student_details, image=self.photoimg4, cursor="hand2")
        b1.place(x=100, y=60, width=180, height=180)

        b1_1 = Button(bg_img,command=self.student_details, text="Student Details", cursor="hand2",
                      font=("times new roman", 12, "bold"), bg="black", fg="white")
        b1_1.place(x=100, y=240, width=180, height=30)

        # detect face button
        img5 = Image.open(r"college_images\detector.png")
        img5 = img5.resize((180, 180), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,command=self.face_data, image=self.photoimg5, cursor="hand2")
        b1.place(x=400, y=60, width=180, height=180)

        b1_1 = Button(bg_img,command=self.face_data,text="Student Detector", cursor="hand2",
                      font=("times new roman", 12, "bold"), bg="black", fg="white")
        b1_1.place(x=400, y=240, width=180, height=30)

        # Attendance button
        img6 = Image.open(r"college_images\attend.jpg")
        img6 = img6.resize((180, 180), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img,command=self.attendance_data, image=self.photoimg6, cursor="hand2")
        b1.place(x=700, y=60, width=180, height=180)

        b1_1 = Button(bg_img,command=self.attendance_data, text="Attendance", cursor="hand2",
                      font=("times new roman", 12, "bold"), bg="black", fg="white")
        b1_1.place(x=700, y=240, width=180, height=30)

        # help desk button
        img7 = Image.open(r"college_images\help.png")
        img7 = img7.resize((180, 180), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img,command=self.help_data, image=self.photoimg7, cursor="hand2")
        b1.place(x=1000, y=60, width=180, height=180)

        b1_1 = Button(bg_img,command=self.help_data,  text="Help Desk", cursor="hand2",
                      font=("times new roman", 12, "bold"), bg="black", fg="white")
        b1_1.place(x=1000, y=240, width=180, height=30)

        # train face button
        img8 = Image.open(r"college_images\train.png")
        img8 = img8.resize((180, 180), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img,command=self.train_data,image=self.photoimg8, cursor="hand2")
        b1.place(x=100, y=310, width=180, height=180)

        b1_1 = Button(bg_img,command=self.train_data,text="Train data", cursor="hand2",
                      font=("times new roman", 12, "bold"), bg="black", fg="white")
        b1_1.place(x=100, y=490, width=180, height=30)

        # photos button
        img9 = Image.open(r"college_images\photo.jpg")
        img9 = img9.resize((180, 180), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img,command=self.open_img, image=self.photoimg9, cursor="hand2")
        b1.place(x=400, y=310, width=180, height=180)

        b1_1 = Button(bg_img,command=self.open_img, text="Photos", cursor="hand2",
                      font=("times new roman", 12, "bold"), bg="black", fg="white")
        b1_1.place(x=400, y=490, width=180, height=30)

        # chatbot button
        img10 = Image.open(r"college_images\chat.jpg")
        img10 = img10.resize((180, 180), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img,command=self.chatbot, image=self.photoimg10, cursor="hand2")
        b1.place(x=700, y=310, width=180, height=180)

        b1_1 = Button(bg_img,command=self.chatbot, text="ChatBot", cursor="hand2",
                      font=("times new roman", 12, "bold"), bg="black", fg="white")
        b1_1.place(x=700, y=490, width=180, height=30)

        # Exit button
        img11 = Image.open(r"college_images\exit.png")
        img11 = img11.resize((180, 180), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img,command=self.iExit, image=self.photoimg11, cursor="hand2")
        b1.place(x=1000, y=310, width=180, height=180)

        b1_1 = Button(bg_img,command=self.iExit,text="Exit", cursor="hand2",
                      font=("times new roman", 12, "bold"), bg="black", fg="white")
        b1_1.place(x=1000, y=490, width=180, height=30)
        
    
    def open_img(self):
        os.startfile("data") 
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def chatbot(self):
        self.new_window=Toplevel(self.root)
        self.app=chatbot(self.new_window)
    
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        
    def iExit(self):
        speak_va('Are you sure you want to exit?')
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit?")
        if self.iExit>0:
            self.root.destroy()
        else:
            return   

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
