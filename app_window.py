import tkinter as tk
from service.task_service import TaskService

class AppWindow(tk.Tk):

    def __init__(self, task_service: TaskService) -> None:
        super().__init__()
        self._task_service = task_service

        self.title("Tkinter desde POO")
        self.geometry("500x500")
        self.resizable(False, False)

        # Widgets
        self.create_widgets()

    def create_widgets(self) -> None:
        label = tk.Label(self, text="Bienvenido a mi App")
        label.pack()

        self.title_entry = tk.Entry(self)
        self.title_entry.pack()

        self.desc_entry = tk.Entry(self)
        self.desc_entry.pack()

        tk.Button(self, text="Agregar tarea", command=self.add_task).pack()

        from tkinter import ttk
        self.tree = ttk.Treeview(self, columns=("ID","Titulo","Descripcion"), show="headings")

        self.tree.heading("ID", text="ID")
        self.tree.heading("Titulo", text="Titulo")
        self.tree.heading("Descripcion", text="Descripcion")

        self.tree.pack()

        self.load_tasks()

    def load_tasks(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        tasks = self._task_service.get_all_task()

        for task in tasks:
            self.tree.insert("", "end", values=(task.uuid, task.title, task.description))

    def add_task(self):
        title = self.title_entry.get()
        desc = self.desc_entry.get()

        self._task_service.create_one_task(title, desc)

        self.load_tasks()
