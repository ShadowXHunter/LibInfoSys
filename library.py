from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import sqlite3

conn = sqlite3.connect('lib.db')
cur = conn.cursor()

class Form:
    def __init__(self, root):
        def chkSrcIn(e):
            if self.srcIn.get()=="Books":
                self.value_list = ['Title','Author','Publisher','ISBN','Subject']

            elif self.srcIn.get()=="Journals":
                self.value_list = ['Title','Publisher','ISSN','Subject']
            elif self.srcIn.get()=="Magazines":
                self.value_list = ['Title','Publisher','ISSN','Genre']
            else:
                self.value_list = ['Title','Author','Publisher','ISBN/ISSN','Subject/Genre']
            self.srcBy.configure(values=self.value_list)

        self.root = root
        self.root.title("LibInfSys")
        self.root.resizable(width = False, height = False)

        MainFrame = Frame(self.root, bd=10,width=770,height=700, relief = RIDGE, bg = 'cadet blue')
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd = 5, width = 900, height = 100, relief = RIDGE)
        TitleFrame.grid(row = 0, column = 0 )

        QueryFrame = Frame(MainFrame, bd = 3, width = 700, height = 190, relief = RIDGE)
        QueryFrame.grid(row = 1, column = 0 )
        QueryFrame1 = Frame(QueryFrame, bd = 3, width = 700, height = 190, relief = RIDGE)
        QueryFrame1.pack(side = TOP)

        OutputFrame = Frame(MainFrame, bd = 3, width = 700, height = 500, relief = RIDGE)
        OutputFrame.grid(row = 2, column = 0 )
        OutputFrame1 = Frame(OutputFrame, bd = 3, width = 700, height = 500, relief = RIDGE)
        OutputFrame1.pack(side = TOP)

        query = StringVar()

        def SrcClick():
            if self.srcIn.get()=="Books":
                if self.srcBy.get()=="Title":
                    if query.get()=="":
                        tkinter.messagebox.showerror("Library Database", "Query Empty")
                    else:
                        sqlstr = 'SELECT Book.Title, Book.ISBN, Author.fname, Publisher.Name,Book.Edition, Book.Year_of_Publication, Book.pages, Book.Subject, Book.Copies, Book.issued, Book.reserved, Book.available FROM Book INNER JOIN Book_by_Author ON Book.id = Book_by_Author.bookID INNER JOIN Author ON Book_by_Author.authorID = Author.id INNER JOIN Book_By_Publisher on Book.id = Book_By_Publisher.bookID inner join Publisher on Book_By_Publisher.publisherID = Publisher.Id WHERE Book.Title = ?'
                        cur.execute(sqlstr, (query.get(),))
                        result = cur.fetchall()
                        if len(result) != 0:
                            self.Table.delete(*self.Table.get_children())
                            for row in result:
                                self.Table.insert('', END, values = row)
                            conn.commit()
                if self.srcBy.get()=="Author":
                    if query.get()=="":
                        tkinter.messagebox.showerror("Library Database", "Query Empty")
                    else:
                        sqlstr = 'SELECT Book.Title, Book.ISBN, Author.fname, Publisher.Name,Book.Edition, Book.Year_of_Publication, Book.pages, Book.Subject, Book.Copies, Book.issued, Book.reserved, Book.available FROM Book INNER JOIN Book_by_Author ON Book.id = Book_by_Author.bookID INNER JOIN Author ON Book_by_Author.authorID = Author.id INNER JOIN Book_By_Publisher on Book.id = Book_By_Publisher.bookID inner join Publisher on Book_By_Publisher.publisherID = Publisher.Id WHERE Author.fname = ?'
                        cur.execute(sqlstr, (query.get(),))
                        result = cur.fetchall()
                        if len(result) != 0:
                            self.Table.delete(*self.Table.get_children())
                            for row in result:
                                self.Table.insert('', END, values = row)
                            conn.commit()
                if self.srcBy.get()=="Subject":
                    if query.get()=="":
                        tkinter.messagebox.showerror("Library Database", "Query Empty")
                    else:
                        sqlstr = 'SELECT Book.Title, Book.ISBN, Author.fname, Publisher.Name,Book.Edition, Book.Year_of_Publication, Book.pages, Book.Subject, Book.Copies, Book.issued, Book.reserved, Book.available FROM Book INNER JOIN Book_by_Author ON Book.id = Book_by_Author.bookID INNER JOIN Author ON Book_by_Author.authorID = Author.id INNER JOIN Book_By_Publisher on Book.id = Book_By_Publisher.bookID inner join Publisher on Book_By_Publisher.publisherID = Publisher.Id WHERE Book.Subject=?'
                        cur.execute(sqlstr, (query.get(),))
                        result = cur.fetchall()
                        if len(result) != 0:
                            self.Table.delete(*self.Table.get_children())
                            for row in result:
                                self.Table.insert('', END, values = row)
                            conn.commit()
            '''
            if self.srcIn.get()=="Journals":
                if self.srcBy.get()=="Title":
                    if query.get()=="":
                        tkinter.messagebox.showerror("Library Database", "Query Empty")
                    else:
                        sqlstr = 'SELECT Journal.Title, Journal.issn, Author.fname, Publisher.Name,Journal.Volume, Book.Year_of_Publication, Book.pages, Book.Subject, Book.Copies, Book.issued, Book.reserved, Book.available FROM Book INNER JOIN Book_by_Author ON Book.id = Book_by_Author.bookID INNER JOIN Author ON Book_by_Author.authorID = Author.id INNER JOIN Book_By_Publisher on Book.id = Book_By_Publisher.bookID inner join Publisher on Book_By_Publisher.publisherID = Publisher.Id WHERE Book.Title = ?'
                        cur.execute(sqlstr, (query.get(),))
                        result = cur.fetchall()
                        if len(result) != 0:
                            self.Table.delete(*self.Table.get_children())
                            for row in result:
                                self.Table.insert('', END, values = row)
                            conn.commit()
            '''
        self.Label4 = Label(TitleFrame)
        self.Label4.pack(side = TOP)
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Times New Roman} -size 20 -weight bold")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Library Information System''')

        self.Label1 = Label(QueryFrame1)
        self.Label1.place(relx=0.212, rely=0.185, height=30, width=113)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 12")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Search in...''')

        self.Label2 = Label(QueryFrame1)
        self.Label2.place(relx=0.212, rely=0.368, height=30, width=113)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 12")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(justify='left')
        self.Label2.configure(text='''Search by...''')

        self.Label3 = Label(QueryFrame1)
        self.Label3.place(relx=0.212, rely=0.551, height=30, width=113)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(cursor="fleur")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 12")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(justify='left')
        self.Label3.configure(text='''Search''')

        self.srcIn = ttk.Combobox(QueryFrame1)
        self.srcIn.place(relx=0.382, rely=0.185, height=30, relwidth=0.239)
        self.value_list = ['All','Books','Journals','Magazines',]
        self.srcIn.configure(values=self.value_list)
        self.srcIn.configure(takefocus="")
        self.srcIn.configure(cursor="fleur")
        self.srcIn.bind("<<ComboboxSelected>>", chkSrcIn)

        self.srcBy = ttk.Combobox(QueryFrame1)
        self.srcBy.place(relx=0.382, rely=0.368, height=30, relwidth=0.238)
        self.srcBy.configure(textvariable=StringVar())
        self.srcBy.configure(takefocus="")
        self.srcBy.configure(cursor="fleur")

        self.searchQuery = Entry(QueryFrame1)
        self.searchQuery.place(relx=0.382, rely=0.551, height=30, relwidth=0.312)
        self.searchQuery.configure(textvariable=query)
        self.searchQuery.configure(background="white")
        self.searchQuery.configure(disabledforeground="#a3a3a3")
        self.searchQuery.configure(font="TkFixedFont")
        self.searchQuery.configure(foreground="#000000")
        self.searchQuery.configure(insertbackground="black")

        self.btnSearch = Button(QueryFrame1)
        self.btnSearch.place(relx=0.722, rely=0.551, height=30, width=47)
        self.btnSearch.configure(command=SrcClick)
        self.btnSearch.configure(activebackground="#ececec")
        self.btnSearch.configure(activeforeground="#000000")
        self.btnSearch.configure(background="#d9d9d9")
        self.btnSearch.configure(disabledforeground="#a3a3a3")
        self.btnSearch.configure(foreground="#000000")
        self.btnSearch.configure(highlightbackground="#d9d9d9")
        self.btnSearch.configure(highlightcolor="black")
        self.btnSearch.configure(pady="0")
        self.btnSearch.configure(text='''OK''')


        scroll_y = Scrollbar(OutputFrame1,orient = VERTICAL)
        scroll_y.pack(side=RIGHT, fill = Y)
        self.column=["title","isbn", "author", "publisher", "volume", "publishedOn", "pages", "subject", "copies", "issued", "reserved", "available"]
        self.Table = ttk.Treeview(OutputFrame1, height=12, columns = self.column,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill = Y)

        self.Table.heading("#1", text = "Title")
        self.Table.heading("#2", text = "ISBN/ISSN")
        self.Table.heading("#3", text = "Author")
        self.Table.heading("#4", text = "Publisher")
        self.Table.heading("#5", text = "Volume/Edition")
        self.Table.heading("#6", text = "Publication Date")
        self.Table.heading("#7", text = "Pages")
        self.Table.heading("#8", text = "Subject/Genre")
        self.Table.heading("#9", text = "Copies")
        self.Table.heading("#10", text = "Issued")
        self.Table.heading("#11", text = "Reserved")
        self.Table.heading("#12", text = "Available")
        self.Table['show']='headings'
        self.Table.column("#1", width = 150)
        self.Table.column("#2", width = 80)
        self.Table.column("#3", width = 120)
        self.Table.column("#4", width = 70)
        self.Table.column("#5", width = 90)
        self.Table.column("#6", width = 100)
        self.Table.column("#7", width = 50)
        self.Table.column("#8", width = 90)
        self.Table.column("#9", width = 50)
        self.Table.column("#10", width = 50)
        self.Table.column("#11", width = 60)
        self.Table.column("#12", width = 60)
        self.Table.pack(fill=BOTH, expand = 1)

if __name__=='__main__':
    root = Tk()
    application = Form(root)
    root.mainloop()
