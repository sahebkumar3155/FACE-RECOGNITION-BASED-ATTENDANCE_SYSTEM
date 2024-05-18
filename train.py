from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from student import Student
import os
import tkinter.messagebox as mb
import mysql.connector
import cv2
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # Fixed geometry dimensions
        self.root.title("Face Recognition System Train Data")


        title_lbl=Label(self.root,text="Image Dataset Training",font=("times new romain",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=10,width=1530,height=60)


        # left label frame
        left_frame=LabelFrame(self.root,bd=2,bg="white",relief=RIDGE,text="Train Data",font=("times new roman",12,"bold"))
        left_frame.place(x=20,y=75,width=725,height=710)

        imag_left0=Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\tain_data1.jpg")
        # resize the image and descrize the image quality
        imag_left0=imag_left0.resize((720,230),Image.ANTIALIAS)
        self.photoimgr_left0=ImageTk.PhotoImage(imag_left0)

        f_lbl=Label(left_frame,image=self.photoimgr_left0)
        f_lbl.place(x=2,y=0,width=712,height=230)

        imag_left1=Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\tainimage2.jpg")
        # resize the image and descrize the image quality
        imag_left1=imag_left1.resize((720,230),Image.ANTIALIAS)
        self.photoimgr_left1=ImageTk.PhotoImage(imag_left1)

        f_lbl=Label(left_frame,image=self.photoimgr_left1)
        f_lbl.place(x=2,y=232,width=712,height=230)

        imag_left2=Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\train_img3.png")
        # resize the image and descrize the image quality
        imag_left2=imag_left2.resize((720,230),Image.ANTIALIAS)
        self.photoimgr_left2=ImageTk.PhotoImage(imag_left2)

        f_lbl=Label(left_frame,image=self.photoimgr_left2)
        f_lbl.place(x=2,y=465,width=712,height=230)


        # right label frame
        Right_frame=LabelFrame(self.root,bd=2,bg="white",relief=RIDGE,text="Train Data",font=("times new roman",12,"bold"))
        Right_frame.place(x=755,y=75,width=755,height=710)

        # face detact student buttom 4
        # imag7=Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\buttom4.jpg")
        # # resize the image and descrize the image quality
        # imag7=imag7.resize((220,220),Image.ANTIALIAS)
        # self.photoimg7=ImageTk.PhotoImage(imag7)

        # b1=Button(Right_frame,image=self.photoimg7,cursor="hand2")
        # b1.place(x=250,y=350,width=220,height=220)

        b1_12=Button(Right_frame,text="Train Data",cursor="hand2",command=self.train_classifier,font=("times new romain",40,"bold"),bg="black",fg="#f2a02e")
        b1_12.place(x=10,y=300,width=735,height=50)



    def train_classifier(self):
        data_dir = r"L:\alpha batch 5.0\python for placement\face recognition attendence system\data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L') # Convert to grayscale
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # Train the classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        mb.showinfo("Training Completed", "Image dataset training completed successfully!")





if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()

