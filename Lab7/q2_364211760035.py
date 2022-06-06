"""
name: {Phatchadawadee  Sariphat}
id: {035}
group: {MIT212}
"""

# create class
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f'My name is {self.name}, I am {self.age} year old.'

# create object
obj = Person('Puriwat Lertkrai',35)
print(obj.introduce())

n = input('Enter your name: ')
a = int(input('How old are you: '))

obj2 = Person(n,a)
print(obj2.introduce())

myperson = [obj,obj2]

# loop
for x in myperson:
    print(x.introduce())