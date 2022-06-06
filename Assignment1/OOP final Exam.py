"""
Student Name: {Phatchadawadee Sariphat}
ID: {364211760035}
Group: {MIT212}
"""

class Student:
    def __init__(self, name, id, age, weight, height):
        # object Student
        self.name = name  # str
        self.id = id  # str
        self.age = age  # int
        self.weight = weight  # float
        self.height = height  # int

    def studentDetail(self):
        print(f'f{self.name} {self.id} {self.age} {self.weight} {self.height}')


S = input('Student Name?: ')
I = int(input('ID?: '))
A = int(input('Age?: '))
W = float(input('Weight?: '))
H = int(input('Height?: '))

class Vaccine:
    def __init__(self,vac_name):
        self.vac = vac_name
#getter and setter method
    def get_vacname(self):  # str
        return self.vac
    def set_vacname(self,new_name):
        self.vac = new_name
    def vaccine_detail(self):
        print(f'f{self.vac} ')
vac = input('How many are you vaccianted? : ')
print('1.sinovac')
print('2.astrazeneca')
print('3.johnson&johnson')
print('4.moderna')
print('5.sinopharm')
print('6.pfizer')
S1 = int(input('select: '))
D1 = input('Date(dd/mm/yyyy): ')
print('1.sinovac')
print('2.astrazeneca')
print('3.johnson&johnson')
print('4.moderna')
print('5.sinopharm')
print('6.pfizer')
S2 = int(input('select: '))
D2 = input('Date(dd/mm/yyyy): ')

class vaccinated:
    def add_vaccinated(self,vaccine):
        self.vaccine = vaccine

    def add_data(self, data):
        self.data = data
print('Student Infomation: ')
print('Student Name: ',S)
print('Age: ',A)
print('Weight: ',W)
print('Height',H)
print('vaccine 1: ',S1,'date: ',D1)
print('vaccine 2: ',S1,'date: ',D2)