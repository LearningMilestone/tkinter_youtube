import tkinter
from PIL import Image,ImageTk
from tkinter import SUNKEN,END,X
import urllib.request

#create root window
root=tkinter.Tk()

#colors and fonts
root_color="#D6CDA4"
title_font=("times new roman",30,"bold")
lbl_font=("times new roman",14)
frame_color="#3D8361"

#configure root
root.title("Recipe Finder")
root.geometry("650x650")
root.resizable(0,0)
root.config(bg=root_color)
#other variables
meal_type=["","Breakfast","Lunch","Dinner","Snack","Teatime"]
cuisine_type=["american","asian","british","caribbean",
                      "central europe","chinese","eastern europe",
                      "french","greek","indian","italian","japanese",
                      "korean","kosher","mediterranean","mexican",
                      "middle eastern","nordic",
                      "south american","south east asian","world"]
diet_type=["Alcohol-Cocktail","Alcohol-Free","Celery-Free","Crustcean-Free","Dairy-Free","DASH","Egg-Free","Fish-Free","FODMAP-Free","Immuno-Supportive","Keto-Friendly","Kidney-Friendly","Kosher","Low Potassium","Low Sugar","Lupine-Free","Mediterranean",
           "Mollusk-Free","Mustard-Free","No oil added","Paleo","Peanut-Free","Pescatarian",
           "Pork-Free","Red-Meat-Free","Sesame-Free","Shellfish-Free","Soy-Free","Sugar-Conscious","Sulfite-Free","Tree-Nut-Free,Vegan","Vegetarian","Wheat-Free"]
#functions

def submit():
    #validate entry field for mandatory field check
    pass


#layout --> parent window

#title frame
title_frame=tkinter.Frame(root,bg=root_color)
title_frame.pack(pady=20)
title_lbl=tkinter.Label(title_frame,text="Recipe Finder",font=title_font,bg=root_color)
title_lbl.grid(row=0,column=0)

#add a logo image
img=Image.open('cooking.png')
img_tk=ImageTk.PhotoImage(img)
lbl_img=tkinter.Label(title_frame,image=img_tk,bg=root_color)
lbl_img.grid(row=0,column=1,padx=10)

#userinput frame
inp_frame=tkinter.Frame(root,bg=frame_color)
inp_frame.pack(fill=X,padx=20)
inp_frame.columnconfigure(0,weight=1)
inp_frame.columnconfigure(1,weight=1)
inp_frame.columnconfigure(2,weight=1)


lbl_ingr=tkinter.Label(inp_frame,text="Ingredients*",font=lbl_font,bg=frame_color,fg=root_color)
entry_ingr=tkinter.Entry(inp_frame,font=lbl_font,width=30)

lbl_mealtype=tkinter.Label(inp_frame,text="Meal Type",font=lbl_font,bg=frame_color,fg=root_color)
list_mealtype = tkinter.Listbox(inp_frame, width=10, height=5, selectmode ="multiple", font=lbl_font, relief=SUNKEN)
list_mealtype.insert(END, *meal_type)
scroll_mealtype=tkinter.Scrollbar(inp_frame)
list_mealtype.config(yscrollcommand=scroll_mealtype.set)
scroll_mealtype.config(command=list_mealtype.yview)

lbl_cuisinetype=tkinter.Label(inp_frame,text="Cuisine Type",font=lbl_font,bg=frame_color,fg=root_color)
list_cuisinetype = tkinter.Listbox(inp_frame, width=10, height=5, selectmode ="multiple", font=lbl_font, relief=SUNKEN)
list_cuisinetype.insert(END, *cuisine_type)
scroll_cuisinetype=tkinter.Scrollbar(inp_frame)
list_cuisinetype.config(yscrollcommand=scroll_cuisinetype.set)
scroll_cuisinetype.config(command=list_cuisinetype.yview)

lbl_dietryreq=tkinter.Label(inp_frame,text="Dietry Requirements",font=lbl_font,bg=frame_color,fg=root_color)
list_dietryrequirement = tkinter.Listbox(inp_frame, width=10, height=5, selectmode ="multiple", font=lbl_font, relief=SUNKEN)
list_dietryrequirement.insert(END, *diet_type)
scroll_diettype=tkinter.Scrollbar(inp_frame)
list_dietryrequirement.config(yscrollcommand=scroll_diettype.set)
scroll_diettype.config(command=list_dietryrequirement.yview)

btn_submit=tkinter.Button(inp_frame,text="Find Recipe",command="",font=lbl_font,bg=root_color)


lbl_ingr.grid(row=0,column=0,padx=5,pady=5,sticky="E")
entry_ingr.grid(row=0,column=1,padx=5,pady=5,sticky="W")

lbl_mealtype.grid(row=1,column=0,padx=10,pady=10,sticky="E")
list_mealtype.grid(row=1,column=1,padx=(10,0),pady=10,sticky="WE")
scroll_mealtype.grid(row=1,column=2,padx=(0,10),pady=10,sticky="NSW")

lbl_cuisinetype.grid(row=2,column=0,padx=10,pady=10,sticky='E')
list_cuisinetype.grid(row=2,column=1,pady=10,padx=(10,0),sticky='WE')
scroll_cuisinetype.grid(row=2,column=2,padx=(0,10),pady=10,sticky="NSW")

lbl_dietryreq.grid(row=3,column=0,padx=10,pady=10,sticky='E')
list_dietryrequirement.grid(row=3,column=1,pady=10,padx=(10,0),sticky='WE')
scroll_diettype.grid(row=3,column=2,padx=(0,10),pady=10,sticky="NSW")

btn_submit.grid(row=4,column=0,columnspan=3,padx=10,pady=10,ipadx=10)

#run main loop
root.mainloop()
