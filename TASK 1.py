
import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

# Create a frame for the listbox and scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

# Create a listbox to display tasks
listbox = tk.Listbox(
    frame,
    width=50,
    height=10,
    bd=0,
    selectbackground="#a6a6a6"
)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Create a scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

# Configure the listbox and scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Create an entry box to add new tasks
entry = tk.Entry(
    root,
    font=("Helvetica", 24)
)
entry.pack(pady=20)

# Create a button to add tasks
add_button = tk.Button(
    root,
    text="Add Task",
    font=("Helvetica", 14),
    command=lambda: add_task()
)
add_button.pack(pady=10)

# Create a button to delete tasks
delete_button = tk.Button(
    root,
    text="Delete Task",
    font=("Helvetica", 14),
    command=lambda: delete_task()
)
delete_button.pack(pady=10)

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Run the main loop
root.mainloop()
