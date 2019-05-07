# Created by: Chris Asante
# Created on: 7-May-2019
# Created for: ICS3U
# Unit 8-03
# This main program will create a car object

class Car:
    
    def __init__(self):
        #private fields
        
        self.__license_plate_number = "TY4SDF3"
        self.__colour = "orange"
        self.__number_of_doors = 4
        self.__speed = 25.0
        self.__gear = 1
        self.__number_of_wheels = 4
        self.__number_of_tires = 4
    
    # properties
    
    def get_license_plate_number(self):
        #get the license plate number property
        return self.__license_plate_number
    
    def set_license_plate_number(self, new_license_plate_number):
        #set the license plate number property
        if not len(new_license_plate_number) == 7:
            # license plate should not be changed
            print("the license plate must be 7 characters long.")
        else:
            self.__license_plate_number = new_license_plate_number
        print("License plate number: " + str(self.__license_plate_number))
    
    def get_colour(self):
        #get the colour property
        return self.__colour
    
    def set_colour(self, new_colour):
        #set the colour property
        if new_colour == "nil":
            #Nothing should change
            pass
        else:
            self.__colour = new_colour
        print("Paint colour: " + str(self.__colour))
    
    def get_number_of_doors(self):
        #get the number of doors property
        return self.__number_of_doors
    
    def get_speed(self):
        #get the speed property
        return self.__speed
    
    def get_gear(self):
        #get the gear property
        return self.__gear
    
    def set_gear(self, new_gear):
        #set the gear property
        if new_gear < 1 or new_gear > 6:
            # nothing happens because this gear is invalid
            pass
        else:
            self.__gear = new_gear
            self.__speed_recalculate()
        print("Gear: " + str(self.__gear))
        print("Speed: " + str(self.__speed) + "km/h")
    
    def get_number_of_wheels(self):
        #get the number of wheels
        return self.__number_of_wheels
    
    def get_number_of_tires(self):
        #get the number of tires
        return self.__number_of_tires
    
    #private methods
    def __speed_recalculate(self):
        #Calculates the speed
        self.__speed = self.__gear * 20
    
    #public methods
    def brake(self, speed_decrease):
        #decreases the speed
        if speed_decrease < 0:
            #Nothing should happen
            pass
        elif speed_decrease > self.__speed:
            self.__speed = 0
        else:
            self.__speed = self.__speed - speed_decrease
        print("Speed: " + str(self.__speed) + "km/h")