import tkinter
import string
import random
import pyperclip

#create root window
root=tkinter.Tk()
root.title("Password Generator")
root.eval("tk::PlaceWindow . center")
root.geometry('225x100')

#creating variables
root_color="peachpuff"

#reconfigure root
root.config(bg=root_color)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)


#create function
def generate():
   password=""
   digits=string.digits
   lower_case=string.ascii_lowercase
   upper_case=string.ascii_uppercase
   characters='!@#$%^&*()'
   main_string=digits+lower_case+upper_case+characters
   main_list=list(main_string)
   random.shuffle(main_list)
   pwd_len=random.randint(8,15)
   for i in range(pwd_len):
       password=password+random.choice(main_list)

   lbl_pwd.config(text=password)

def copy():
    random_pwd=lbl_pwd.cget('text')
    pyperclip.copy(random_pwd)

#create layout

#create widgets
lbl_pwd=tkinter.Label(root,text="To be Updated",bg="black",fg="white")
btn_generate=tkinter.Button(root,text="Generate",command=generate)
btn_copy=tkinter.Button(root,text="Copy",command=copy)

lbl_pwd.grid(row=0,column=0,columnspan=2,sticky='EW',padx=20,pady=20)
btn_generate.grid(row=1,column=0,pady=(0,20),ipadx=10)
btn_copy.grid(row=1,column=1,pady=(0,20),ipadx=15)


#run mainloop
root.mainloop()