import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkinter.ttk import OptionMenu
from Filter import Filter
from Task import Task

class TaskUI:
    def __init__(self):
        self.drop_menu = None
        self.priority_window = None
        self.change_name_window = None
        self.edit_task_window = None
        self.not_completed_image_grid = None
        self.completed_image_grid = None
        self.date_text = None
        self.task_window = None
        self.priority_drop_menu = None
        self.month_choice = None
        self.month_choice_menu = None
        self.day_choice_menu = None
        self.year_choice_menu = None
        self.day_choice = None
        self.priorityText = None
        self.priority_choices = None
        self.year_choice = None
        self.priorityVal = None
        self.desc_field = None
        self.name_field = None
        self.blank = None
        self.clicked = None
        self.sort_button = None
        self.text = None
        self.descText = None
        self.sort_by_boolean = False
        self.taskArray = []  # Creates an array, later to be filled with tasks

        # Set colors for readability
        self.background_color = "#95F9E3"
        self.text_color = "#53131E"  #
        self.button_bg_color = "#009FB7"  # Blue
        self.button_fg_color = "#FFFFFF"  # White
        self.text_bg_color = "#95F9E3"  #

        # setup of TKinter main window
        self.root = tk.Tk()
        self.root.geometry('1920x1080')
        self.root.title('taskManager')
        self.mainframe = tk.Frame(self.root, bg=self.background_color)
        self.mainframe.pack(fill='both', expand=True)

        # Check marks/not completed png
        self.completed = tk.PhotoImage(file='//Users//nathantamari//PycharmProjects//pythonProject//completed.png')
        self.not_completed = tk.PhotoImage(file='//Users//nathantamari//PycharmProjects//pythonProject//notCompleted'
                                                '.png')

        # Fills home page with current tasks
        self.printlist()
        self.root.mainloop()
        return

    def sort_alphabetically(self):  # triggered when user enters to sort alphabetically
        filter = Filter()
        self.taskArray = filter.sortAlpha(self.taskArray)
        self.removealltext()
        self.printlist()
        return

    def sort_due_date(self):  # triggered when user enters to sort by due date
        filter = Filter()
        self.taskArray = filter.sortDueDate(self.taskArray)
        self.removealltext()
        self.printlist()

    def sort_priority(self):
        filter = Filter()
        self.taskArray = filter.sort_priority(self.taskArray)
        self.removealltext()
        self.printlist()

    def sort_by_status(self):
        filter = Filter()
        self.taskArray = filter.sort_by_status(self.taskArray)
        self.removealltext()
        self.printlist()

    def printlist(self):  # organizes the task menu by whatever order the array is in
        style = ttk.Style()
        style.theme_use('default')
        style.configure('TButton', background=self.button_bg_color, foreground=self.button_fg_color,
                        width=20, borderwidth=1, focusthickness=3)
        style.map('TButton', background=[('active', 'blue')])
        style.configure('TLabel', background=self.text_bg_color, foreground=self.text_color,
                        font=('Source Sans Pro', 20))

        # place is used instead of grid because the sort by button should stay in the same place for
        # easier usability
        self.text = ttk.Label(self.mainframe, text=' ' * 4 + "Task List:", font=('Source Sans Pro', 30))
        self.blank = ttk.Label(self.mainframe, text=' ', font=('Source Sans Pro', 20))
        sort_by_button = ttk.Button(self.mainframe, text='Sort By', style='TButton')
        add_task_button = ttk.Button(self.mainframe, text="Add Task", style='TButton', command=self.enterTasks)

        sort_by_button.config(command=self.sort_by)
        self.text.place(x=100, y=50)
        self.blank.grid(row=0, column=0, pady=50)
        sort_by_button.place(x=1005, y=20)
        add_task_button.place(x=0, y=575, width=1550, height=325)
        counter = 0
        for task in self.taskArray:
            # if there is no due date, sets text to a blank string
            if task.get_year() == '' or task.get_month() == '' or task.get_day() == '':
                due_date_text = ''
            else:
                due_date_text = f'Due:  {task.get_month()} {task.get_day()}, {task.get_year()}.'

            # makes sure that there are 4 separate rows of tasks
            if 15 <= counter < 20:
                columnnum = -30
                rowchanger = 8

            elif 10 <= counter < 15:
                columnnum = -20
                rowchanger = 6

            elif 4 < counter < 10:
                columnnum = -10
                rowchanger = 3

            else:
                columnnum = 0
                rowchanger = 0

            # Creates the task menu: sets name, description, and how high priority it is
            self.text = ttk.Label(self.mainframe, text=task.getname(), style='TLabel')
            self.descText = ttk.Label(self.mainframe, text=task.getdesc(), font=("Montserrat", 15))
            self.priorityText = ttk.Label(self.mainframe, text='!' * int(task.get_priority()), foreground='red')
            self.date_text = ttk.Label(self.mainframe, text=due_date_text, font=("Montserrat", 15))

            self.text.grid(row=3 + rowchanger, column=(counter * 2) + columnnum, pady=(45, 20), padx=(30, 10))
            self.descText.grid(row=4 + rowchanger, column=(counter * 2) + columnnum, pady=(0, 30))
            self.priorityText.grid(row=3 + rowchanger, column=(counter * 2) + columnnum + 1, pady=(25, 0))
            self.date_text.grid(row=4 + rowchanger, column=(counter * 2) + columnnum, pady=(30, 0))

            self.constructTasks()

            counter += 1  # iterates

    def removealltext(self):  # When sort is called, this method removes the previous organized text
        for widget in self.mainframe.winfo_children():
            widget.destroy()

    def sort_by(self):  # created 'self.clicked', which stores which sort is used, and doesn't sort until choose_sort is
        # called.
        self.sort_by_boolean = not self.sort_by_boolean  # toggles boolean value

        if self.sort_by_boolean:
            self.clicked = tk.StringVar()
            self.drop_menu = OptionMenu(self.root, self.clicked, "Alphabetically", "Alphabetically", "Priority",
                                        "Due Date", "Status")
            self.drop_menu.place(x=1005, y=60, width=195, height=31)
            self.sort_button = ttk.Button(self.mainframe, text="Sort", command=self.choose_sort, style='TButton')
            self.sort_button.place(x=1200, y=60)
        else:
            self.sort_button.destroy()
            self.drop_menu.destroy()

    def choose_sort(self):  # removes sort by buttons and calls whichever sorting method is selected by the user
        self.sort_button.destroy()
        self.drop_menu.destroy()
        self.sort_by_boolean = not self.sort_by_boolean

        if self.clicked.get() == 'Alphabetically':
            self.sort_alphabetically()
        if self.clicked.get() == 'Due Date':
            self.sort_due_date()
        if self.clicked.get() == 'Priority':
            self.sort_priority()
        if self.clicked.get() == 'Status':
            self.sort_by_status()

    def enterTasks(self):  # creates task-entering window and "enter task" button

        if len(self.taskArray) > 14:
            messagebox.showinfo("Information", "You can only have a maximum of 15 tasks.")

        else:
            self.task_window = tk.Toplevel(self.root, bg=self.background_color)
            self.task_window.geometry('750x300')
            self.task_window.title('Enter Tasks')
            self.setupOptions(self.task_window)  # passes the window to the next method
            enter_task_button = ttk.Button(self.task_window, text="Enter Task", style='TButton',
                                           command=self.close_window)
            enter_task_button.grid(row=6, column=0, sticky='nwes', columnspan=4)

    def setupOptions(self, window):  # sets up labels and selection windows for data entry
        l1 = ttk.Label(window, text='Task Name', font=('Source Sans Pro', 25), foreground=self.button_bg_color)
        l2 = ttk.Label(window, text='Task Description', font=('Source Sans Pro', 25),
                       foreground=self.button_bg_color)
        l3 = ttk.Label(window, text='Priority', font=('Source Sans Pro', 25), foreground=self.button_bg_color)
        l4 = ttk.Label(window, text='Due Date', font=('Source Sans Pro', 25), foreground=self.button_bg_color)
        l1.grid(row=0, column=0, padx=5, pady=5)
        l2.grid(row=1, column=0, padx=5, pady=5)
        l3.grid(row=2, column=0, padx=5, pady=5)
        l4.grid(row=3, column=0, padx=5, pady=5)

        self.name_field = ttk.Entry(window, font=('Source Sans Pro', 20))
        self.desc_field = ttk.Entry(window, font=('Source Sans Pro', 20))

        # Creates and places OptionMenus for priority, due date
        self.priority_choices = tk.StringVar()
        self.priority_drop_menu = OptionMenu(window, self.priority_choices, "!", "!", "!!", "!!!", "!!!!")

        self.month_choice = tk.StringVar()
        self.month_choice.set('')
        self.month_choice_menu = OptionMenu(window, self.month_choice, self.month_choice.get(), 'January', 'February',
                                            'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                                            'November', 'December')
        self.day_choice = tk.StringVar()
        self.day_choice.set('')
        self.day_choice_menu = OptionMenu(window, self.day_choice, self.day_choice.get(), *range(1, 32))

        self.year_choice = tk.StringVar()
        self.year_choice.set('')
        self.year_choice_menu = OptionMenu(window, self.year_choice, self.year_choice.get(), '2023', '2024', '2025',
                                           '2026', '2027')

        # places all Option Menus in the grid
        self.name_field.grid(row=0, column=1, sticky='nwes', columnspan=3, padx=10, pady=15)
        self.desc_field.grid(row=1, column=1, sticky='nwes', columnspan=3, padx=10, pady=15)
        self.priority_drop_menu.grid(row=2, column=1, sticky='ew', columnspan=3)
        self.month_choice_menu.grid(row=3, column=1, sticky='ew')
        self.day_choice_menu.grid(row=3, column=2, sticky='ew')
        self.year_choice_menu.grid(row=3, column=3, sticky='ew')

    def close_window(self):  # If the task has a name, task is added to the array, and the window closes
        self.setPriority()
        self.realDate()
        if self.name_field.get() == '':
            messagebox.showinfo(title='', message='Please enter a task name.')
        else:
            self.taskArray.append(Task(self.name_field.get(), self.desc_field.get(), self.priorityVal,
                                       self.month_choice.get(), self.day_choice.get(), self.year_choice.get()))
            self.task_window.destroy()
            self.printlist()

    def setPriority(self):  # assigns a numerical value to however many '!'s there are
        if self.priority_choices.get() == "!!!!":
            self.priorityVal = 4
        elif self.priority_choices.get() == "!!!":
            self.priorityVal = 3
        elif self.priority_choices.get() == "!!":
            self.priorityVal = 2
        else:
            self.priorityVal = 1

    def realDate(self):  # Makes sure the date is real (no February 31st for example)
        if self.month_choice.get() in ['February', 'April', 'June', 'September', 'November']:
            if self.day_choice.get() == '31':
                self.day_choice.set('30')
        if self.day_choice.get() == '30' and self.month_choice.get() == 'February':
            self.day_choice.set('28')
        if self.day_choice.get() == '29' and self.month_choice.get() == 'February' and self.year_choice.get() != "2024":
            self.day_choice.set('28')

    def constructTasks(self):  # creates a clickable button on each task to edit all tasks
        max_buttons = min(len(self.taskArray), 15)
        for i in range(max_buttons):
            button = ttk.Button(self.mainframe, command=lambda t=self.taskArray[i]: self.edit_button_pressed(t),
                                style='TLabel')
            if self.taskArray[i].get_status():
                button.config(image=self.completed)
            else:
                button.config(image=self.not_completed)
            button.grid(row=4 + (i // 5) * 3, column=1 + (i % 5) * 2)

    def edit_button_pressed(self, task):  # creates popup window that deals with editing the tasks
        self.printlist()

        self.edit_task_window = tk.Toplevel(self.root, bg=self.background_color)
        self.edit_task_window.geometry('650x175')
        self.edit_task_window.title('Edit Tasks')

        edit_name = ttk.Button(self.edit_task_window, text="Edit Name", style='TButton',
                               command=lambda: self.change_name(task))
        edit_desc = ttk.Button(self.edit_task_window, text="Edit Description", style='TButton',
                               command=lambda: self.change_desc(task))
        edit_priority = ttk.Button(self.edit_task_window, text="Change Priority", style='TButton',
                                   command=lambda: self.change_priority(task))
        edit_status = ttk.Button(self.edit_task_window, text="Change Status", style='TButton',
                                 command=lambda: self.change_status(task))
        edit_due_date = ttk.Button(self.edit_task_window, text="Change Due Date", style='TButton',
                                   command=lambda: self.edit_due_date(task))
        delete_task = ttk.Button(self.edit_task_window, text="Delete Task", style='TButton',
                                 command=lambda: self.delete_task(task))

        edit_name.grid(row=0, column=0, padx=10, pady=(10, 50))
        edit_desc.grid(row=0, column=1, padx=10, pady=(10, 50))
        edit_priority.grid(row=0, column=2, padx=10, pady=(10, 50))
        edit_status.grid(row=1, column=0, padx=10, pady=(10, 50))
        edit_due_date.grid(row=1, column=1, padx=10, pady=(10, 50))
        delete_task.grid(row=1, column=2, padx=10, pady=(10, 50))

    def change_name(self, task):
        self.edit_task_window.destroy()  # gets rid of other pop-up window
        old_name = task.getname()

        result = ""
        while result == "":
            result = simpledialog.askstring("Text Input", "Enter your text:")

        if result is None:  # if cancel is pressed, the value is saved as the old name
            result = old_name

        task.setname(result)
        self.removealltext()
        self.printlist()

    def change_status(self, task):
        if task.get_status():
            task.set_status(False)
        else:
            task.set_status(True)
        self.edit_task_window.destroy()
        self.removealltext()
        self.printlist()

    def change_desc(self, task):
        self.edit_task_window.destroy()  # gets rid of other pop-up window
        old_name = task.getdesc()

        result = ""
        while result == "":
            result = simpledialog.askstring("Text Input", "Enter your text:")

        if result is None:  # if cancel is pressed, the value is saved as the old name
            result = old_name

        task.set_description(result)
        self.removealltext()
        self.printlist()

    def change_priority(self, task):
        self.edit_task_window.destroy()  # gets rid of other pop-up window

        self.priority_window = tk.Toplevel(self.root, bg=self.background_color)
        self.priority_window.geometry('820x150')
        self.priority_window.title('Edit Priority')

        p1 = ttk.Button(self.priority_window, text="!", style='TButton', command=lambda: self.set_priority(task, 1))
        p2 = ttk.Button(self.priority_window, text="!!", style='TButton', command=lambda: self.set_priority(task, 2))
        p3 = ttk.Button(self.priority_window, text="!!!", style='TButton', command=lambda: self.set_priority(task, 3))
        p4 = ttk.Button(self.priority_window, text="!!!!", style='TButton', command=lambda: self.set_priority(task, 4))

        p1.grid(row=0, column=0, padx=5, pady=40)
        p2.grid(row=0, column=1, padx=5, pady=40)
        p3.grid(row=0, column=2, padx=5, pady=40)
        p4.grid(row=0, column=3, padx=5, pady=40)

    def set_priority(self, task, num):
        task.set_priority(num)
        self.priority_window.destroy()
        self.removealltext()
        self.printlist()

    def edit_due_date(self, task):
        self.edit_task_window.destroy()
        due_date_window = tk.Toplevel(self.root, bg=self.background_color)
        due_date_window.geometry('300x125')
        due_date_window.title('Edit Due Date')

        month_choice = tk.StringVar()
        month_choice.set(task.get_month())
        month_choice_menu = OptionMenu(due_date_window, month_choice, month_choice.get(), 'January', 'February',
                                       'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                                       'November', 'December')
        day_choice = tk.StringVar()
        day_choice.set(task.get_day())
        day_choice_menu = OptionMenu(due_date_window, day_choice, day_choice.get(), *range(1, 32))

        year_choice = tk.StringVar()
        year_choice.set(task.get_year())
        year_choice_menu = OptionMenu(due_date_window, year_choice, year_choice.get(), '2023', '2024',
                                      '2025', '2026', '2027')

        select_button = ttk.Button(due_date_window, text='Set',
                                   command=lambda: self.change_due_date(task, due_date_window,
                                                                        month_choice.get(), day_choice.get(),
                                                                        year_choice.get()))

        # places all Option Menus in the grid
        month_choice_menu.grid(row=0, column=1, padx=10, pady=10)
        day_choice_menu.grid(row=0, column=2, padx=10, pady=10)
        year_choice_menu.grid(row=0, column=3, padx=10, pady=10)
        select_button.grid(row=4, column=0, padx=10, pady=10, sticky='ew', columnspan=4)

    def change_due_date(self, task, window, month, day, year):
        window.destroy()
        task.set_month(month)
        task.set_day(day)
        task.set_year(year)
        self.removealltext()
        self.printlist()

    def delete_task(self, task):
        self.edit_task_window.destroy()
        self.taskArray.remove(task)
        self.removealltext()
        self.printlist()


if __name__ == '__main__':
    TaskUI()
