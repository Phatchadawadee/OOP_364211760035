"""
OOP Exercise Chapter 6

1. จงเขียนโปรแกรมภาษาไพธอนเพื่อสร้างคลาสพาหนะชื่อ Vehicle ที่ประกอบไปด้วยคุณลักษณะ (attributes) คือ
ยี่ห้อรถ (brand)
รุ่นรถ (model)
สีรถ (color)
ความรเร็วสูงสุด (max speed)
ราคา (price)

2.จากข้อที่ 1 เขียนโปรแกรมเพื่อสร้างวัตถุ (object) จากคลาส Vehicle โดยรับข้อมูลจากผู้ใช้ตามคุณลักษณะ (attributes)ของคลาส
จากนั้นแสดงข้อมูลทางหน้าจอภาพ

"""
from Vehicle import Vehicle

Vehicle_store = []
num = int(input('คุณมีรถกี่คัน?:'))

for x in range(num):
    brand = input('ยี่ห้อรถ:')
    model = input('รุ่นรถ:')
    color = input('สีรถ:')
    max_speed = input('ความรเร็วสูงสุด:')
    price = float(input('ราคา:'))

    a = Vehicle(brand,model,color,max_speed,price)
    Vehicle_store.append(a)

def display_Vehicle(Vehicle):
    print('จำนวนรถทั้งหมด:',len(Vehicle))
    for x in Vehicle:
        x.Vehicle_detail()

display_Vehicle(Vehicle_store)



class Vehicle:
    def __init__(self,brandname,model,color,max_speed,price):
        # object attributes
        self.brandname = brandname
        self.model = model
        self.color = color
        self.max_speed = max_speed
        self.price = price

    def Vehicle_detail(self):
        print(f'brandname:{self.brandname} model: {self.model} '
              f'color:{self.color} max_speed:{self.max_speed} price: {self.price}  THB')