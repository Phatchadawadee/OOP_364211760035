"""
Student Name: {Phatchadawadee Sariphat}
ID: {035}
Group: {MIT212}
"""

# class attributes

class Student:
    major = 'MT'

    def __init__(self,name,group):
        self.name = name
        self.group = group
    def introduce(self):
        print(f'My name is {self.name}, I\'m in {self.group} and'
              f'studying in {self.major} major.')

std1 = Student('Phatchadawadee Sariphat', 'MIT212')
std1.introduce()

std2 = Student('Puriwat Lertkrai', 'MIT211')
std2.introduce()

Student.major = 'LM'

std1.introduce()
std2.introduce()

std2.group = 'LM211'
std2.introduce()