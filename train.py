from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="Chocolate",fg="Black")
        title_lbl.place(x=0,y=0,width=1450,height=45)

        img=Image.open(r"C:\Users\user\Desktop\FACE-REGONITION\College_Image\7.jpg")
        img=img.resize((2200,896),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb=Label(self.root,image=self.photoimg)
        f_lb.place(x=0,y=40,width=2000,height=900)


        b0_1=Button(f_lb,text="TRAIN DATA",cursor="hand2",command=self.train_classifier,font=("times new roman",15,"bold"),bg="chocolate",fg="Black",borderwidth = 7)
        b0_1.place(x=620,y=600,width=150,height=40)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray Scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)

        #======================= Train the classifier===================

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("result","Training dataset completed!!")








if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
