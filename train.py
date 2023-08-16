from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice

def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x700+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("Algerian",20,"bold"),bg="teal",fg="black")
        title_lbl.place(x=20,y=0,width=1230,height=45)
        
        img_top = Image.open(r"college_images\facialrecognition.png")
        img_top=img_top.resize((1230, 260),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=20,y=45,width=1230,height=260)
        
        # Button
            # ,command=self.train_classifier
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("Algerian",25,"bold"),bg="dark slate grey",fg="white")
        b1_1.place(x=20,y=305,width=1230,height=60)
        
        img_bottom=Image.open(r"college_images\facialrecognition.png")
        img_bottom=img_bottom.resize((1230,260),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=20,y=365,width=1230,height=260)

        title_lbl=Label(self.root,bg="lightgreen")
        title_lbl.place(x=20,y=625,width=1230,height=15)
        
    
    def train_classifier(self):
        data_dir = (r"data")
        path=[os.path.join(data_dir,file) for  file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')  # grAY SCALE image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #=============================Train the classifier and save =============================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        
        cv2.destroyAllWindows()
        speak_va("Training datasets completed successfully!")
        messagebox.showinfo("Result","Training datasets completed successfully!",parent=self.root)
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()