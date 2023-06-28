#################################################
# Author: Nathan Tamari
# Purpose:
#################################################

import tkinter as tk
from tkinter import ttk
from Filter import Filter
from Task import Task

class TaskUI:
    def __init__(self):
        self.text = None
        self.descText = None
        self.taskArray = []  # Creates an array, later to be filled with tasks
        ##################################################
        # setup of TKinter
        self.color = "#%02x%02x%02x" % (157, 209, 241)  # creates light blue background
        self.root = tk.Tk()
        self.root.geometry('1920x1080')
        self.root.title('taskManager')
        self.mainframe = tk.Frame(self.root)
        self.mainframe.pack(fill='both', expand=True)
        #################################################

        # random tasks, delete
        self.taskArray.append(Task("Hello", "hey,"))
        self.taskArray.append(Task("Goodbye", "bye"))
        self.taskArray.append(Task("Bot Man", "man bot"))
        self.taskArray.append(Task("Bot ZZ", "zz bot"))
        self.taskArray.append(Task("Aaa this the first one", "it better be"))

        # Fills home page with current tasks
        self.printlist()
        self.root.mainloop()
        return

    def sortbycommand(self):
        filter = Filter()
        self.taskArray = filter.sortAlpha(self.taskArray)
        self.removealltext()
        self.printlist()
        return

    def printlist(self):
        self.text = ttk.Label(self.mainframe, text="Task List:", font=("Brass Mono", 30), foreground=self.color)
        self.text.grid(row=0, column=0, padx=100, pady=30)

        sort_by_button = ttk.Button(self.mainframe, text='Sort By')
        sort_by_button.grid(row=0, column=1, pady=5, padx=(300, 0))
        sort_by_button.config(command=self.sortbycommand)

        search_button = ttk.Button(self.mainframe, text='Search')
        search_button.grid(row=0, column=2, pady=5)
        counter = 0

        for task in self.taskArray:
            self.text = ttk.Label(self.mainframe, text=task.getname(), foreground=self.color, font=("Brass Mono", 20))
            self.text.grid(row=2 + counter * 2, column=0, pady=15, padx=30)
            self.descText = ttk.Label(self.mainframe, text=task.getdesc(), foreground=self.color,
                                      font=("Brass Mono", 15))
            self.descText.grid(row=2 + (counter * 2) + 1, column=0, pady=(0, 30))
            counter += 1

    def removealltext(self):
        for widget in self.mainframe.winfo_children():
            widget.destroy()


if __name__ == '__main__':
    TaskUI()
