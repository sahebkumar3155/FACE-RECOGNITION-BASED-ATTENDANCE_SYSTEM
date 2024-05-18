from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # Fixed geometry dimensions
        self.root.title("Face Recognition System")


        # =================variable=====================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_section=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_Phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()



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

        title_lbl=Label(bg_img,text="Student Details",font=("times new romain",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=5,width=1530,height=45)


        # frame create
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=60,width=1510,height=620)

        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=25,y=10,width=720,height=580)


        imag_left=Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\student.jpg")
        # resize the image and descrize the image quality
        imag_left=imag_left.resize((720,130),Image.ANTIALIAS)
        self.photoimgr_left=ImageTk.PhotoImage(imag_left)

        f_lbl=Label(left_frame,image=self.photoimgr_left)
        f_lbl.place(x=2,y=0,width=712,height=130)


        # current course details
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=2,y=135,width=712,height=115)

        # Department
        deep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        deep_label.grid(row=0,column=0,padx=10)

        deep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        deep_combo["values"]=("select Department","Computer science","IT","civil","Mechnical","Data science")
        deep_combo.current(0)
        deep_combo.grid(row=0,column=1,padx=2,pady=10)


        # Course
        deep_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        deep_label.grid(row=0,column=3,padx=10)

        deep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        deep_combo["values"]=("select Course","Data Science","IOT","Civil","Mechnical","AI&Ml")
        deep_combo.current(0)
        deep_combo.grid(row=0,column=4,padx=2,pady=10)

        # Year
        deep_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        deep_label.grid(row=1,column=0,padx=10)

        deep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        deep_combo["values"]=("select Year","2023-2024","2024-2025","2025-2026","2026-2027")
        deep_combo.current(0)
        deep_combo.grid(row=1,column=1,padx=2,pady=10)


        # Semester
        deep_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        deep_label.grid(row=1,column=3,padx=10)

        deep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        deep_combo["values"]=("select Semester","1st Sem","2nd Sem")
        deep_combo.current(0)
        deep_combo.grid(row=1,column=4,padx=2,pady=10)


        # Student Class Information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Student Class Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=2,y=255,width=712,height=300)


        # student id
        stuedentId_label=Label(class_student_frame,text="Unique ID:",font=("times new roman",12,"bold"),bg="white")
        stuedentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5)


        # student Name
        stuedentName_label=Label(class_student_frame,text="Studen Name:",font=("times new roman",12,"bold"),bg="white")
        stuedentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5)


        # Class Section
        Class_division_label=Label(class_student_frame,text="Class Section:",font=("times new roman",12,"bold"),bg="white")
        Class_division_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        section_combo=ttk.Combobox(class_student_frame,textvariable=self.var_section,font=("times new roman",12,"bold"),state="readonly")
        section_combo["values"]=("select Section","A","B","C","D")
        section_combo.current(0)
        section_combo.grid(row=1,column=1)


        # Roll No
        Roll_No_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        Roll_No_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Roll_No_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        Roll_No_entry.grid(row=1,column=3,padx=10,pady=5)


        # Gender
        stuedent_gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        stuedent_gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        # student_gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        # student_gender_entry.grid(row=2,column=1,padx=10,pady=5)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly")
        gender_combo["values"]=("select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1)


        # DOB
        stuedent_DOB_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        stuedent_DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        student_DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        student_DOB_entry.grid(row=2,column=3,padx=10,pady=5)


        # Email
        stuedent_email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        stuedent_email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        student_email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        student_email_entry.grid(row=3,column=1,padx=10,pady=5)


        # Contact No.
        stuedent_contact_label=Label(class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        stuedent_contact_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        student_contact_entry=ttk.Entry(class_student_frame,textvariable=self.var_Phone,width=20,font=("times new roman",12,"bold"))
        student_contact_entry.grid(row=3,column=3,padx=10,pady=5)



        # Address:
        stuedent_Address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        stuedent_Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        student_Address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        student_Address_entry.grid(row=4,column=1,padx=10,pady=5)


        # Teacher Names
        stuedent_Teacher_label=Label(class_student_frame,text="Teacher's Name:",font=("times new roman",12,"bold"),bg="white")
        stuedent_Teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        student_Teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        student_Teacher_entry.grid(row=4,column=3,padx=10,pady=5)


        # radio Buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take Photo Sample",value="Yes")
        radionbtn1.grid(row=5,column=0,padx=10,pady=5)

        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radionbtn1.grid(row=5,column=1,padx=10,pady=5)


        # buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=708,height=35)

        save_button=Button(btn_frame,width=17,command=self.add_data,text="Save",font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_button.grid(row=0,column=0)

        Update_button = Button(btn_frame, width=17, text="Update", command=self.update_data,font=("times new roman", 13, "bold"), bg="blue", fg="white")
        Update_button.grid(row=0,column=1)

        Delate_button=Button(btn_frame,width=17,text="Delete",command=self.delete_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Delate_button.grid(row=0,column=2)

        Reset_button=Button(btn_frame,width=17,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Reset_button.grid(row=0,column=3)

        # buttons frame
        btn1_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn1_frame.place(x=0,y=245,width=708,height=35)

        # Addphoto sample
        addphoto_sample=Button(btn1_frame,width=35,command=self.generate_dataset,text="Take Photo Sample",font=("times new roman",13,"bold"),bg="blue",fg="white")
        addphoto_sample.grid(row=0,column=0)

        addphotoUpdate_sample=Button(btn1_frame,width=35,text="Update Photo Sample",font=("times new roman",13,"bold"),bg="blue",fg="white")
        addphotoUpdate_sample.grid(row=0,column=1)




        # right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=755,y=10,width=720,height=580)

        #=======Search System=============
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Current Course information",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=5,width=708,height=75)

        search_label=Label(Search_frame,text="Search By",width=12,height=2,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5)

        Search_combo=ttk.Combobox(Search_frame,width=12,font=("times new roman",15,"bold"),state="readonly")
        Search_combo["values"]=("select","Unique ID","Roll No","Phone No","dfs")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10)

        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5)

        Search_button=Button(Search_frame,width=13,text="Search",font=("times new roman",12,"bold"),bg="blue",fg="white")
        Search_button.grid(row=0,column=3,padx=5)

        Showall_button=Button(Search_frame,width=13,text="Search All",font=("times new roman",12,"bold"),bg="blue",fg="white")
        Showall_button.grid(row=0,column=4,padx=5)


        #=======Table frame=============
        Table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        Table_frame.place(x=5,y=90,width=708,height=450)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(Table_frame,columns=("Department","Course","Year","Semester","Unique ID","Student Name","Class Section","Roll No","Gender","DOB","Email","Phone No","Address","Teacher's Name","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Years")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Unique ID",text="Unique ID")
        self.student_table.heading("Student Name",text="Student Name")
        self.student_table.heading("Class Section",text="Class Section")
        self.student_table.heading("Roll No",text="Roll No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone No",text="Phone No")
        self.student_table.heading("Address",text="Adsress")
        self.student_table.heading("Teacher's Name",text="Teacher's Name")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("Department",width=150)
        self.student_table.column("Course",width=150)
        self.student_table.column("Year",width=150)
        self.student_table.column("Semester",width=150)
        self.student_table.column("Unique ID",width=150)
        self.student_table.column("Student Name",width=150)
        self.student_table.column("Class Section",width=150)
        self.student_table.column("Roll No",width=150)
        self.student_table.column("Gender",width=150)
        self.student_table.column("DOB",width=150)
        self.student_table.column("Email",width=150)
        self.student_table.column("Phone No", width=150)
        self.student_table.column("Address",width=150)
        self.student_table.column("Teacher's Name",width=150)
        self.student_table.column("Photo",width=150)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    # ========function============
    def add_data(self):
        if self.var_dep.get()=="select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Saheb@315596",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_semester.get(),
                                                                                            self.var_std_id.get(),
                                                                                            self.var_std_name.get(),
                                                                                            self.var_section.get(),
                                                                                            self.var_roll.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_Phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get()
                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



    # ============fetch data========================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Saheb@315596",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    # ===============get cursor=============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_section.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_Phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


    # =========update funciton ===========
        
    def update_data(self):
        if self.var_dep.get() == "select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student detail", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Saheb@315596",
                                                database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE student SET Department=%s, Course=%s, Year=%s, Semester=%s,student_Name=%s,class_Section=%s, Roll_No=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher_Name=%s, Photo=%s WHERE student_id=%s",
                                        (
                                            self.var_dep.get(),
                                            self.var_course.get(),
                                            self.var_year.get(),
                                            self.var_semester.get(),
                                            self.var_std_name.get(),
                                            self.var_section.get(),
                                            self.var_roll.get(),
                                            self.var_gender.get(),
                                            self.var_dob.get(),
                                            self.var_email.get(),
                                            self.var_Phone.get(),
                                            self.var_address.get(),
                                            self.var_teacher.get(),
                                            self.var_radio1.get(),
                                            self.var_std_id.get()  # Add this line to pass std_id
                                        ))

                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully update completed", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # ============Delete data=======
    # ============Delete data=======
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete page", "Do you want to delete this student", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Saheb@315596",
                                                    database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where student_id=%s"  # Corrected typo from 'form' to 'from'
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)  # Corrected the parameter passing here
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
    # ============reset button============
    def reset_data(self):
        self.var_dep.set("select department")
        self.var_course.set("select course")
        self.var_year.set("select year")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_section.set("select section")
        self.var_roll.set(" ")
        self.var_gender.set("select gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_Phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
    # ===================generate data set or take photo samples==============
    def generate_dataset(self):
        if self.var_dep.get() == "select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Saheb@315596",
                                                database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("UPDATE student SET Department=%s, Course=%s, Year=%s, Semester=%s, class_Section=%s, Roll_No=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher_Name=%s, Photo=%s WHERE student_id=%s",
                                        (
                                            self.var_dep.get(),
                                            self.var_course.get(),
                                            self.var_year.get(),
                                            self.var_semester.get(),
                                            self.var_section.get(),
                                            self.var_roll.get(),
                                            self.var_gender.get(),
                                            self.var_dob.get(),
                                            self.var_email.get(),
                                            self.var_Phone.get(),
                                            self.var_address.get(),
                                            self.var_teacher.get(),
                                            self.var_radio1.get(),
                                            self.var_std_id.get()==id+1  # Add this line to pass std_id
                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ============= Load predifiend data on face frontals from opencv===========
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.2, 5)
                    
                    for (x, y, w, h) in faces:  # Fixed variable name 'y' to 'h'
                        face_cropped = img[y:y+h, x:x+w]  # Fixed variable name 'y' to 'h' and 'y' to 'x'
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret, my_frame=cap.read()
                    if(face_cropped(my_frame)) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".png"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets compled!!!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)



    




if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
