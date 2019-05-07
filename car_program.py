# Created by: Chris Asante
# Created on: 7-May-2019
# Created for: ICS3U
# Unit 8-03
# This main program will create a car object

from car import *

car1 = Car()
car2 = Car()

print("Car 1:")
car1.set_license_plate_number("4321UYT")
print("Speed: " + str(car1.get_speed()) + "km/h")
car1.set_gear(3)
car1.set_gear(5)
car1.set_gear(7)
car1.brake(50)
car1.brake(100)

print("\nCar 2:")
car2.set_license_plate_number("1234TYU")
print("Paint colour: " + str(car2.get_colour()))
car2.set_license_plate_number("6789QWE")
car2.set_colour("black")
car2.set_license_plate_number("F1GUR380")
car2.set_colour("red")