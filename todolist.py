import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)

app = tk.Tk()
app.title("To-Do List")

frame = tk.Frame(app)
frame.pack(pady=10)

listbox = tk.Listbox(frame, selectmode=tk.SINGLE)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(app, width=40)
entry.pack(pady=10)

add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack()
remove_button = tk.Button(app, text="Remove Task", command=remove_task)
remove_button.pack()

app.mainloop()
