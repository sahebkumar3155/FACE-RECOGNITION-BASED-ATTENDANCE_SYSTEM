from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from student import Student
import os
import tkinter.messagebox as mb
from train import Train
from face_recog import face_Reco
from attendances import attendance
from Developer import Developer

class face_recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # Fixed geometry dimensions
        self.root.title("Face Recognition System")


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

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new romain",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        
        # buttom for student buttom 1
        imag4=Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\button.jpg")
        # resize the image and descrize the image quality
        imag4=imag4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(imag4)

        b1=Button(bg_img,image=self.photoimg4,command=self.open_student_details_window,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.open_student_details_window,cursor="hand2",font=("times new romain",15,"bold"),bg="white",fg="black")
        b1_1.place(x=200,y=300,width=220,height=40)


        # face detact student buttom 2
        imag5=Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\buttom1.jpg")
        # resize the image and descrize the image quality
        imag5=imag5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(imag5)

        b1=Button(bg_img,image=self.photoimg5,command=self.face_Data,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",command=self.face_Data,cursor="hand2",font=("times new romain",15,"bold"),bg="white",fg="black")
        b1_1.place(x=500,y=300,width=220,height=40)


        # face detact student buttom 3
        imag6=Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\button.jpg")
        # resize the image and descrize the image quality
        imag6=imag6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(imag6)

        b1=Button(bg_img,image=self.photoimg6,command=self.attendance_details,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",command=self.attendance_details,cursor="hand2",font=("times new romain",15,"bold"),bg="white",fg="black")
        b1_1.place(x=800,y=300,width=220,height=40)

        
        # face detact student buttom 4
        imag7=Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\buttom4.jpg")
        # resize the image and descrize the image quality
        imag7=imag7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(imag7)

        b1=Button(bg_img,image=self.photoimg7,command=self.developer_details,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",command=self.developer_details,cursor="hand2",font=("times new romain",15,"bold"),bg="white",fg="black")
        b1_1.place(x=1100,y=300,width=220,height=40)


        # face detact student buttom 5
        imag8=Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\buttom5.jpg")
        # resize the image and descrize the image quality
        imag8=imag8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(imag8)

        b1=Button(bg_img,image=self.photoimg8,command=self.open_img,cursor="hand2")
        b1.place(x=200,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",command=self.open_img,cursor="hand2",font=("times new romain",15,"bold"),bg="white",fg="black")
        b1_1.place(x=200,y=600,width=220,height=40)

        
        # face detact student buttom 6
        imag9=Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\button.jpg")
        # resize the image and descrize the image quality
        imag9=imag9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(imag9)

        b1=Button(bg_img,image=self.photoimg9,command=self.train_data,cursor="hand2")
        b1.place(x=500,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new romain",15,"bold"),bg="white",fg="black")
        b1_1.place(x=500,y=600,width=220,height=40)


        # face detact student buttom 7
        imag10=Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\button.jpg")
        # resize the image and descrize the image quality
        imag10=imag10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(imag10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Help Center",cursor="hand2",font=("times new romain",15,"bold"),bg="white",fg="black")
        b1_1.place(x=800,y=600,width=220,height=40)


        # face detact student buttom 8
        imag11=Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\button.jpg")
        # resize the image and descrize the image quality
        imag11=imag11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(imag11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new romain",15,"bold"),bg="white",fg="black")
        b1_1.place(x=1100,y=600,width=220,height=40)

    

    # ========== photo button work ==========
    def open_img(self):
        directory = r"L:\alpha batch 5.0\python for placement\face recognition attendence system\data"
        try:
            if os.path.exists(directory) and os.listdir(directory):
                os.startfile(directory)
            else:
                mb.showwarning("Directory Error", "The 'data' directory does not exist or is empty.")
        except Exception as e:
            mb.showerror("Error", f"An error occurred: {str(e)}")




        # =======================Functiono Button=============================


    def open_student_details_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    # ===========train data=============
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    # =============face data==============
    def face_Data(self):
        self.new_window=Toplevel(self.root)
        self.app=face_Reco(self.new_window)

    # =============face data==============
    def attendance_details(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance(self.new_window)

    # ===========Developer Details========
    def developer_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)





if __name__ == "__main__":
    root = Tk()
    obj = face_recognition_system(root)
    root.mainloop()

