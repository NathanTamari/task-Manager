class Filter:
    def __init__(self):
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

    def sortDueDate(self,array):

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

        return array

    @staticmethod
    def printall(array):
        print('')
        for i in array:
            print(i.getname())

    def earlierDate(self, task1, task2):
        # returns true if the first task has an earlier due date than the second task
        year1 = int(task1.get_year())
        year2 = int(task2.get_year())
        month1 = self.monthToInt(task1.get_month())
        month2 = self.monthToInt(task2.get_month())
        day1 = int(task1.get_day())
        day2 = int(task2.get_day())

        if year1 < year2:
            return True
        elif month1 < month2:
            return True
        elif day1 < day2:
            return True
        elif day1 == day2:
            return True
        else:
            return False

    def monthToInt(self, month):
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
        else:
            return 12