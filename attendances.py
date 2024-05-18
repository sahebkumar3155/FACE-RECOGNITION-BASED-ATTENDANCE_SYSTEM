from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []

class attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # Fixed geometry dimensions
        self.root.title("attendance system")

        # ========text variable====
        # -----------Variables-------------------
        self.var_std_id=StringVar()
        self.var_roll=StringVar()
        self.var_std_name=StringVar()
        self.var_dep=StringVar()
        # self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()

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
        current_course_frame.place(x=2,y=135,width=712,height=400)

        # student id
        stuedentId_label=Label(current_course_frame,text="Unique ID:",font=("times new roman",12,"bold"),bg="white")
        stuedentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(current_course_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5)

        # student Name
        stuedentName_label=Label(current_course_frame,text="Studen Name:",font=("times new roman",12,"bold"),bg="white")
        stuedentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(current_course_frame,width=20,textvariable=self.var_std_name,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5)

        # Roll No
        Roll_No_label=Label(current_course_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        Roll_No_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Roll_No_entry=ttk.Entry(current_course_frame,width=20,textvariable=self.var_roll,font=("times new roman",12,"bold"))
        Roll_No_entry.grid(row=1,column=1,padx=10,pady=5)

        # Department
        Roll_No_label=Label(current_course_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        Roll_No_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Roll_No_entry=ttk.Entry(current_course_frame,width=20,textvariable=self.var_dep,font=("times new roman",12,"bold"))
        Roll_No_entry.grid(row=1,column=3,padx=10,pady=5)

        # Date
        Roll_No_label=Label(current_course_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        Roll_No_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Roll_No_entry=ttk.Entry(current_course_frame,width=20,textvariable=self.var_date,font=("times new roman",12,"bold"))
        Roll_No_entry.grid(row=3,column=1,padx=10,pady=5)

        # Time
        Roll_No_label=Label(current_course_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        Roll_No_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        Roll_No_entry=ttk.Entry(current_course_frame,width=20,textvariable=self.var_time,font=("times new roman",12,"bold"))
        Roll_No_entry.grid(row=3,column=3,padx=10,pady=5)

        # Attendance 
        Class_division_label=Label(current_course_frame,text="Attendance",font=("times new roman",12,"bold"),bg="white")
        Class_division_label.grid(row=5,column=0,padx=10,pady=5,sticky=W)

        section_combo=ttk.Combobox(current_course_frame,textvariable=self.var_attend,font=("times new roman",12,"bold"),state="readonly")
        section_combo["values"]=("select Section","Present","Absent")
        section_combo.current(0)
        section_combo.grid(row=5,column=1)

        # buttons frame
        btn_frame=Frame(current_course_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=165,width=708,height=35)

        save_button=Button(btn_frame,width=17,text="Import csv",command=self.importCsv,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_button.grid(row=6,column=0)

        Update_button = Button(btn_frame, width=17, text="Export csv",command=self.exportCsv,font=("times new roman", 13, "bold"), bg="blue", fg="white")
        Update_button.grid(row=6,column=1)

        Delate_button=Button(btn_frame,width=17,text="Update",command=self.update_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Delate_button.grid(row=6,column=2)

        Reset_button=Button(btn_frame,width=17,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Reset_button.grid(row=6,column=3)

        # Reset_button=Button(btn_frame,width=17,text="Reset",command=self.update_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        # Reset_button.grid(row=7,column=0)


        # right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=755,y=10,width=720,height=580)

        Table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        Table_frame.place(x=5,y=0,width=708,height=450)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(Table_frame,columns=("id","roll","name","department","date","time","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id",text="ID")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("department",text="Department")
        self.student_table.heading("date",text="Date")
        self.student_table.heading("time",text="Time")
        self.student_table.heading("attendance",text="Attendance")

        self.student_table["show"]="headings"

        self.student_table.column("id", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("department", width=100)
        self.student_table.column("date", width=100)
        self.student_table.column("time", width=100)
        self.student_table.column("attendance", width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor_right)



    def fetchData(self, rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("", END, values=i)

    # ======import the dada ===
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)

    # ========export the data==============
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 


    #  #=============Cursur Function for mysql========================

    def get_cursor_right(self, event=""):
        cursor_focus = self.student_table.focus()
        if cursor_focus:
            content = self.student_table.item(cursor_focus)
            data = content["values"]
            if data:
                self.var_std_id.set(data[0])
                self.var_roll.set(data[1])
                self.var_std_name.set(data[2])
                self.var_dep.set(data[3])
                self.var_time.set(data[4])
                self.var_date.set(data[5])
                self.var_attend.set(data[6]) 

    #============================Reset Data======================
    def reset_data(self):
        self.var_std_id.set("")
        self.var_roll.set("")
        self.var_std_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("Status")

    def update_data(self):
        if self.var_std_id.get() == "" or self.var_roll.get() == "" or self.var_std_name.get() == "" or self.var_time.get() == "" or self.var_date.get() == "" or self.var_attend.get() == "Status":
            messagebox.showerror("Error", "Please Fill All Fields are Required!", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to Update this Student Attendance?", parent=self.root)
                if Update:
                    for row in mydata:
                        if row[0] == self.var_std_id.get():
                            row[1] = self.var_roll.get()
                            row[2] = self.var_std_name.get()
                            row[3] = self.var_dep.get()
                            row[4] = self.var_date.get()
                            row[5] = self.var_time.get()
                            row[6] = self.var_attend.get()
                            break
                    messagebox.showinfo("Success", "Successfully Updated!", parent=self.root)
                    self.fetchData(mydata)  # Update Treeview with updated data
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID Must be Required!", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to Delete?", parent=self.root)
                if delete:
                    global mydata
                    for row in mydata:
                        if row[0] == self.var_std_id.get():
                            mydata.remove(row)
                            break
                    self.fetchData(mydata)  # Update Treeview with updated data
                    messagebox.showinfo("Delete", "Successfully Deleted!", parent=self.root)
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
            




if __name__ == "__main__":
    root = Tk()
    obj = attendance(root)
    root.mainloop()
