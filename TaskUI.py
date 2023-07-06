#################################################
# Author: Nathan Tamari
# Purpose:
#################################################

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import OptionMenu
from Filter import Filter
from TaskWindow import TaskWindow


class TaskUI:
    def __init__(self):
        self.desc_field = None
        self.name_field = None
        self.blank = None
        self.clicked = None
        self.drop_menu = None
        self.sort_button = None
        self.text = None
        self.descText = None
        self.taskArray = []  # Creates an array, later to be filled with tasks

        # Set colors for readability
        self.background_color = "#95F9E3"  # Light gray
        self.text_color = "#53131E"  #
        self.button_bg_color = "#009FB7"  # Blue
        self.button_fg_color = "#FFFFFF"  # White
        self.text_bg_color = "#95F9E3"  #

        # setup of TKinter Stuff
        self.root = tk.Tk()
        self.root.geometry('1920x1080')
        self.root.title('taskManager')
        self.mainframe = tk.Frame(self.root, bg=self.background_color)
        self.mainframe.pack(fill='both', expand=True)

        # random tasks, delete
        # self.taskArray.append(Task("Goodbye", "bye", 3, 'January', '4', '2023'))
        # self.taskArray.append(Task("Bot march172024", "man bot", 2, 'March', '17', '2024'))
        # self.taskArray.append(Task("bot ZZ", "zz bot", 3, 'January', '4', '2023'))
        # self.taskArray.append(Task("Afirst one", "it better be", 1, 'January', '17', '2023'))
        # self.taskArray.append(Task("DJ KHALED", "we the best", 4, 'January', '16', '2023'))
        # self.taskArray.append(Task("may152024", "we h", 2, 'may', '15', '2024'))
        # self.taskArray.append(Task("dfwd", "we h", 4, 'January', '14', '2023'))
        # self.taskArray.append(Task("fger", "we h", 4, 'January', '9', '2023'))
        # self.taskArray.append(Task("dfe", "we h", 2, 'January', '8', '2023'))
        # self.taskArray.append(Task("asasas", "we h", 1, 'January', '7', '2023'))
        # self.taskArray.append(Task("fort", "we h", 2, 'January', '6', '2023'))
        # self.taskArray.append(Task("night", "we h", 2, 'January', '5', '2023'))
        # self.taskArray.append(Task("fork", "we h", 2, 'January', '4', '2023'))
        # self.taskArray.append(Task("april 2024", "we h", 2, 'April', '1', '2024'))
        # self.taskArray.append(Task("tswi", "we h", 2, 'January', '2', '2023'))
        # self.taskArray.append(Task("agr", "we h", 2, 'January', '1', '2023'))
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

    def sortduedate(self):
        filter = Filter()
        self.taskArray = filter.sortDueDate(self.taskArray)
        self.removealltext()
        self.printlist()

    def printlist(self):

        style = ttk.Style()
        style.theme_use('default')
        style.configure('TButton', background=self.button_bg_color, foreground=self.button_fg_color,
                        width=20, borderwidth=1, focusthickness=3)
        style.map('TButton', background=[('active', self.button_bg_color)])
        style.configure('TLabel', background=self.text_bg_color, foreground=self.text_color,
                        font=('Source Sans Pro', 20))

        self.text = ttk.Label(self.mainframe, text=' ' * 4 + "Task List:", font=('Source Sans Pro', 30))
        self.text.place(x=100, y=50)

        self.blank = ttk.Label(self.mainframe, text=' ', font=('Source Sans Pro', 30))
        self.blank.grid(row=0, column=0, pady=50)

        sort_by_button = ttk.Button(self.mainframe, text='Sort By', style='TButton')
        sort_by_button.place(x=1005, y=20)
        # sort_by_button.grid(row=0, column=4, pady=5, padx=(300, 0))
        sort_by_button.config(command=self.sort_by)

        add_task_button = ttk.Button(self.mainframe, text="Add Task", style='TButton', command=self.enterTasks)
        add_task_button.place(x=0, y=575, width=1550, height=325)
        # add_task_button.grid(row=13, column=4, padx=5, pady=(0, 30))
        # add_task_button.grid(sticky='NWES')

        search_button = ttk.Button(self.mainframe, text='Search', style='TButton')
        search_button.place(x=1200, y=20)
        # search_button.grid(row=0, column=5, pady=5)

        counter = 0

        for task in self.taskArray:
            # makes sure that there are 4 separate rows of tasks
            if 15 <= counter < 20:
                columnnum = -30
                rowchanger = 8

            elif 10 <= counter < 15:
                columnnum = -20
                rowchanger = 6

            elif 4 < counter < 10:
                columnnum = -10
                rowchanger = 2

            else:
                columnnum = 0
                rowchanger = 0

            self.text = ttk.Label(self.mainframe, text=task.getname(), style='TLabel')
            self.text.grid(row=2 + rowchanger, column=(counter * 2) + columnnum, pady=15, padx=(30, 10))
            self.descText = ttk.Label(self.mainframe, text=task.getdesc(), font=("Montserrat", 15))
            self.descText.grid(row=3 + rowchanger, column=(counter * 2) + columnnum, pady=(0, 30))
            self.priorityText = ttk.Label(self.mainframe, text='!' * int(task.get_priority()), foreground='red')
            self.priorityText.grid(row=2 + rowchanger, column=(counter * 2) + columnnum + 1)

            counter += 1

    def removealltext(self):
        for widget in self.mainframe.winfo_children():
            widget.destroy()

    def enterTasks(self):
        new_window = TaskWindow(self.taskArray)
        self.printlist()
    def sort_by(self):
        self.clicked = tk.StringVar()
        self.drop_menu = OptionMenu(self.root, self.clicked, "Alphabetically", "Alphabetically", "Priority", "Due Date",
                                    "Status")
        self.drop_menu.place(x=1005, y=60, width=195, height=31)
        self.sort_button = ttk.Button(self.mainframe, text="Sort", command=self.choose_sort, style='TButton')
        self.sort_button.place(x=1200, y=60)

    def choose_sort(self):
        self.sort_button.destroy()
        self.drop_menu.destroy()

        if self.clicked.get() == 'Alphabetically':
            self.sortbycommand()
        if self.clicked.get() == 'Due Date':
            self.sortduedate()


if __name__ == '__main__':
    TaskUI()
