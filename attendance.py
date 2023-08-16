from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import pathlib
import csv
import mysql.connector
from tkinter import filedialog
import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice

def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x700+0+0")
        self.root.title("Face Recognition System")

        # variable 
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar() 

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
        
        #bg image
        img3=Image.open(r"college_images\clock.jpg")
        img3=img3.resize((1400,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=90,width=1400,height=610)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="teal",fg="black")
        title_lbl.place(x=0,y=0,width=1400,height=35)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=40,width=1250,height=510)
        
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=1,width=610,height=500)
        
        img_left=Image.open(r"college_images\student4.jpg")
        img_left=img_left.resize((600,90),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=600,height=90)
        
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=95,width=595,height=380)
        
        # label andentry 
        #attendane id

        attendanceId_label=Label(left_inside_frame,text="AttendanceId :",font=("times new roman",11,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
            # textvariable=self.var_atten_id,
        attendanceID_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("times new roman",10,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #Roll
        rollLabel=Label(left_inside_frame,text="Roll :",font=("times new roman",11,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=10,pady=10,sticky=W)
            # textvariable=self.var_atten_roll,
        atten_roll=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("times new roman",10,"bold"))
        atten_roll.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        #Name
        nameLabel=Label(left_inside_frame,text="Name :",font=("times new roman",11,"bold"),bg="white")
        nameLabel.grid(row=1,column=0,padx=10,pady=10,sticky=W)
            # textvariable=self.var_atten_name,
        atten_name=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=("times new roman",10,"bold"))
        atten_name.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #Department
        depLabel=Label(left_inside_frame,text="Department :",font=("times new roman",11,"bold"),bg="white")
        depLabel.grid(row=1,column=2,padx=10,pady=10,sticky=W)
            # textvariable=self.var_atten_dep,
        atten_dep=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=20,font=("times new roman",10,"bold"))
        atten_dep.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        #Time
        timeLabel=Label(left_inside_frame,text="Time :",font=("times new roman",11,"bold"),bg="white")
        timeLabel.grid(row=2,column=0,padx=10,pady=10,sticky=W)
            # textvariable=self.var_atten_time,
        atten_time=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("times new roman",10,"bold"))
        atten_time.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #Date
        dateLabel=Label(left_inside_frame,text="Date :",font=("times new roman",11,"bold"),bg="white")
        dateLabel.grid(row=2,column=2,padx=10,pady=10,sticky=W)
            # textvariable=self.var_atten_date,
        atten_date=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("times new roman",10,"bold"))
        atten_date.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        # attendence combo box
        attendancelabel=Label(left_inside_frame,text="Attendance_Status :",font=("times new roman",10,"bold"),bg="White")
        attendancelabel.grid(row=3,column=0,padx=10,pady=10,sticky=W)
            # textvariable=self.var_atten_attendance,
        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman",10,"bold"),state="readonly",width=18)
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,padx=10,pady=10,sticky=W)
        
        # button 
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=290,width=580,height=70)
            # ,command=self.importCsv
        save_button=Button(btn_frame,command=self.importCsv,text="Import csv",width=31,font=("times new roman",12,"bold"),bg="teal",fg="black")
        save_button.grid(row=0,column=0)
            # command=self.exportCsv,
        export_button=Button(btn_frame,command=self.exportCsv,text="Export csv ",width=31,font=("times new roman",12,"bold"),bg="teal",fg="black")
        export_button.grid(row=0,column=1)
            # command=self.action,
        update_button=Button(btn_frame,text="Update",command=self.action,width=31,font=("times new roman",12,"bold"),bg="teal",fg="black")
        update_button.grid(row=1,column=0)
            # command=self.reset_data,
        reset_button=Button(btn_frame,command=self.reset_data,text="Reset",width=31,font=("times new roman",12,"bold"),bg="teal",fg="black")
        reset_button.grid(row=1,column=1)
        
        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=630,y=1,width=610,height=500)
        
        table_frame=Frame(Right_frame,bd=3,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=0,width=600,height=475)
        
        # scroll bar table 
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text=" Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=120)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=120)
        self.AttendanceReportTable.column("attendance",width=100)
              
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
        
        #============================================fetch data======================================== 
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    #============================================import csv==========================================
    def importCsv(self):    
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata) 
            
    #===========================================export update===========================================
    def action(self):
        id=self.var_atten_id.get()
        roll=self.var_atten_roll.get()
        name=self.var_atten_name.get()
        dep=self.var_atten_dep.get()
        time=self.var_atten_time.get()
        date=self.var_atten_date.get()
        attendn=self.var_atten_attendance.get()

        #====================================write to csv file============================================
        try:
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="a",newline="\n") as f:
                dict_writer=csv.DictWriter(f,fieldnames=(["ID","Roll","Name","Department","Time","Date","Attendance"]))
                dict_writer.writerow({
                "ID":id,
                "Roll":roll,
                "Name":name,
                "Department":dep,
                "Time":time,
                "Date":date,
                "Attendance":attendn
                    })
            speak_va("Your Data Exported to" + os.path.basename(fln) + " Successfully")
            messagebox.showinfo("Data Exported","Your data exported to " +os.path.basename(fln)+ " Successfully",parent=self.root)
        except Exception as es:
            speak_va("Error")
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)        
               
    #================================================export csv ===============================================        
    def exportCsv(self):    
        try:
            if len(mydata)<1:
                speak_va("No Data Found")
                messagebox.showerror("No Data","No Data Found",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                   exp_write.writerow(i)
            speak_va("Your Data Exported to " + os.path.basename(fln) + " Successfully")
            messagebox.showinfo("Data Export","Your Data has been Exported to " +os.path.basename(fln)+ " Successfully")    
        except Exception as es:
                speak_va("Error")
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    #============================================view attendance report csv==========================================       
    # def viewReport(self):    
    #     try:
    #         if len(mydata)<1:
    #             speak_va("No Data Found")
    #             messagebox.showerror("No Data","No Data Found",parent=self.root)
    #             return False
    #         fln=filedialog.asksaveasfile(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
    #         with open(fln,mode="w",newline="") as myfile:
    #             exp_write=csv.writer(myfile,delimiter=",")
    #             for i in mydata:
    #                 exp_write.writerow(i)
    #             speak_va("Your Data Exported to" + os.path.basename(fln) + " Successfully")
    #             messagebox.showinfo("Data Export","Your Data has been Exported to"+os.path.basename(fln)+"Successfully")    
    #     except Exception as es:
    #             speak_va("Error")
    #             messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)
        
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
    def reset_data(self): 
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")







if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()