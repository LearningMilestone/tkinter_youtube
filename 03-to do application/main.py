#import
import tkinter
from PIL import Image,ImageTk
from tkinter import END,ANCHOR

#create main window
root=tkinter.Tk()
root.title("To Do List")
root.geometry("350x450")

#variable
root_color="#FFB200"
title_font=("Segoe Script",22,"roman")
btn_color="#7FBCD2"
btn_font=("Times New Roman",12)


#configure window
root.config(bg=root_color)

#create function

def add_item():
    value=add_entry.get()
    list_box.insert(END,value)
    add_entry.delete(0,END)

def remove_item():
    #x=list_box.curselection()
    list_box.delete(ANCHOR)

def clear():
    list_box.delete(0,END)

def save():
    x=list_box.get(0,END)
    with open("tasklist.txt","w") as f:

        for item in x:
            if item.endswith("\n"):
                f.write(item)
            else:
                f.write(item+"\n")

def open_app():
    try:
        with open("tasklist.txt","r") as f:
            content=f.readlines()
            for item in content:
                list_box.insert(END,item)

    except FileNotFoundError:
        pass

#create layout

#create title frame and its elements
frame_title=tkinter.Frame(root,bg=root_color)
lbl_title=tkinter.Label(frame_title,text="My To Do List",bg=root_color,font=title_font)
#Add Image
img_1=Image.open("logo.png")
img_1.thumbnail((100,100))
img=ImageTk.PhotoImage(img_1)
#lbl_img=tkinter.Label(frame_title,image=img)
canvas=tkinter.Canvas(frame_title,width=100,height=100,bg=root_color,highlightthickness=0)
canvas.create_image((50,50),image=img)

#place on the window
lbl_title.grid(row=0,column=0)
#lbl_img.grid(row=1,column=0)
canvas.grid(row=1,column=0)


#add items frame
frame_input=tkinter.Frame(root,bg=root_color)
#add entry and button widget
add_entry=tkinter.Entry(frame_input,width=25,font=btn_font)
add_btn=tkinter.Button(frame_input,text="Add Item",bg=btn_color,font=btn_font,command=add_item)

add_entry.grid(row=0,column=0,padx=5)
add_btn.grid(row=0,column=1,padx=5,ipadx=5)

frame_output=tkinter.Frame(root)
my_scrollbar=tkinter.Scrollbar(frame_output)
list_box=tkinter.Listbox(frame_output,width=45,height=8)

list_box.grid(row=0,column=0)
my_scrollbar.grid(row=0,column=1,sticky='NS')

list_box.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=list_box.yview)

frame_management=tkinter.Frame(root,bg=root_color)
btn_rem=tkinter.Button(frame_management,text="Remove",font=btn_font,bg=btn_color,command=remove_item)
btn_clear=tkinter.Button(frame_management,text="Clear",font=btn_font,bg=btn_color,command=clear)
btn_save=tkinter.Button(frame_management,text="Save",font=btn_font,bg=btn_color,command=save)
btn_quit=tkinter.Button(frame_management,text="Quit",font=btn_font,bg=btn_color,command=root.destroy)

btn_rem.grid(row=0,column=0,padx=5,ipadx=5)
btn_clear.grid(row=0,column=1,padx=5,ipadx=8)
btn_save.grid(row=0,column=2,padx=5,ipadx=10)
btn_quit.grid(row=0,column=3,padx=5,ipadx=10)



frame_title.pack(padx=10,pady=10)
frame_input.pack(padx=10,pady=10)
frame_output.pack(padx=10,pady=10)
frame_management.pack(padx=10,pady=10)

open_app()

#mainloop
root.mainloop()
