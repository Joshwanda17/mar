import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.root = tk.Tk()
        self.root.title("To-Do List")

        #Task List
        self.task_list=tk.Listbox(self.root, width=40, height=10)
        self.task_list.pack(padx=10, pady=10)

        #Task entry
        self.task_entry = tk.Entry(self.root,width=40)
        self.task_entry.pack(padx=10, pady=10)

        #Buttons
        self.add_button=tk.Button(self.root,text="Add Task", command=self.add_task)
        self.add_button.pack(padx=10, pady=5)

        self.delete_button=tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(padx=10, pady=10)

        self.quit_button=tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack(padx=10, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            self.tasks.pop(task_index)
        except IndexError:
            messagebox.showwarning("Error", "Select a task to delete")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()
