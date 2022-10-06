#data source -https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks
#image attribution- <a href="https://www.flaticon.com/free-icons/education" title="education icons">Education icons created by Freepik - Flaticon</a>
#other - #reference-https://stackoverflow.com/questions/68492630/how-can-i-save-a-csv-file-using-tk-filedialog-with-tkinter
import csv
import tkinter
from PIL import Image,ImageTk
from tkinter import StringVar,ttk,END,filedialog,messagebox

#create root window
root=tkinter.Tk()
root.title('Library Management')
root.geometry("750x600")

#create variables
root_color="#38E54D"
title_font=("Times New Roman",32,"bold")
lbl_font=("Times New Roman",14)
frame_col="#2192FF"

ratings=["1+","2+","3+","4+"]

#configure root
root.configure(bg=root_color)

#create functions
def add_image(master,path):
    img_1=Image.open(path)
    img_1=ImageTk.PhotoImage(img_1)
    img_lbl=tkinter.Label(master,image=img_1,bg=root_color)
    img_lbl.image=img_1
    return img_lbl

def search():
    #first clear listbox
    book_list.delete(0,END)
    #fetch value from input fields
    #if all the fields are empty show all books
    #else show the books meeting criteria in the input fields
    bktitle=ent_bktitle.get()
    bkauthor=ent_bkauthor.get()
    bkisbn=ent_bkISBN.get()
    bkrating=rating_option.get()

    with open('books-data.csv', 'r',encoding='utf-8-sig') as f:
        dict_reader = csv.DictReader(f)
        if len(bktitle)==0 and len(bkauthor)==0 and len(bkisbn)==0 and bkrating=="1+":
            #read data from csv and update in listbox
            for row in dict_reader:
                book_list.insert(END,row)
                #book_list.insert(END,f"{row['title']}|{row['authors']}")
        else:
            for row in dict_reader:
                if bktitle.title() in row['title'] and bkauthor.title() in row['authors'] and bkisbn.title() in row['isbn'] and float(row['average_rating'])> int(bkrating.title()[0]):
                   book_list.insert(END,row)

def export():
    #open filedialogue and save file in csv format
    save_name=filedialog.asksaveasfilename(initialdir='/',
                                           title="Save File",
                                           filetypes= [("csv file(*.csv)","*.csv"),('All Files', '*.*')], defaultextension = [('All tyes(*.*)', '*.*'),("csv file(*.csv)","*.csv")])

    with open(save_name, "w", newline='',encoding='utf-8-sig') as f:
        writer_csv = csv.writer(f)
        writer_csv.writerow(['Title', 'Author',"ISBN","Rating"])
        listbox_data = book_list.get(0, END)
        for data in listbox_data:
            data=eval(data)
            writer_csv.writerow([data['title'],data['authors'],data['average_rating'],data['isbn']])

def add_new():
    #open a top level window which lets you add title,author,isbn,rating
    #add data to csv file
    def add_bookdata():
        if len(entry_title.get())!=0 and len(entry_author.get())!=0 and len(entry_rating.get())!=0 and len(entry_isbn.get()) !=0:
            with open("books-data.csv","a",newline='') as f:
                writer_csv=csv.writer(f)
                writer_csv.writerow([entry_title.get(),entry_author.get(),entry_rating.get(),entry_isbn.get()])
                messagebox.showinfo(title="New Book added", message="Book Added successfully",)
        else:
            messagebox.showerror("empty field","all fields must be filled")
    add_window=tkinter.Toplevel(root,bg=root_color)
    add_window.title("Add a New Book")
    add_window.geometry("420x250")
    add_window.resizable(0,0)
    lbl_booktitle=tkinter.Label(add_window,text="Title",bg=root_color,font=lbl_font)
    book_title=StringVar()
    entry_title=tkinter.Entry(add_window,width=50,text=book_title)
    lbl_author=tkinter.Label(add_window,text="Author",bg=root_color,font=lbl_font)
    book_author=StringVar()
    entry_author=tkinter.Entry(add_window,width=50,text=book_author)
    lbl_isbn=tkinter.Label(add_window,text="ISBN",bg=root_color,font=lbl_font)
    book_isbn=StringVar()
    entry_isbn=tkinter.Entry(add_window,width=30,text=book_isbn)
    lbl_rating = tkinter.Label(add_window, text="Rating", bg=root_color, font=lbl_font)
    book_rating = StringVar()
    entry_rating = tkinter.Entry(add_window, width=10, text=book_rating)

    lbl_booktitle.grid(row=0, column=0, padx=20, pady=10)
    entry_title.grid(row=0, column=1, padx=(0, 20), pady=10)
    lbl_author.grid(row=1, column=0, padx=20, pady=10)
    entry_author.grid(row=1, column=1, padx=(0, 20), pady=10)
    lbl_isbn.grid(row=2, column=0, padx=20, pady=10)
    entry_isbn.grid(row=2, column=1, padx=(0, 20), pady=10, sticky='W')
    lbl_rating.grid(row=3, column=0, padx=20, pady=10)
    entry_rating.grid(row=3, column=1, padx=(0, 20), pady=10, sticky='W')
    btn_addnew = tkinter.Button(add_window, text="Add", command=add_bookdata)
    btn_addnew.grid(row=4, column=0, columnspan=2, padx=(0, 20), pady=10)
    btn_exit = tkinter.Button(add_window, text="Exit", command=add_window.destroy)
    btn_exit.grid(row=4, column=1, columnspan=2, padx=(0, 20), pady=10)


#create layout

#title frame
title_frame=tkinter.Frame(root,bg =root_color)
title_frame.pack(pady=20)
title_text=tkinter.Label(title_frame,bg =root_color,text="Library Management",font=title_font)
title_text.grid(row=0,column=0)

#add image
img_lbl=add_image(title_frame,"book-stack.png")
img_lbl.grid(row=0,column=1)

#input frame
input_frame=tkinter.Frame(root,bg=frame_col)
input_frame.pack(pady=20,padx=20)

# Add input fields
lbl_bktitle=tkinter.Label(input_frame,text="Title  \n (full /partial)",font=lbl_font,bg=frame_col)
ent_bktitle=tkinter.Entry(input_frame,width=30)
lbl_bktitle.grid(row=0,column=0,padx=5,pady=5)
ent_bktitle.grid(row=0,column=1,padx=10,pady=5)

lbl_bkauthor=tkinter.Label(input_frame,text="Author Name \n (full/partial) ",font=lbl_font,bg=frame_col)
ent_bkauthor=tkinter.Entry(input_frame,width=30)
lbl_bkauthor.grid(row=0,column=2,padx=5,pady=5)
ent_bkauthor.grid(row=0,column=3,padx=10,pady=5)

lbl_bkISBN=tkinter.Label(input_frame,text="ISBN",font=lbl_font,bg=frame_col)
ent_bkISBN=tkinter.Entry(input_frame,width=30)
lbl_bkISBN.grid(row=1,column=0,padx=5,pady=5,)
ent_bkISBN.grid(row=1,column=1,padx=10,pady=5,)


lbl_rating=tkinter.Label(input_frame,text="Rating",font=lbl_font,bg=frame_col)
lbl_rating.grid(row=1,column=2,padx=5,pady=5,)

rating_option=StringVar()
rating_list=ttk.OptionMenu(input_frame,rating_option,*ratings)
rating_list.grid(row=1,column=3,padx=10,pady=5,sticky='W')
rating_option.set("1+")
rating_list.config(width=8)

btn_search=tkinter.Button(input_frame,text="Search Books",command=search,font=lbl_font)
btn_search.grid(row=3,column=0,columnspan=4,pady=10,ipadx=10)

#output_frame
output_frame=tkinter.Frame(root,bg=root_color)
output_frame.pack(pady=20,padx=20)
book_list=tkinter.Listbox(output_frame,width=100,height=10)
book_list.grid(row=0,column=0,columnspan=3)
scroll_books_y=tkinter.Scrollbar(output_frame)
scroll_books_y.grid(row=0,column=3,stick="NS")

# book_list.config(yscrollcommand=scroll_books_y.set)
scroll_books_y.config(command=book_list.yview)

scroll_books_x=tkinter.Scrollbar(output_frame,orient='horizontal')
scroll_books_x.grid(row=1,column=0,columnspan=4,sticky="EW")

book_list.config(yscrollcommand=scroll_books_y.set,xscrollcommand=scroll_books_x.set)
scroll_books_x.config(command=book_list.xview)

btn_export=tkinter.Button(output_frame,text="Export",command=export,font=lbl_font)
btn_export.grid(row=2,column=0,padx=10,pady=10,ipadx=20,sticky='EW')

btn_addnew=tkinter.Button(output_frame,text="Add New",command=add_new,font=lbl_font)
btn_addnew.grid(row=2,column=1,pady=10,ipadx=10,padx=10,sticky='EW')

btn_exit=tkinter.Button(output_frame,text="Exit",command=root.destroy,font=lbl_font,bg='red')
btn_exit.grid(row=2,column=2,pady=10,ipadx=10,padx=10,sticky='EW')

#run mainloop
root.mainloop()