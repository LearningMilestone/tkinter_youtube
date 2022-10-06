import csv
import tkinter
from PIL import Image,ImageTk
from tkinter import StringVar,ttk,END,filedialog,messagebox


root_color="#38E54D"
title_font=("Times New Roman",32,"bold")
lbl_font=("Times New Roman",14)
frame_col="#2192FF"

class AddBook(tkinter.Toplevel):

    def __init__(self,parent):
        super().__init__()
        self.title("Add New Book")
        self.geometry("420x250")
        self.resizable(0, 0)
        self.config(bg=root_color)
        self.lbl_booktitle = tkinter.Label(self, text="Title", bg=root_color, font=lbl_font)
        self.book_title = StringVar()
        self.entry_title = tkinter.Entry(self, width=50, text=self.book_title)
        self.lbl_author = tkinter.Label(self, text="Author", bg=root_color, font=lbl_font)
        self.book_author = StringVar()
        self.entry_author = tkinter.Entry(self, width=50, text=self.book_author)
        self.lbl_isbn = tkinter.Label(self, text="ISBN", bg=root_color, font=lbl_font)
        self.book_isbn = StringVar()
        self.entry_isbn = tkinter.Entry(self, width=30, text=self.book_isbn)
        self.lbl_rating = tkinter.Label(self, text="Rating", bg=root_color, font=lbl_font)
        self.book_rating = StringVar()
        self.entry_rating = tkinter.Entry(self, width=10, text=self.book_rating)

        self.lbl_booktitle.grid(row=0, column=0, padx=20, pady=10)
        self.entry_title.grid(row=0, column=1, padx=(0, 20), pady=10)
        self.lbl_author.grid(row=1, column=0, padx=20, pady=10)
        self.entry_author.grid(row=1, column=1, padx=(0, 20), pady=10)
        self.lbl_isbn.grid(row=2, column=0, padx=20, pady=10)
        self.entry_isbn.grid(row=2, column=1, padx=(0, 20), pady=10, sticky='W')
        self.lbl_rating.grid(row=3, column=0, padx=20, pady=10)
        self.entry_rating.grid(row=3, column=1, padx=(0, 20), pady=10, sticky='W')
        self.btn_addnew = tkinter.Button(self, text="Add", command=self.add_bookdata)
        self.btn_addnew.grid(row=4, column=0, columnspan=2, padx=(0, 20), pady=10)
        self.btn_exit = tkinter.Button(self, text="Exit", command=self.destroy)
        self.btn_exit.grid(row=4, column=1, columnspan=2, padx=(0, 20), pady=10)

    # add data to csv file
    def add_bookdata(self):
        if len(self.entry_title.get()) != 0 and len(self.entry_author.get()) != 0 and len(self.entry_rating.get()) != 0 and len(
                self.entry_isbn.get()) != 0:
            with open("books-data.csv", "a", newline='') as f:
                writer_csv = csv.writer(f)
                writer_csv.writerow([self.entry_title.get(), self.entry_author.get(), self.entry_rating.get(), self.entry_isbn.get()])
                messagebox.showinfo(title="New Book added", message="Book Added successfully", )
        else:
            messagebox.showerror("empty field", "all fields must be filled")


class App(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.title("My First OOPs app")
        self.geometry("750x600")
        self.config(bg=root_color)

        #variables
        self.ratings = ["1 or above", "2 or above", "3 or above", "4 or above"]

        #create layout
        self.title_frame = tkinter.Frame(self, bg=root_color)
        self.title_frame.pack(pady=20)
        self.title_text = tkinter.Label(self.title_frame, bg=root_color, text="Library Management", font=title_font)
        self.title_text.grid(row=0, column=0)

        # add image
        self.img_lbl = self.add_image(self.title_frame, "book-stack.png")
        self.img_lbl.grid(row=0, column=1)

        # input frame
        self.input_frame = tkinter.Frame(self, bg=frame_col)
        self.input_frame.pack(pady=20, padx=20)

        # Add input fields
        self.lbl_bktitle = tkinter.Label(self.input_frame, text="Title  \n (full /partial)", font=lbl_font, bg=frame_col)
        self.ent_bktitle = tkinter.Entry(self.input_frame, width=30)
        self.lbl_bktitle.grid(row=0, column=0, padx=5, pady=5)
        self.ent_bktitle.grid(row=0, column=1, padx=10, pady=5)

        self.lbl_bkauthor = tkinter.Label(self.input_frame, text="Author Name \n (full/partial) ", font=lbl_font, bg=frame_col)
        self.ent_bkauthor = tkinter.Entry(self.input_frame, width=30)
        self.lbl_bkauthor.grid(row=0, column=2, padx=5, pady=5)
        self.ent_bkauthor.grid(row=0, column=3, padx=10, pady=5)

        self.lbl_bkISBN = tkinter.Label(self.input_frame, text="ISBN", font=lbl_font, bg=frame_col)
        self.ent_bkISBN = tkinter.Entry(self.input_frame, width=30)
        self.lbl_bkISBN.grid(row=1, column=0, padx=5, pady=5, )
        self.ent_bkISBN.grid(row=1, column=1, padx=10, pady=5, )

        self.lbl_rating = tkinter.Label(self.input_frame, text="Rating", font=lbl_font, bg=frame_col)
        self.lbl_rating.grid(row=1, column=2, padx=5, pady=5, )

        self.rating_option = StringVar()
        self.rating_list = ttk.OptionMenu(self.input_frame, self.rating_option, *self.ratings)
        self.rating_list.grid(row=1, column=3, padx=10, pady=5, sticky='W')
        self.rating_option.set("Select Rating")
        self.rating_list.config(width=15)

        self.btn_search = tkinter.Button(self.input_frame, text="Search Books", command=self.search, font=lbl_font)
        self.btn_search.grid(row=3, column=0, columnspan=4, pady=10, ipadx=10)

        # output_frame
        self.output_frame = tkinter.Frame(self, bg=root_color)
        self.output_frame.pack(pady=20, padx=20)
        self.book_list = tkinter.Listbox(self.output_frame, width=100, height=10)
        self.book_list.grid(row=0, column=0, columnspan=3)
        self.scroll_books_y = tkinter.Scrollbar(self.output_frame)
        self.scroll_books_y.grid(row=0, column=3, stick="NS")

        # book_list.config(yscrollcommand=scroll_books_y.set)
        self.scroll_books_y.config(command=self.book_list.yview)

        self.scroll_books_x = tkinter.Scrollbar(self.output_frame, orient='horizontal')
        self.scroll_books_x.grid(row=1, column=0, columnspan=4, sticky="EW")

        self.book_list.config(yscrollcommand=self.scroll_books_y.set, xscrollcommand=self.scroll_books_x.set)
        self.scroll_books_x.config(command=self.book_list.xview)

        self.btn_export = tkinter.Button(self.output_frame, text="Export", command=self.export, font=lbl_font)
        self.btn_export.grid(row=2, column=0, padx=10, pady=10, ipadx=20, sticky='EW')

        self.btn_addnew = tkinter.Button(self.output_frame, text="Add New", command=self.add_new, font=lbl_font)
        self.btn_addnew.grid(row=2, column=1, pady=10, ipadx=10, padx=10, sticky='EW')

        self.btn_exit = tkinter.Button(self.output_frame, text="Exit", command=self.destroy, font=lbl_font, bg='red')
        self.btn_exit.grid(row=2, column=2, pady=10, ipadx=10, padx=10, sticky='EW')

    def add_image(self,master, path):
        img_1 = Image.open(path)
        img_1 = ImageTk.PhotoImage(img_1)
        img_lbl = tkinter.Label(master, image=img_1, bg=root_color)
        img_lbl.image = img_1
        return img_lbl

    def search(self):
        print("search")

    def export(self):
        print("search")

    def add_new(self):
        AddBook(self)

if __name__=="__main__":
    root=App()
    root.mainloop()