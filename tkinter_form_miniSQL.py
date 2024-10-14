import tkinter as tk
import sqlite3
from tkinter import messagebox

def create_main_window():
    """Creates the main window of the library form application.
    Sets the title, size, and non-sliding of the window.
    Adds labels and text fields for title, author, year, genre, and publisher.
    """
    main_window = tk.Tk()
    main_window.title("Library Management Form")
    main_window.geometry("400x300")
    main_window.resizable(False, False)

    label_title = tk.Label(main_window, text="Title:", bg="lightblue")
    label_title.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="e")

    entry_title = tk.Entry(main_window, width=40)
    entry_title.grid(row=0, column=1, padx=10, pady=10)

    label_author = tk.Label(main_window, text="Author:", bg="lightblue")
    label_author.grid(row=1, column=0, padx=(10, 0), pady=10, sticky="e")

    entry_author = tk.Entry(main_window, width=40)
    entry_author.grid(row=1, column=1, padx=10, pady=10)

    label_year = tk.Label(main_window, text="Year:", bg="lightblue")
    label_year.grid(row=2, column=0, padx=(10, 0), pady=10, sticky="e")

    entry_year = tk.Entry(main_window, width=40)
    entry_year.grid(row=2, column=1, padx=10, pady=10)

    button_add = tk.Button(main_window, text="Add Book", command=lambda: add_book(entry_title, entry_author, entry_year))
    button_add.grid(row=3, columnspan=2, pady=20)

    main_window.mainloop()


def add_book(entry_title, entry_author, entry_year):
    """Adds a book to the database from the data entered in the form.
    Collects data from text fields and saves them to the database.
    Displays success or error messages depending on the result of the operation.
    """
    title = entry_title.get()
    author = entry_author.get()
    year = entry_year.get()

    if title and author and year:
        try:
            conn = sqlite3.connect('libray.db')
            cursor = conn.cursor()

            cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", f"Book '{title}' added successfully!")

            entry_title.delete(0, tk.END)
            entry_author.delete(0, tk.END)
            entry_year.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Error", f"Could not add book: {e}")
    else:
        messagebox.showwarning("Warning", "All fields are required!")


if __name__ == "__main__":
    create_main_window()
