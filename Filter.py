class Filter:
    def __init__(self):
        self.null_array = None
        print('')

    def sortAlpha(self, array):
        counter = 1
        while counter > 0:
            counter = 0
            # when counter is 0, the array is in alphabetical order, and while loop ends
            index = 0
            for currentTask in array:
                if index + 1 != len(array):
                    if self.comparestrings(array[index].getname(), array[index + 1].getname()) == currentTask.getname():
                        index += 1
                    else:
                        temp = currentTask
                        array[index] = array[index + 1]
                        array[index + 1] = temp
                        index += 1
                        counter += 1
                # put string at current index and next index into comparestrings. if it returns current index,
                # you are good

        return array

    @staticmethod
    def comparestrings(string1, string2):
        # returns the string that comes first in alphabetical order

        if len(string1) > len(string2):
            smallerstring = string2
            largerstring = string1
        else:
            smallerstring = string1
            largerstring = string2

        count = 0
        for char in range(len(smallerstring)):
            # makes sure capital letters aren't ranked higher than lowercase (by default ASCII ranks like that
            val1 = ord(smallerstring[count:count + 1])
            val2 = ord(largerstring[count:count + 1])
            if val1 > 90:
                val1 -= 32
            if val2 > 90:
                val2 -= 32

            # statement comparing values previously adjusted
            if val1 < val2:
                return smallerstring
            elif val2 < val1:
                return largerstring
            else:
                count += 1
        return smallerstring

    def sortDueDate(self, array):  # takes initial array, returns array sorted by which due date is soonest

        null_array = []

        for i in array:  # removes all tasks with empty due dates and puts them in another array
            if i.get_year() == '' or i.get_month() == '' or i.get_day() == '':
                null_array.append(i)
                array.remove(i)

        counter = 1
        while counter > 0:
            counter = 0
            # when counter is 0, the array is in the right order, and while loop ends
            index = 0
            for currentTask in array:
                if index + 1 != len(array):
                    if self.earlierDate(array[index], array[index + 1]):
                        index += 1
                    else:
                        temp = currentTask
                        array[index] = array[index + 1]
                        array[index + 1] = temp
                        index += 1
                        counter += 1
                # put string at current index and next index into comparestrings. if it returns current index,
                # you are good

        for i in null_array:
            array.append(i)
        return array

    @staticmethod
    def printall(array):  # delete this just for tesring
        print('')
        for i in array:
            print(i.getname())

    def earlierDate(self, task1, task2):  # returns true if the first task has an earlier due date than the second task

        if task1.get_year() == '' or task1.get_month() == '' or task1.get_day() == '':
            return False
        if task2.get_year() == '' or task2.get_month() == '' or task2.get_day() == '':
            return True

        year1 = int(task1.get_year())
        year2 = int(task2.get_year())
        month1 = self.monthToInt(task1.get_month())
        month2 = self.monthToInt(task2.get_month())
        day1 = int(task1.get_day())
        day2 = int(task2.get_day())

        if year1 < year2:
            return True

        elif year2 < year1:
            return False

        elif month1 < month2:
            return True

        elif month2 < month1:
            return False

        elif day1 < day2:
            return True

        elif day2 < day1:
            return False

        elif day1 == day2:
            return True

        else:
            return False

    def monthToInt(self, month):  # converts Month of
        if month == 'January':
            return 1
        if month == 'February':
            return 2
        if month == 'March':
            return 3
        if month == 'April':
            return 4
        if month == 'May':
            return 5
        if month == 'June':
            return 6
        if month == 'July':
            return 7
        if month == 'August':
            return 8
        if month == 'September':
            return 9
        if month == 'October':
            return 10
        if month == 'November':
            return 11
        if month == 'December':
            return 12

    @staticmethod
    def sort_priority(array):
        counter = 1
        while counter > 0:
            counter = 0
            # when counter is 0, the array is in the right order, and while loop ends
            index = 0
            for currentTask in array:
                if index + 1 != len(array):
                    if array[index].get_priority() >= array[index+1].get_priority():
                        index += 1
                    else:
                        temp = currentTask
                        array[index] = array[index + 1]
                        array[index + 1] = temp
                        index += 1
                        counter += 1
        return array
