from tkinter import*
from tkinter import ttk
import tkinter
from tkinter import messagebox
from PIL import Image , ImageTk
from r import Face_Recognition
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root

        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")
   
    
    #bg image

        img = Image.open(r"C:\Users\lenovo\Downloads\Face_Emotion_Recognition_Machine_Learning-main (1)\Face_Emotion_Recognition_Machine_Learning-main\images\bgg.png")
        img = img.resize((1690,710), Image.ANTIALIAS )
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg) 
        f_lbl.place(x=0,y=0,width=1690,height=710)

#title heading

        title_lbl=Label(f_lbl,text="FACE  EMOTION  RECOGNITION  SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="orange")
        title_lbl.place(x=0,y=0,width=1690,height=45)
       #button 
        img1 = Image.open(r"C:\Users\lenovo\Downloads\Face_Emotion_Recognition_Machine_Learning-main (1)\Face_Emotion_Recognition_Machine_Learning-main\images\logo-img.png")
        img1 = img1.resize((220,220), Image.ANTIALIAS )
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1 = Button(f_lbl, image =  self.photoimg1,cursor="hand2",command=self.student_details)
        b1.place(x=100,y=100,width=220,height=220)
        b1_1=Button(f_lbl,text="Realtime Emotion", cursor="hand2",command=self.student_details,font=("times new roman",15,"bold"),bg="dark blue",fg="white") 
        b1_1.place(x=100,y=300,width=220,height=40)
        #button 2 help
        #img2 = Image.open(r"C:\Users\lenovo\Downloads\Face_Emotion_Recognition_Machine_Learning-main (1)\Face_Emotion_Recognition_Machine_Learning-main\images\helpdesk.png")
        #self.photoimg2=ImageTk.PhotoImage(img2)

        #b1 = Button(f_lbl, image =  self.photoimg2)
        #b1.place(x=400,y=100,width=220,height=220)
        #b1_1=Button(f_lbl,text="help  desk", cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white") 
       # b1_1.place(x=400,y=300,width=220,height=40)
        #exit button 
        img3 = Image.open(r"C:\Users\lenovo\Downloads\Face_Emotion_Recognition_Machine_Learning-main (1)\Face_Emotion_Recognition_Machine_Learning-main\images\ex.png" )
        img3 = img3.resize((220,220), Image.ANTIALIAS )
        self.photoimg3=ImageTk.PhotoImage(img3)

        b1 = Button(f_lbl, image =  self.photoimg3,command = self.iExit)
        b1.place(x=400,y=100,width=220,height=220)
        b1_1=Button(f_lbl,text="EXIT", command = self.iExit, cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white") 
        b1_1.place(x=400,y=300,width=220,height=40)

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Emotion Recognition"," Are you sure exit the project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

   