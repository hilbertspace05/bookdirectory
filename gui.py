# gui.py
import tkinter as tk
from tkinter import ttk
from db_operations import Database

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Directory")

        # Database connection parameters
        self.db_params = {
            "dbname": "books_directory",
            "user": "postgres",
            "password": "",
            "host": "localhost",
            "port": "5432",
        }

        # Initialize database connection
        self.db = Database(**self.db_params)

        # Create and configure widgets
        self.create_widgets()

    def create_widgets(self):
        # Create Treeview widget to display book information
        self.tree = ttk.Treeview(self.root, columns=("ID", "Title", "Author", "Published Year"))
        self.tree.heading("#1", text="ID")
        self.tree.heading("#2", text="Title")
        self.tree.heading("#3", text="Author")
        self.tree.heading("#4", text="Published Year")
        self.tree.pack()

        # Create entry fields for user input
        self.horizontal_box1 = tk.Frame(self.root)
        self.title_label = tk.Label(self.horizontal_box1, text="Title: ")
        self.title_entry = tk.Entry(self.horizontal_box1)
        self.horizontal_box2 = tk.Frame(self.root)
        self.author_label = tk.Label(self.horizontal_box2, text="Author: ")
        self.author_entry = tk.Entry(self.horizontal_box2)
        self.horizontal_box3 = tk.Frame(self.root)
        self.year_label = tk.Label(self.horizontal_box3, text="Year: ")
        self.year_entry = tk.Entry(self.horizontal_box3)

        # Create buttons for database operations
        self.create_button = tk.Button(self.root, text="Create Book", command=self.create_book)
        self.update_button = tk.Button(self.root, text="Update Book", command=self.update_book)

        # Place widgets using grid or pack method
        self.horizontal_box1.pack()
        self.horizontal_box2.pack()
        self.horizontal_box3.pack()
        self.title_label.pack(side=tk.LEFT)
        self.title_entry.pack(side=tk.LEFT)
        self.author_label.pack(side=tk.LEFT)
        self.author_entry.pack(side=tk.LEFT)
        self.year_label.pack(side=tk.LEFT)
        self.year_entry.pack(side=tk.LEFT)
        self.create_button.pack()
        self.update_button.pack()
        self.load_books()

    def create_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()
        data = (title, author, year)
        self.db.create_book(data)
        self.clear_entry_fields()
        self.load_books()

    def update_book(self):
        selected_item = self.tree.selection()
        if selected_item:
            id = self.tree.item(selected_item)["values"][0]
            title = self.title_entry.get()
            author = self.author_entry.get()
            year = self.year_entry.get()
            data = (title, author, year, id)
            self.db.update_book(data)
            self.clear_entry_fields()
            self.load_books()

    def load_books(self):
        self.tree.delete(*self.tree.get_children())
        books = self.db.get_all_books()
        for book in books:
            self.tree.insert("", "end", values=book)

    def clear_entry_fields(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
