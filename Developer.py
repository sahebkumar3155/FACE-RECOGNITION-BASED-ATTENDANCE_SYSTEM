from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from student import Student
import os
import tkinter.messagebox as mb
from train import Train
from face_recog import face_Reco
from attendances import attendance

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # Fixed geometry dimensions
        self.root.title("Developer Details")


        # first image
        imag=Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\ggi.jpg")
        # resize the image and descrize the image quality
        imag=imag.resize((500,130),Image.ANTIALIAS)
        self.photoimgr=ImageTk.PhotoImage(imag)

        f_lbl=Label(self.root,image=self.photoimgr)
        f_lbl.place(x=0,y=0,width=500,height=130)


        # second  image
        imag1=Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\berojgar.jpg")
        # resize the image and descrize the image quality
        imag1=imag1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(imag1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


        # third image
        imag2=Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\iNurture.jpg")
        # resize the image and descrize the image quality
        imag2=imag2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(imag2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)


        # background image
        imag3=Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\bg1.jpg")
        # resize the image and descrize the image quality
        imag3=imag3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(imag3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="Developer Details",font=("times new romain",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        
        # button for student details
        imag4=Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\button.jpg")
        # resize the image and descrize the image quality
        imag4=imag4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(imag4)

        b1=Button(bg_img,image=self.photoimg4,command=self.open_student_details_window,cursor="hand2")
        b1.place(x=250,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Saheb Kumar",command=self.open_student_details_window,cursor="hand2",font=("times new romain",15,"bold"),bg="white",fg="black")
        b1_1.place(x=250,y=300,width=220,height=40)


        # button for face data
        imag5=Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\buttom1.jpg")
        # resize the image and descrize the image quality
        imag5=imag5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(imag5)

        b2=Button(bg_img,image=self.photoimg5,command=self.face_Data,cursor="hand2")
        b2.place(x=550,y=100,width=220,height=220)

        b2_1=Button(bg_img,text="Maaz ahamad",command=self.face_Data,cursor="hand2",font=("times new romain",15,"bold"),bg="white",fg="black")
        b2_1.place(x=550,y=300,width=220,height=40)


        # button for attendance details
        imag6=Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\button.jpg")
        # resize the image and descrize the image quality
        imag6=imag6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(imag6)

        b3=Button(bg_img,image=self.photoimg6,command=self.attendance_details,cursor="hand2")
        b3.place(x=850,y=100,width=220,height=220)

        b3_1=Button(bg_img,text="Pradeep Kumar",command=self.attendance_details,cursor="hand2",font=("times new romain",15,"bold"),bg="white",fg="black")
        b3_1.place(x=850,y=300,width=220,height=40)

    def open_student_details_window(self):
        # Implement this method to open student details window
        pass

    def face_Data(self):
        # Implement this method for face data
        pass

    def attendance_details(self):
        # Implement this method for attendance details
        pass

if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
