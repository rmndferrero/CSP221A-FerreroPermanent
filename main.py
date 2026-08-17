class Robot:
    manufacturer = "ReymondRobotics"
    
    population_count = 0

    def __init__ (self, name, battery = 100):
        self.name = name
        self.battery = battery
        self.battery_usage = 10
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

    def use_battery(self, value):
        if value < 0:
            value == 0
        else:
            self.battery -= value
    
    def perform_task(self):
        if self.battery >= self.battery_usage:
            print("Power on..")
            self.use_battery(self.battery_usage)
        else:
            raise InsufficientValueError(self.name, self.battery, self.battery_usage)
        return

    def __str__(self):
        return f"{self.name} ({self.battery}% battery)"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.battery!r})"

class CleaningRobot(Robot):
    
    def __init__(self, name, battery = 100):
        super().__init__(name, battery)
        self.dust_capacity = 0
        self.battery_usage = 20

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
        if self.dust_capacity < 100 and self.battery >= self.battery_usage:
            print("Cleaning the area..")
            self.dust_capacity += 10
            self.use_battery(self.battery_usage)

        elif self.dust_capacity == 100 and self.battery >= self.battery_usage:
            print("Please clear the dust compartment of the CleaningRobot.")

        elif self.dust_capacity < 100 and self.battery < self.battery_usage:
            raise InsufficientValueError(self.name, self.battery, self.battery_usage)
        else:
            print("Please charge and clean the dust compartment of the CleaningRobot.")
    
class DroneRobot(Robot):
    def __init__(self, name, battery = 100):
            super().__init__(name, battery)
            self.max_altitude = 1500
            self.battery_usage = 15

    def perform_task(self, height):
        if height > self.max_altitude:
            print("Maximum altitude is 1500m.")
        elif self.battery < self.battery_usage:
            raise InsufficientValueError(self.name, self.battery, self.battery_usage)
        else:
            print(f"Flying {height}m")
            self.use_battery(self.battery_usage)

class InsufficientValueError(Exception):
    def __init__(self, name, battery, use_battery):
        super().__init__(f"{name} needs {use_battery}% battery for this task but only has {battery}%.")
        self.battery = battery
        self.use_battery = use_battery

def run_task_safely( robot , **kwargs):
    try:
        task_result = robot.perform_task(**kwargs)

    except InsufficientValueError as error:
        print(f"{error}")

    else:
        print(task_result)

    finally: 
        print(f"Current battery: {robot.battery}")

def fleet_reports(fleet):
    for robots in fleet:
        print(robots)

drone = DroneRobot("SB", 10)
run_task_safely(drone, height = 500)

    



    
