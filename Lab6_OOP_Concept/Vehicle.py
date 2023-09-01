"""
1. จงเขียนโปรแกรมภาษาไพธอนเพื่อสร้างคลาสพาหนะชื่อ Vehicle ที่ประกอบไปด้วยคุณลักษณะ (attributes) คือ
ยี่ห้อรถ (brand)
รุ่นรถ (model)
สีรถ (color)
ความรเร็วสูงสุด (max speed)
ราคา (price)

2.จากข้อที่ 1 เขียนโปรแกรมเพื่อสร้างวัตถุ (object) จากคลาส Vehicle โดยรับข้อมูลจากผู้ใช้ตามคุณลักษณะ (attributes)ของคลาส
จากนั้นแสดงข้อมูลทางหน้าจอภาพ

"""

class Vehicle:
    #class attribute
    my_vihecle = []

    def __init__(self,brand,model,color,maxspeed,price):
        self.brand = brand
        self.model = model
        self.color = color
        self.maxspeed = maxspeed
        self.price = price
        #self.my_vihecle.append(self)

    def vehicle_detail(self):
        print(f'Brand:{self.brand} '
              f'Model:{self.model} '
              f'Color:{self.color} '
              f'Max speed: {self.maxspeed} '
              f'Price:{self.price}')

    def add_vehicle(self,new_vehicle):
        self.my_vihecle.append(new_vehicle)

    def delete_vehicle(self, index):
        self.my_vihecle.pop(index)

    def edit_vehicle_price(self,index,new_price):
        self.my_vihecle[index].price = new_price

    def edit_vehicle_color(self,index,new_color):
        self.my_vihecle[index].color = new_color