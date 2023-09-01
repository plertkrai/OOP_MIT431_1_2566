from Vehicle import Vehicle

# option
def display_option():
    print("Welcome to Vehicle Data Store System (VDSS)")
    print("1.Add Vehicle")
    print("2.Delete Vehicle")
    print("3.Edit Vehicle Price")
    print("4.Display all Vehicle")
    print("5.exit")
    select = int(input("select(1-5)? : "))
    if select == 1:
        input_vehicle_data()
    elif select==2:
        delete_vehicle()
    elif select == 3:
        edit_vehicle()
    elif select==4:
        display_vehicle()
    elif select ==5:
        print("Good Bye.")
        exit(0)
    else:
        print("Please, select number 1-3.")

# add data
def input_vehicle_data():
    brand = input("Enter vehicle brand: ")
    model = input("Enter vehicle model: ")
    color = input("Enter vehicle color: ")
    maxspeed = int(input("Enter vehicle max speed:"))
    price = float(input("Enter vehicle price: "))

    #Vehicle.my_vihecle.append(Vehicle(brand,model,color,maxspeed,price))
    Vehicle.add_vehicle(Vehicle,Vehicle(brand,model,color,maxspeed,price))
    print("\n-----------------------------------")
    print("Already add vehicle to store.")
    print("-----------------------------------\n")


# display data
def display_vehicle():
    if len(Vehicle.my_vihecle) ==0:
        print("\nYou had no vehicle data.\n")
    else:
        print(f'You had {len(Vehicle.my_vihecle)} vehicle data following:')
        n = 1 # count
        for x in Vehicle.my_vihecle:
            print(f'[{n}]:',end=" ")
            x.vehicle_detail()
            n = n+1
        print("\n")

# delete vehicle
def delete_vehicle():
    # display all data in list
    display_vehicle()
    if len(Vehicle.my_vihecle) != 0:
        s = int(input("Select to delete?: "))

        Vehicle.delete_vehicle(Vehicle, s-1)
        print("\n-----------------------------------")
        print("Your data has been deleted.")
        print("-----------------------------------\n")

# edit vehicle price
def edit_vehicle():
    display_vehicle()
    if len(Vehicle.my_vihecle) != 0:
        s = int(input("Select to edit?: "))
        # display previous price
        l = 0
        while(l == 0):
            print(f'Please, select the option following: ')
            print(f'1. Edit color')
            print(f'2. Edit price')
            print(f'3. Exit from edit option')
            x = int(input(f'select(1 or 2): '))
            if x ==1:
                print(f'\nprevious color: {Vehicle.my_vihecle[s-1].color}')
                new_color = input("new color: ")
                Vehicle.edit_vehicle_color(Vehicle,s-1,new_color)
                print("\n-----------------------------------")
                print("Your data has been edited.")
                print("-----------------------------------\n")
            elif x ==2:
                print(f'\nprevious price: {Vehicle.my_vihecle[s-1].price}')
                new_price = float(input("new price: "))
                Vehicle.edit_vehicle_price(Vehicle,s-1,new_price)
                print("\n-----------------------------------")
                print("Your data has been edited.")
                print("-----------------------------------\n")
            elif x == 3:
                break
            else:
                print("Please, select number 1-3.")



# run application
s = 0
while s==0:
    display_option()


















