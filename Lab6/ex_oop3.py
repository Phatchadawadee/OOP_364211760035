"""
Student Name: {Phatchadawadee Sariphat}
ID: {035}
Group: {MIT212}
"""

class Teacher:
    def __init__(self,name):
        self.name = name
    def introuduce(self):
        print(f'Mt name is {self.name}, Iam a Teacher.')

class Student:
    def __init__(self,name):
        self.name = name
    def introuduce(self):
        print(f'Mt name is {self.name}, I am a Student.')

mylist = []
t = Teacher('Puriwat Lertkrai')
s = Student('Jatuphon Chit')

mylist.append(t)
mylist.append(s)

#print(mylist, len(mylist))

for x in mylist:
    x.introuduce()