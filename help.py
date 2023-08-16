from tkinter import*
from PIL import Image,ImageTk


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x700+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="HELP DESK",font=("Algerian",30,"bold"),bg="light blue",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1400,height=45)
        
        bg_img= Image.open(r"college_images\help.jpeg")
        bg_img=bg_img.resize((1400,600),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(bg_img)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1400,height=600)

        dev_lbl=Label(f_lbl,text="Email:amankumar909828@gmail.com",font=("times new roman",20,"bold"),bg="black",fg="white")
        dev_lbl.place(x=465,y=150)


if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()