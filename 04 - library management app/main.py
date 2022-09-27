#import
import tkinter
from PIL import ImageTk,Image
from tkinter import StringVar,END,messagebox,filedialog
import csv

#root window
root=tkinter.Tk()

root.title("Library Management App")
root.geometry("750x700")

#variables
root_color="#C3F8FF"
title_font=("times new roman",30,"roman")
title_color="#F0EABE"
lbl_font=("times new roman",12,"bold")
btn_font=("times new roman",13)
btn_color="#21E1E1"

#configure root
root.config(bg=root_color)

#functions
def view_books():
    # read data from csv
    with open('books-data.csv','r',encoding='utf-8-sig') as f:
        dict_reader=csv.DictReader(f)
        for row in dict_reader:
            #print(row)
            listbox_book.insert(END,f"{row['title']}|{row['authors']}")

def search_books():
    listbox_book.delete(0,END)
    with open('books-data.csv','r',encoding='utf-8-sig') as f:
        book_title=entry_title.get().title()
        book_author=entry_author.get().title()
        book_isbn=entry_isbn.get().title()
        book_rating=entry_rating.get()
        dict_reader=csv.DictReader(f)
        for row in dict_reader:
            #print(row)
            if book_title in row['title'] and book_author in row['authors']and book_author in row['authors']and book_isbn in row['isbn']and row['average_rating'].startswith(book_rating):
                listbox_book.insert(END,f"{row['title']}|{row['authors']}")

def export_books():
    #save_name=filedialog.asksaveasfilename(initialdir="/",title="Save Note",filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")))
    #reference-https://stackoverflow.com/questions/68492630/how-can-i-save-a-csv-file-using-tk-filedialog-with-tkinter
    save_name=filedialog.asksaveasfilename(filetypes = [('All types(*.*)', '*.*'),("csv file(*.csv)","*.csv")], defaultextension = [('All tyes(*.*)', '*.*'),("csv file(*.csv)","*.csv")])

    with open(save_name,"w",newline='') as f:
        writer_csv=csv.writer(f)
        writer_csv.writerow(['BookId','Title','Author'])
    #write data back into a csv
        listbox_data=listbox_book.get(0,END)
        for element in listbox_data:
            element.rstrip("\n")
            # book_id=element.split('|')[0]
            book_title=element.split('|')[0]
            print(book_title)
            book_author=element.split('|')[1]

            with open(save_name,"a",newline='') as f:
                writer_csv=csv.writer(f)
                writer_csv.writerow([book_title,book_author])

def add_book():
    def add_bookdata():

        with open("books-data.csv","a",newline='') as f:
            writer_csv=csv.writer(f)
            writer_csv.writerow([entry_title.get(),entry_author.get(),entry_rating.get(),entry_isbn.get()])
            messagebox.showinfo(title="New Book added", message="Book Added successfully",)
    add_window=tkinter.Toplevel(root,bg=title_color)
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

    lbl_rating=tkinter.Label(add_window,text="Rating",bg=root_color,font=lbl_font)
    book_rating=StringVar()
    entry_rating=tkinter.Entry(add_window,width=10,text=book_rating)

    lbl_booktitle.grid(row=0,column=0,padx=20,pady=10)
    entry_title.grid(row=0,column=1,padx=(0,20),pady=10)
    lbl_author.grid(row=1,column=0,padx=20,pady=10)
    entry_author.grid(row=1,column=1,padx=(0,20),pady=10)
    lbl_isbn.grid(row=2,column=0,padx=20,pady=10)
    entry_isbn.grid(row=2,column=1,padx=(0,20),pady=10,sticky='W')
    lbl_rating.grid(row=3,column=0,padx=20,pady=10)
    entry_rating.grid(row=3,column=1,padx=(0,20),pady=10,sticky='W')
    btn_addnew=tkinter.Button(add_window,text="Add",command=add_bookdata)
    btn_addnew.grid(row=4,column=0,columnspan=2,padx=(0,20),pady=10)
    btn_exit=tkinter.Button(add_window,text="Exit",command=add_window.destroy)
    btn_exit.grid(row=4,column=1,columnspan=2,padx=(0,20),pady=10)


#layout
#frame 0 - Logo Image & Title
frame0=tkinter.LabelFrame(root,bg=root_color)
frame0.columnconfigure(0,weight=1)
#add title
lbl_title=tkinter.Label(frame0,text="Library Management App",font=title_font,bg=root_color)

#add image
#image attribution- <a href="https://www.flaticon.com/free-icons/education" title="education icons">Education icons created by Freepik - Flaticon</a>
img_1=Image.open("book-stack.png")
img_1.thumbnail((100,100))
img=ImageTk.PhotoImage(img_1)

canvas=tkinter.Canvas(frame0,width=100,height=100,bg=root_color,highlightthickness=0)
canvas.create_image((50,50),image=img)


frame0.pack(padx=10,pady=10)
lbl_title.grid(row=0,column=0,padx=20,pady=10)
canvas.grid(row=1,column=0,padx=20,pady=10)

#Frame 1 - Search Input Frame
frame1=tkinter.Frame(root,bg=root_color)
frame1.columnconfigure(0,weight=1)
frame1.columnconfigure(1,weight=1)
frame1.columnconfigure(2,weight=1)
frame1.columnconfigure(3,weight=1)

#search field -->book title
lbl_booktitle=tkinter.Label(frame1,text="Title",bg=root_color,font=lbl_font)
book_title=StringVar()
entry_title=tkinter.Entry(frame1,width=50,text=book_title)

#search field -->book author
lbl_author=tkinter.Label(frame1,text="Author",bg=root_color,font=lbl_font)
book_author=StringVar()
entry_author=tkinter.Entry(frame1,width=50,text=book_author)

#search field -->book isbn
lbl_isbn=tkinter.Label(frame1,text="ISBN",bg=root_color,font=lbl_font)
book_isbn=StringVar()
entry_isbn=tkinter.Entry(frame1,width=30,text=book_isbn)

#search field -->book rating
lbl_rating=tkinter.Label(frame1,text="Rating",bg=root_color,font=lbl_font)
book_rating=StringVar()
entry_rating=tkinter.Entry(frame1,width=10,text=book_rating)

#place frame1 and widgets
frame1.pack(padx=10,pady=10)
lbl_booktitle.grid(row=0,column=0,padx=5,pady=5)
entry_title.grid(row=0,column=1,padx=5,pady=5)
lbl_author.grid(row=0,column=2,padx=5,pady=5)
entry_author.grid(row=0,column=3,padx=5,pady=5)
lbl_isbn.grid(row=1,column=0,padx=5,pady=5)
entry_isbn.grid(row=1,column=1,padx=5,pady=5,sticky='W')
lbl_rating.grid(row=1,column=2,padx=5,pady=5)
entry_rating.grid(row=1,column=3,padx=5,pady=5,sticky='W')

#Frame 2 - Search Button Frame

frame2=tkinter.Frame(root,bg=root_color)

#view all button
btn_viewall=tkinter.Button(frame2,text="View All",font=btn_font,bg=btn_color,command=view_books)

#search button
btn_search=tkinter.Button(frame2,text="Search",font=btn_font,bg=btn_color,command=search_books)

#export data button
btn_export=tkinter.Button(frame2,text="Export",font=btn_font,bg=btn_color,command=export_books)

frame2.pack(padx=10,pady=10)
btn_viewall.grid(row=0,column=0,padx=5,pady=5,ipadx=15)
btn_search.grid(row=0,column=1,padx=5,pady=5,ipadx=20)
btn_export.grid(row=0,column=2,padx=5,pady=5,ipadx=20)


#Frame 3 - Output Frame
frame3=tkinter.Frame(root,bg=root_color)

#list box showing book id, title, author,isbn,rating
listbox_book=tkinter.Listbox(frame3,width=100,height=10)

#vertical scrollbar
vertical_scroll=tkinter.Scrollbar(frame3)
vertical_scroll.config(command=listbox_book.yview)
listbox_book.config(yscrollcommand=vertical_scroll.set)

#horizontal scrollbar
horizontal_scroll=tkinter.Scrollbar(frame3,orient='horizontal')
horizontal_scroll.config(command=listbox_book.xview)
listbox_book.config(xscrollcommand=horizontal_scroll.set)

#place frame3 and widgets
frame3.pack(padx=10,pady=10)
listbox_book.grid(row=0,column=0,padx=(10,0))
vertical_scroll.grid(row=0,column=1,padx=(0,10),sticky='NS')
horizontal_scroll.grid(row=1,column=0,columnspan=2,padx=10,sticky='EW')

#Frame 4 - Book Manage Frame
frame4=tkinter.Frame(root,bg=root_color)

# button for a top level window - add new book
btn_addbook=tkinter.Button(frame4,text="Add New Book", bg=btn_color,font=btn_font,command=add_book)
btn_exit=tkinter.Button(frame4,text="Exit", bg='pink',font=btn_font,command=root.destroy)

# button for a top level window-  update book

#place frame4 and widgets
frame4.pack(padx=10,pady=10)
btn_addbook.grid(row=0,column=0,padx=10,ipadx=5)
btn_exit.grid(row=0,column=2,padx=10,ipadx=20)

#main loop
root.mainloop()