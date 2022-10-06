import random
import tkinter
from io import BytesIO

from PIL import Image,ImageTk
from tkinter import SUNKEN,END,X,messagebox,DISABLED
from urllib.request import urlopen
import webbrowser
import requests


#create root window
root=tkinter.Tk()

#colors and fonts
root_color="#D6CDA4"
title_font=("times new roman",30,"bold")
lbl_font=("times new roman",14)
frame_color="#3D8361"
app_id="f14ea768"
app_key="41b94c47dc89ddf565cdd201cc5504bc"
url="https://api.edamam.com/api/recipes/v2/"

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
    #verify if toplevel is already open and close the toplevel
    for child in root.winfo_children():
        if child.winfo_class() == "Toplevel":
            child.destroy()

    ingredient = entry_ingr.get()
    if len(ingredient) ==0:
        #add a error dialogue box here
        #print("please enter the ingredient")
        messagebox.showerror("Missing Ingredient","Please enter ingredient")

    else:
        #open toplevel window here //call a function

        send_request(ingredient.title())

def send_request(ingredient_name):
    global recipe_name
    global ingredients
    global calories
    global prep_time
    global recipe_img
    global recipesource


    #create request-https://api.edamam.com/api/recipes/v2?type=public&q=avocado&app_id=f14ea768&app_key=41b94c47dc89ddf565cdd201cc5504bc
    #type = public & q = avocado & app_id = f14ea768 & app_key = 41
    # b94c47dc89ddf565cdd201cc5504bc
    queryString={"type":"public","q":ingredient_name,
                 "app_id":app_id,"app_key":app_key,"imageSize":"LARGE"}
    response=requests.request("GET",url=url,params=queryString)
    response=response.json()['hits'][random.randint(0,19)]['recipe']
    print(round(response['calories'],2),response['totalTime'])

    #send api request and fetch data from the response
    ingredient=ingredient_name
    recipe_name=response['label']
    calories = round(response['calories'],2)
    prep_time = response['totalTime']
    ingredients=response['ingredientLines']
    recipesource=response['url']
    recipe_img=response['images']['SMALL']['url']
    recipewin(ingredient)


def recipewin(ingredient_name):

    recipe_win=tkinter.Toplevel(root,bg=root_color)
    recipe_win.geometry("500x620")
    recipe_win.resizable(0,0)
    recipe_win.title("Amazing Recipe")


    #add widgets on toplevel window
    #Recipe Title
    title_frame=tkinter.Frame(recipe_win,bg=root_color)
    title_frame.pack()

    lbl_recipe=tkinter.Label(title_frame,bg=root_color,text=recipe_name,font=title_font)
    lbl_recipe.grid(row=0,column=0,pady=20)

    output_frame=tkinter.Frame(recipe_win,bg=frame_color)
    output_frame.pack()
    # output_frame.columnconfigure(0,weight=1)
    # output_frame.columnconfigure(1, weight=1)

    #link help - https://web.archive.org/web/20201111190625id_/http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
    # img=Image.open('bibimbap.png')
    #function can be created to read image from url
    raw_data = urlopen(recipe_img).read()
    img = Image.open(BytesIO(raw_data))
    img_recipe=ImageTk.PhotoImage(img)
    lbl_imgrec=tkinter.Label(output_frame,image=img_recipe,bg=frame_color)
    lbl_imgrec.image=img_recipe
    lbl_imgrec.grid(row=0,column=0,columnspan=2,ipadx=20,pady=10)

    #Prep time and calories Label

    lbl_cal=tkinter.Label(output_frame,text=f"Total Calories: {calories} Cal  ***  Prep Time: {prep_time} Minutes",font=lbl_font,bg=frame_color,fg=root_color)
    #lbl_preptime=tkinter.Label(output_frame,text=f"Prep Time: {prep_time} Minutes",font=lbl_font,bg=root_color,fg=frame_color)
    lbl_cal.grid(row=1,column=0,columnspan=2,padx=10,pady=10,ipadx=10)
    #lbl_preptime.grid(row=1,column=1,sticky='WN',padx=10)
    txt_ingr=tkinter.Text(output_frame,height=5,width=50,font=lbl_font,bg=root_color,fg=frame_color)
    txt_ingr.grid(row=2,column=0,sticky='EW',padx=(10,0),pady=10)
    txt_ingr.insert(1.0,"Ingredients:\n\n")

    for item in ingredients:
        txt_ingr.insert(END,item+'\n')
    txt_ingr.config(state=DISABLED)

    scroll_ingr=tkinter.Scrollbar(output_frame)
    scroll_ingr.grid(row=2,column=1,pady=10,padx=(0,10),sticky='WNS')
    txt_ingr.config(yscrollcommand=scroll_ingr.set)
    scroll_ingr.config(command=txt_ingr.yview)

    btn_frame=tkinter.Frame(recipe_win,bg=root_color)
    btn_frame.pack(pady=20)

    btn_recipedetail = tkinter.Button(btn_frame, text="Go To Recipe", command=lambda: webbrowser.open(recipesource), font=lbl_font, bg="#FF6337")
    btn_anotherrecipe = tkinter.Button(btn_frame, text=f"Another {ingredient_name} Dish", command=submit, font=lbl_font, bg=frame_color,fg=root_color)
    btn_quittop = tkinter.Button(btn_frame, text="Quit", command=recipe_win.destroy, font=lbl_font,bg="#C64756")

    btn_recipedetail.grid(row=0,column=0,padx=5)
    btn_anotherrecipe.grid(row=0, column=1,padx=5)
    btn_quittop.grid(row=0, column=2, padx=10)
    return recipe_win


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


lbl_ingr=tkinter.Label(inp_frame,text="Ingredient*",font=lbl_font,bg=frame_color,fg=root_color)
entry_ingr=tkinter.Entry(inp_frame,font=lbl_font,width=30)
entry_ingr.focus()

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

btn_submit=tkinter.Button(inp_frame,text="Find Recipe",command=submit,font=lbl_font,bg=root_color)
btn_quit=tkinter.Button(inp_frame,text="Quit",command=root.destroy,font=lbl_font,bg="#C64756")


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

btn_submit.grid(row=4,column=0,columnspan=2,padx=(10,0),pady=10,sticky='EW')
btn_quit.grid(row=4,column=2,padx=10,pady=10,ipadx=10)

#run main loop
root.mainloop()
