"""
OOP Exercise Chapter 6

1. จงเขียนโปรแกรมภาษาไพธอนเพื่อสร้างคลาสพาหนะชื่อ Vehicle ที่ประกอบไปด้วยคุณลักษณะ (attributes) คือ
ยี่ห้อรถ (brand)
รุ่นรถ (model)
สีรถ (color)
ความรเร็วสูงสุด (max speed)
ราคา (price)

2.จากข้อที่ 1 เขียนโปรแกรมเพื่อสร้างวัตถุ (object) จากคลาส Vehicle โดยรับข้อมูลจากผู้ใช้ตามคุณลักษณะ (attributes) ของคลาส
จากนั้นแสดงข้อมูลทางหน้าจอภาพ

"""


class Vehicle:
    def __init__(self,bran,color,maxspeed,price):
        # object attributes
        self.brand = bran
        self.color = color
        self.maxs = maxspeed  # int
        self.price = price  # float

    def displayDetail(self):
        print(f'f{self.brand} {self.color} {self.maxs} {self.price}')

b = input('Vehicel brand: ')
c = input('Color: ')
m = int(input('Max speed: '))
p = float(input('Price: '))

v = Vehicle(b,c,m,p)
v.displayDetail()
