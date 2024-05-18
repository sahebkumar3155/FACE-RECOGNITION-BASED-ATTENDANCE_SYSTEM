from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
# --------------------------
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


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")

        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\loginBg1.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame1= Frame(self.root,bg="#002B53")
        frame1.place(x=560,y=170,width=340,height=450)

        img1=Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\log1.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1,bg="#002B53")
        lb1img1.place(x=690,y=175, width=100,height=100)

        get_str = Label(frame1,text="Login",font=("times new roman",20,"bold"),fg="white",bg="#002B53")
        get_str.place(x=140,y=100)

        #label1 
        username =lb1= Label(frame1,text="Username:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        username.place(x=30,y=160)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtuser.place(x=33,y=190,width=270)


        #label2 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        pwd.place(x=30,y=230)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=33,y=260,width=270)


        # Creating Button Login
        loginbtn=Button(frame1,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#002B53",bg="white",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=33,y=320,width=270,height=35)


        # Creating Button Registration
        loginbtn=Button(frame1,command=self.reg,text="Register",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=33,y=370,width=50,height=20)


        # Creating Button Forget
        loginbtn=Button(frame1,command=self.forget_pwd,text="Forget",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=90,y=370,width=50,height=20)


    #  THis function is for open register window
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if (self.txtuser.get() == "" or self.txtpwd.get() == ""):
            messagebox.showerror("Error", "All fields are required!")
        elif (self.txtuser.get() == "admin" and self.txtpwd.get() == "admin"):
            messagebox.showinfo("Success", "Welcome to Attendance Management System Using Facial Recognition")
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(username='root', password='Saheb@315596',host='localhost',database='face_recognizer',port=3306)
            mycursor = conn.cursor()
            mycursor.execute("select * from registration where Email=%s and Password=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_min=messagebox.askyesno("YesNo","Access only Admin")
                if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=face_recognition_system(self.new_window)
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()
#=======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(username='root', password='Saheb@315596',host='localhost',database='face_recognizer',port=3306)
            mycursor = conn.cursor()
            query=("select * from registration where Email=%s and SecurityQ=%s and SecurityA=%s")
            value=(self.txtuser.get(),self.var_ssq.get(),self.var_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("update registration set Password=%s where Email=%s")
                value=(self.var_pwd.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
                



# =====================Forget window=========================================
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")
        else:
            conn = mysql.connector.connect(username='root', password='Saheb@315596',host='localhost',database='face_recognizer',port=3306)
            mycursor = conn.cursor()
            query=("select * from registration where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x400+610+170")
                l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                ssq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                ssq.place(x=70,y=80)

                #Combo Box1
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                sa.place(x=70,y=150)

                #entry2 
                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=70,y=180,width=270)

                #label2 
                new_pwd =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_pwd.place(x=70,y=220)

                #entry2 
                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=70,y=300,width=270,height=35)


            

# =====================main program Face deteion system====================

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

    
    def open_img(self):
        os.startfile("dataset")
    
  




if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.mainloop()