"""
exercise lab7:
Option menu
1. add ev car
2. display all ev car
3. exit
"""

from evcar import ThaiEvCar

e = ThaiEvCar(1001,"Tesla","Model 3",6.1,347,559,1759000)


# display data by using getter
print(e.get_id(),e.get_brand(),e.get_model())

e.ev_car_detail()

e.set_price(1650000)
e.ev_car_detail()