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

    @staticmethod
    def printall(array):
        print('')
        for i in array:
            print(i.getname())