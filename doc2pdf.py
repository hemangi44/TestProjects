from tkinter import *
from docx2pdf import convert
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import *

root=Tk()
root.title("Word to PDF converter")

def openFile():
    file = askopenfile(filetypes=[("Word Files",'*.docx')])
    convert(file.name,r'E:\workspace\Python Classes\demo\doc123.pdf')
    showinfo("DONE","File Successfully Converted")
    return
   

label=Label(root,text="Choose File: ")
label.grid(row=0,column=0,padx=5,pady=5)

button=Button(root,text="Select",width=30,command=openFile)
button.grid(row=0,column=1,padx=5,pady=5)


root.mainloop()
  