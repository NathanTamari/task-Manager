
class Task:
    def __init__(self, name, description, priority, month, day, year):
        self.description = description
        self.name = name
        self.month = month
        self.day = day
        self.year = year
        self.priority = priority
        # It is presumed that when a task is being added, it is not yet completed
        self.status = 'False'

    def getname(self):
        return self.name

    def getdesc(self):
        return self.description

    def get_priority(self):
        return self.priority

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def get_year(self):
        return self.year

    def get_status(self):
        return self.status

    def setname(self, newname):
        self.name = newname

    def set_description(self, new_desc):
        self.description = new_desc

    def set_priority(self, new_priority):
        self.priority = new_priority

    def set_month(self, new_month):
        self.month = new_month

    def set_day(self, new_day):
        self.day = new_day

    def set_year(self, new_year):
        self.year = new_year

    def set_status(self, new_status):
        self.status = new_status
