
class Task:
    def __init__(self, name, description, priority, due_date):
        self.description = description
        self.name = name
        self.due_date = due_date
        self.priority = priority
        # It is presumed that when a task is being added, it is not yet completed
        self.status = 'False'

    def getname(self):
        return self.name

    def getdesc(self):
        return self.description

    def get_priority(self):
        return self.priority

    def get_due_date(self):
        return self.due_date

    def get_status(self):
        return self.status

    def setname(self, newname):
        self.name = newname

    def set_description(self, new_desc):
        self.description = new_desc

    def set_priority(self, new_priority):
        self.priority = new_priority

    def set_due_date(self, new_date):
        self.due_date = new_date

    def set_status(self, new_status):
        self.status = new_status
