class Robot:
    manufacturer = "ReymondRobotics"
    
    population_count = 0

    def __init__ (self, name, battery = 100):
        self.name = name
        self.battery = battery
        Robot.population_count += 1

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, value):
        if value < 0:
            self._battery = 0
        elif value > 100:
            self._battery = 100
        else:
            self._battery = value

    def perform_task(self):
        if self.battery > 0:
            print("Power on..")
            self.battery -= 10
        else:
            print("Battery insufficient please charge the Robot.")
        return

    def __str__(self):
        return f"{self.name} ({self.battery}% battery)"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.battery!r})"

class CleaningRobot (Robot):
    
    def __init__(self, name, battery):
        super().__init__(name, battery)
        self.dust_capacity = 0

    @property
    def dust_capacity(self):
        return self._dust_capacity

    @dust_capacity.setter
    def dust_capacity(self, value):
            if value < 0:
                self._dust_capacity = 0
            elif value > 100:
                self._dust_capacity = 100
            else:
                self._dust_capacity = value
            
    def perform_task(self):
        if self.dust_capacity < 100 and self.battery >= 10:
            print("Cleaning the area..")
            self.dust_capacity += 10
            self.battery -= 10

        elif self.dust_capacity == 100 and self.battery >= 10:
            print("Please clear the dust compartment of the CleaningRobot.")

        elif self.dust_capacity < 100 and self.battery < 10:
            print("Please charge the CleaningRobot.")

        else:
            print("Please charge and clean the dust compartment of the CleaningRobot.")
    
class DrobeRobot(Robot):
    max_altitude = 1500

    def __init__(self, name, battery):
            super().__init__(name, battery)
    

    



    
