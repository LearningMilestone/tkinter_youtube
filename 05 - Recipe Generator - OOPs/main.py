import tkinter
from PIL import Image,ImageTk
from tkinter import SUNKEN,END
import urllib.request

class RecipePage:
    def __init__(self):
        self.img_data="data:image/jpeg;base64,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"
        self.frame1_col='#F57328'
        self.title_font=("Courier New",38,"bold")
        self.lbl_font=("Courier New",12,"bold")
        self.lb_font=("Courier New",10)
        self.btn_font=("Courier New",12,"bold")
        self.recipewin=tkinter.Toplevel(bg="white")
        self.frame_recipe=tkinter.Frame(self.recipewin,bg="white")
        self.frame_recipe.pack(padx=20, pady=20)

        self.lbl_recipetitle=tkinter.Label(self.frame_recipe, text="Recipe Title", font=self.title_font, bg=self.frame1_col)
        self.lbl_recipetitle.grid(row=0, column=0)

        self.raw_data = urllib.request.urlopen(self.img_data).read()
        #img_rec=Image.open(BytesIO(raw_data))
        self.img=ImageTk.PhotoImage(data=self.raw_data)
        self.lbl_imgrec=tkinter.Label(self.frame_recipe, image=self.img)
        self.lbl_imgrec.grid(row=1,column=0,rowspan=2)
        self.lbl_imgrec.image=self.img

        self.lbl_cal=tkinter.Label(self.frame_recipe, text="Total Calories: 1234 cal", bg=self.frame1_col)
        self.lbl_cal.grid(row=1,column=1,sticky='W')

        self.lbl_prep=tkinter.Label(self.frame_recipe, text="Prep Time: 10 Minutes", bg=self.frame1_col)
        self.lbl_prep.grid(row=2,column=1,sticky='W')

        self.ingredients=["2 cups sugar","1 cup water","1 dash ground cloves","1 dash cinnamon","2 tablespoons peach schnapps","1 cup club soda","3 tablespoons spiced peach syrup"]
        n1="\n"
        self.lbl_ingr=tkinter.Label(self.frame_recipe, text=f"Ingredients \n \n { n1.join(str(x) for x in self.ingredients)}", bg=self.frame1_col)
        self.lbl_ingr.grid(row=3,column=0,columnspan=2,pady=20)

        self.btn_knowmore=tkinter.Button(self.frame_recipe, text='Know More About Recipe')
        self.btn_knowmore.grid(row=3,column=2)

        self.btn_nextrecipe=tkinter.Button(self.frame_recipe, text='Get Other Recipe')
        self.btn_nextrecipe.grid(row=4,column=0)


class RecipeFinder(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('Recipe Finder')
        self.geometry('700x600')
        #variable
        self.root_color='#FAC213'
        self.frame1_col='#F57328'
        self.title_font=("Courier New",38,"bold")
        self.lbl_font=("Courier New",12,"bold")
        self.lb_font=("Courier New",10)
        self.btn_font=("Courier New",12,"bold")

        self.base_url='https://api.edamam.com/api/recipes/v2'
        self.app_id='f14ea768'
        self.api_key='41b94c47dc89ddf565cdd201cc5504bc'
        self.meal_type=["","Breakfast","Lunch","Dinner","Snack","Teatime"]
        self.cuisine_type=["american","asian","british","caribbean",
                      "central europe","chinese","eastern europe",
                      "french","greek","indian","italian","japanese",
                      "korean","kosher","mediterranean","mexican",
                      "middle eastern","nordic",
                      "south american","south east asian","world"]

        #configure root
        self.config(bg=self.root_color)

        #layout
        #title frame
        self.frame_1=tkinter.Frame(self, bg=self.root_color)
        self.frame_1.pack(pady=10)

        self.title_lbl=tkinter.Label(self.frame_1, text="Recipe Finder", font=self.title_font, bg=self.root_color)
        self.title_lbl.grid(row=0, column=0, pady=20)

        #add a logo image
        #<a href="https://www.flaticon.com/free-icons/recipe" title="recipe icons">Recipe icons created by Freepik - Flaticon</a>
        self.img_1=Image.open('cooking.png')
        self.img_tk=ImageTk.PhotoImage(self.img_1)
        self.lbl_img=tkinter.Label(self.frame_1, image=self.img_tk, bg=self.root_color)
        self.lbl_img.grid(row=0,column=1,pady=5)

        #input frame
        self.frame_2=tkinter.Frame(self, bg=self.frame1_col)
        self.frame_2.pack(pady=10)
        self.frame_2.columnconfigure(0,weight=1)
        self.frame_2.columnconfigure(1,weight=1)

        #add user input parameter fields
        #Ingredient Entry Field
        ingr_lbl=tkinter.Label(self.frame_2, text="Ingredient*", bg=self.frame1_col, font=self.lbl_font)
        ingr_lbl.grid(row=0,column=0,pady=20,padx=10,sticky='W')

        self.ingr_ent=tkinter.Entry(self.frame_2, width=30, relief=SUNKEN, font=self.lb_font)
        self.ingr_ent.grid(row=0,column=1,pady=10,padx=10,sticky='W')

        #Meal Type Drop Down - Options -
        self.mealtype_lbl=tkinter.Label(self.frame_2, text="Meal Type", bg=self.frame1_col, font=self.lbl_font)
        self.mealtype_lbl.grid(row=1,column=0,pady=10,padx=10,sticky='W')

        self.list_mealtype = tkinter.Listbox(self.frame_2, width=30, height=5, selectmode ="multiple", font=self.lb_font, relief=SUNKEN)
        self.list_mealtype.grid(row=1,column=1,pady=10,padx=10,sticky='W')
        self.list_mealtype.insert(END, *self.meal_type)

        self.cuisinetype_lbl=tkinter.Label(self.frame_2, text="Cuisine Type", bg=self.frame1_col, font=self.lbl_font)
        self.cuisinetype_lbl.grid(row=2,column=0,pady=10,padx=10,sticky='W')
        self.list_cuisinetype = tkinter.Listbox(self.frame_2, width=30, height=5, selectmode ="multiple", font=self.lb_font, relief=SUNKEN)
        self.list_cuisinetype.grid(row=2,column=1,pady=10,padx=10,sticky='W')
        self.list_cuisinetype.insert(END, *self.cuisine_type)


        self.dietryrequirement_lbl=tkinter.Label(self.frame_2, text="Dietry Requirement", bg=self.frame1_col, font=self.lbl_font)
        self.dietryrequirement_lbl.grid(row=3,column=0,pady=10,padx=10,sticky='W')
        self.list_dietryrequirement = tkinter.Listbox(self.frame_2, width=30, height=5, selectmode ="multiple", font=self.lb_font, relief=SUNKEN)
        self.list_dietryrequirement.grid(row=3,column=1,pady=10,padx=10,sticky='W')
        self.list_dietryrequirement.insert(END, *self.cuisine_type)

        self.btn_search=tkinter.Button(self.frame_2, text="Search My Yummy Recipe", bg="#FFE9A0", font=self.btn_font, command=self.search)
        self.btn_search.grid(row=4,column=0,columnspan=2,pady=10,padx=10,ipadx=20)
        #output frame
        frame_3=tkinter.Frame(self, bg=self.root_color)

        frame_3.pack()

    def search(self):
        print('hello')
        #RecipePage()
        self.recipe_wind=RecipePage()
        #self.recipe_wind.recipewin.mainloop()



if __name__ == "__main__":
    root=RecipeFinder()
    root.mainloop()
