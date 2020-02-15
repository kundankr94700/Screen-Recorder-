import cv2
import numpy as np
import os
import pyautogui
from tkinter import *
from tkinter import messagebox
from tkinter.font import  Font
from PIL import ImageTk, Image
from os import listdir,mkdir
from os.path import isfile, join
try:
 mkdir('D:/Screen_Record/')
except:
 pass
output = "D:\\Screen_Record\\video.avi"
img = pyautogui.screenshot()
img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
height, width, channels = img.shape
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))
def abc():

 a =messagebox.showinfo('Screen Recording Application','Press Q To Stop Recording ')
 root.destroy()


 while(True):
  try:
   img = pyautogui.screenshot()
   image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
   out.write(image)
   img_frame = image[0:20, 0:20]
   cv2.imshow('H',img_frame)
   StopIteration(0.5)
  except KeyboardInterrupt:
   break
  if cv2.waitKey(1) == ord('q') :
    break

 out.release()
 cv2.destroyAllWindows()
 def get_file_name():
  s1=ss1.get()
  onlyfiles = [f for f in listdir("D:\\Screen_Record\\") if isfile(join("D:\\Screen_Record\\", f))]

  if s1== '':
   messagebox.showinfo("Face Recognition Software ", "PLease Enter the Name of File First !")
  else:
   if s1+".avi" in onlyfiles:
    messagebox.showinfo("Face Recognition Software ", "Name Already Exist!")
   else:
    os.rename(output,"D:\\Screen_Record\\%s.avi"%(s1))
    messagebox.showinfo("Screen Recording Application","Video Saved Successfully")
    t1.destroy()

 t1 = Tk()
 t1.geometry('500x130+500+100')
 t1.title('Screen Recording Application')
 l3 = Label(t1, text=" Save File As ", fg='green', font=f1, bg='white').place(x=80, y=50)
 ss1 = StringVar()
 e1 = Entry(t1, textvariable=ss1,font=f1).place(x=205, y=50)
 b1 = Button(t1, text='Save ', command=get_file_name, width=30, height=1, bg='Darkred', fg='white',
             font=f3).place(x=150, y=90)
 t1.mainloop()

root=Tk()
root.geometry('500x400+500+100')
frame=Frame(root,height=600,width=0).pack(side=LEFT)
img = ImageTk.PhotoImage(Image.open("screen.jpg"))
panel = Label(frame, image = img)
root.title('Screen Recording Application')
panel.pack(side = "right", fill = "both", expand = "yes")
f1 = Font(family="Time New Roman", size=12, weight="bold", underline=1)
f2 = Font(family="Time New Roman", size=15, weight="bold", underline=1)
f3 = Font(family="Time New Roman", size=10, weight="bold")
l3 = Label(root, text=" @Copywrite Kundan Kumar", fg='green', font=f1,bg='white').place(x=200, y=8)
b1 = Button(root, text='Start Recording Screen', command=abc, width=30, height=1, bg='Darkred', fg='white', font=f3).place(x=100,y=360)
root.mainloop()