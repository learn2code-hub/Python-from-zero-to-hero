import math

class Student:
    def __init__(self, grades):
        self.__grades = grades[:]

    def computeAverage(self):
        grades_sum = 0
        for grade in self.__grades:
            grades_sum += grade
        average =  grades_sum / len(self.__grades)
        return math.trunc(average * 100) / 100

    @classmethod
    def computeSum(cls, a, b):
        return a + b