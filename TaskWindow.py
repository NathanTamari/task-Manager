import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.ttk import OptionMenu

from Task import Task


class TaskWindow:
    def __init__(self, array):
        self.mainframe2 = None
        self.window = None
        self.priority_drop_menu = None
        self.month_choice = None
        self.priority_choices = None
        self.month_choice_menu = None
        self.name_field = None
        self.day_choice = None
        self.day_choice_menu = None
        self.year_choice = None
        self.year_choice_menu = None
        self.desc_field = None
        self.priorityVal = None
        self.array = array
        # Set colors for readability
        self.background_color = "#95F9E3"  # Light gray
        self.text_color = "#53131E"  #
        self.button_bg_color = "#009FB7"  # Blue
        self.button_fg_color = "#FFFFFF"  # White
        self.text_bg_color = "#95F9E3"
        self.enterTasks()
        return

    def enterTasks(self):
        # setup of TKinter Stuff
        self.window = tk.Tk()
        self.window.title('Enter Tasks')
        self.window.geometry('750x250')

        self.setupOptions()
        self.realDate()

    def close_window(self):
        month = self.month_choice.get()
        day = self.day_choice.get()
        year = self.year_choice.get()
        print(f'{month}, {day}, {year}')

        self.setPriority()
        if self.name_field.get() == '':
            messagebox.showinfo(title='', message='Please enter a task name.')
        else:
            print(f'{self.month_choice.get()}, {self.day_choice.get()}, {self.year_choice.get()}')
            self.array.append(Task(self.name_field.get(), self.desc_field.get(), self.priorityVal,
                                   self.month_choice.get(), self.day_choice.get(), self.year_choice.get()))
            self.window.destroy()

    def setupOptions(self):


        l1 = ttk.Label(self.window, text='Task Name', font=('Source Sans Pro', 25), foreground=self.button_bg_color)
        l2 = ttk.Label(self.window, text='Task Description', font=('Source Sans Pro', 25), foreground=self.button_bg_color)
        l3 = ttk.Label(self.window, text='Priority', font=('Source Sans Pro', 25), foreground=self.button_bg_color)
        l4 = ttk.Label(self.window, text='Due Date', font=('Source Sans Pro', 25), foreground=self.button_bg_color)
        l1.grid(row=0, column=0, padx=5, pady=5)
        l2.grid(row=1, column=0, padx=5, pady=5)
        l3.grid(row=2, column=0, padx=5, pady=5)
        l4.grid(row=3, column=0, padx=5, pady=5)

        self.name_field = ttk.Entry(self.window, font=('Source Sans Pro', 30))
        self.desc_field = ttk.Entry(self.window, font=('Source Sans Pro', 30))

        # Creates and places OptionMenus for priority, due date
        self.priority_choices = tk.StringVar()
        self.priority_drop_menu = OptionMenu(self.window, self.priority_choices, "!", "!", "!!", "!!!", "!!!!")

        self.month_choice = tk.StringVar()
        self.month_choice.set('January')
        self.month_choice_menu = OptionMenu(self.window, self.month_choice, self.month_choice.get(), 'January', 'February', 'March',
                                            'April', 'May', 'June', 'July', 'August', 'September', 'October',
                                            'November', 'December')
        self.day_choice = tk.StringVar()
        self.day_choice.set('1')
        self.day_choice_menu = OptionMenu(self.window, self.day_choice, self.day_choice.get(), '1', '2', '3', '4', '5', '6', '7', '8',
                                          '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
                                          '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')

        self.year_choice = tk.StringVar()
        self.year_choice.set('2023')
        self.year_choice_menu = OptionMenu(self.window, self.year_choice, self.year_choice.get(), '2023', '2024', '2025', '2026',
                                           '2027')

        # places all Option Menus in the grid
        self.name_field.grid(row=0, column=1, sticky='nwes', columnspan=3)
        self.desc_field.grid(row=1, column=1, sticky='nwes', columnspan=3)
        self.priority_drop_menu.grid(row=2, column=1, sticky='ew', columnspan=3)
        self.month_choice_menu.grid(row=3, column=1, sticky='ew')
        self.day_choice_menu.grid(row=3, column=2, sticky='ew')
        self.year_choice_menu.grid(row=3, column=3, sticky='ew')

        enter_task_button = ttk.Button(self.window, text="Enter Task", style='TButton', command=self.close_window)
        enter_task_button.grid(row=6, column=0, sticky='nwes', columnspan=4)

    def setPriority(self):
        if self.priority_choices.get() == "!!!!":
            self.priorityVal = 4
        elif self.priority_choices.get() == "!!!":
            self.priorityVal = 3
        elif self.priority_choices.get() == "!!":
            self.priorityVal = 2
        else:
            self.priorityVal = 1

    def realDate(self):
        # Makes sure the date is real (no February 31st for example)
        if self.month_choice.get() in ['February', 'April', 'June', 'September', 'November']:
            if self.day_choice.get() == '31':
                self.day_choice.set('30')
        if self.day_choice.get() == '30' and self.month_choice.get() == 'February':
            self.day_choice.set('28')
        if self.day_choice.get() == '29' and self.month_choice.get() == 'February' and self.year_choice.get() != "2024":
            self.day_choice.set('28')

