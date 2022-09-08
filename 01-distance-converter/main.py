import tkinter

#create main window
root=tkinter.Tk()
root.eval("tk::PlaceWindow . center")

root.title("Distance Converter")
root.resizable(0,0)

#create variables
root_color="coral"
my_font=("Times New Roman",12)



#reconfig root
root.config(bg=root_color)

#create functions
def calculate():
    m_val=float(m_entry.get())
    #print(type(m_val))
    f_val=m_val*3.28084
    #print(f_val)
    ft_val.config(text=f_val)

#create layout
m_lbl=tkinter.Label(root,text="metre",bg=root_color,font=my_font)
m_entry=tkinter.Entry(root)
ft_lbl=tkinter.Label(root,text="feet",bg=root_color,font=my_font)
ft_val=tkinter.Label(root,text="",bg='black',font=my_font,fg='white')
btn_calculate=tkinter.Button(root,text="Calculate",command=calculate)

m_lbl.grid(row=0,column=0,padx=10,pady=(10,0))
m_entry.grid(row=0,column=1,padx=10,pady=(10,0))
ft_lbl.grid(row=1,column=0,padx=10,pady=(10,0))
ft_val.grid(row=1,column=1,padx=10,pady=(10,0))
btn_calculate.grid(row=2,column=0,columnspan=2,sticky='WE',padx=10,pady=10)


#run mainloop
root.mainloop()