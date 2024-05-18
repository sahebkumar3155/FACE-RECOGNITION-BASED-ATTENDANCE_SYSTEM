from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import cv2
import mysql.connector
from datetime import datetime
from time import strftime
import csv

class face_Reco:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # Fixed geometry dimensions
        self.root.title("Face Recognition System Train Data")

        title_lbl = Label(self.root, text="Image Dataset Training", font=("times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=10, width=1530, height=60)

        imag3 = Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\back_train.jpg")
        imag3 = imag3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(imag3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=70, width=1530, height=710)

        imag4 = Image.open(r"L:\alpha batch 5.0\python for placement\face recognition attendence system\all image\train2.jpg")
        imag4 = imag4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(imag4)

        b1 = Button(self.root, image=self.photoimg4, command=self.face_recogn, cursor="hand2")
        b1.place(x=1200, y=250, width=220, height=220)

        b1_1 = Button(self.root, text="Face Detect", cursor="hand2", command=self.face_recogn, font=("times new romain", 15, "bold"), bg="white", fg="black")
        b1_1.place(x=1200, y=450, width=220, height=40)

    #=====================Attendance===================

    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list))and ((i not in name_list)) and ((n not in name_list)) and ((d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r}, {n}, {d}, {dtString}, {d1}, Present")
    def face_recogn(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord=[]

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Saheb@315596", database="face_recognizer")
                my_cursor = conn.cursor()


                my_cursor.execute("SELECT student_id FROM student WHERE student_id = %s", (str(id),))
                i = my_cursor.fetchone()
                if i is not None:
                    i = "+".join(d)
                else:
                    i = "Unknown"

                my_cursor.execute("SELECT student_Name FROM student WHERE student_id = %s", (str(id),))
                n = my_cursor.fetchone()
                if n is not None:
                    n = "+".join(n)
                else:
                    n = "Unknown"

                my_cursor.execute("SELECT Roll_No FROM student WHERE student_id = %s", (str(id),))
                r = my_cursor.fetchone()
                if r is not None:
                    r = "+".join(r)
                else:
                    r = "Unknown"

                my_cursor.execute("SELECT Department FROM student WHERE student_id = %s", (str(id),))
                d = my_cursor.fetchone()
                if d is not None:
                    d = "+".join(d)
                else:
                    d = "Unknown"


                if confidence > 77:
                    cv2.putText(img, f"id: {i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 3)
                    cv2.putText(img, f"roll: {r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 3)
                    cv2.putText(img, f"dep: {d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord=[x,y,w,y]
            

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_capture = cv2.VideoCapture(0)

        while True:
            ret, img = video_capture.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = face_Reco(root)
    root.mainloop()
