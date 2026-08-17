import logging
from functools import wraps
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO)

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__}")

        try:
            return func(*args, **kwargs)
        finally:
            logging.info(f"Finished {func.__name__}")

    return wrapper

class Robot(ABC):
    manufacturer = "ReymondRobotics"
    
    population = 0

    def __init__ (self, name, battery = 100):
        self.name = name
        self.battery = battery
        self.battery_usage = 10
        Robot.population += 1

    @classmethod
    def from_config(cls, config):
        return cls(config["name"], config.get("battery", 100))

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

    def use_battery(self, amount):
        if self.battery < amount:
            raise InsufficientBatteryError(
                self.name,
                amount,
                self.battery
            )
        self.battery -= amount

    @log_action
    @abstractmethod
    def perform_task(self):
        pass

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

    @log_action
    def perform_task(self):
            self.use_battery(self.battery_usage)
            self.dust_capacity += 10
            return "Cleaning the area.."
    
class DroneRobot(Robot):
    def __init__(self, name, battery = 100):
            super().__init__(name, battery)
            self.max_altitude = 1500
            self.battery_usage = 15

    @log_action
    def perform_task(self, height):
        if height > self.max_altitude:
            return "Maximum altitude is 1500m."

        self.use_battery(self.battery_usage)
        return f"Flying {height}m"

class InsufficientBatteryError(Exception):
    def __init__(self, name, required, available):
        self.name = name
        self.required = required
        self.available = available

        super().__init__(
            f"{name} needs {required}% battery for this task "
            f"but only has {available}%."
        )

def run_task_safely( robot , **kwargs):
    try:
        task_result = robot.perform_task(**kwargs)

    except InsufficientBatteryError as error:
        logging.error(error)

    else:
        print(task_result)

    finally: 
        print(f"Current battery: {robot.battery}")

def fleet_reports(fleet):
    for robots in fleet:
        print(str(robots))

drone = DroneRobot("SB", 10)
run_task_safely(drone, height=500)

robot = CleaningRobot.from_config({
    "name": "Roomba",
    "battery": 80
})
print(robot)

drone = DroneRobot.from_config({
    "name": "Aqua-Drone",
    "battery": 15
})
print(drone)

# 1.8 Mutable Class Attribute Trap Demonstration

class BuggyShoppingCart:
    items = []

    def add_item(self, item):
        self.items.append(item)


cart1 = BuggyShoppingCart()
cart2 = BuggyShoppingCart()

cart1.add_item("Apple")

print("Buggy version:")
print("Cart 1:", cart1.items)
print("Cart 2:", cart2.items)


# CORRECTED VERSION:
# The list is created inside __init__, so each instance gets its own independent list.

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)


cart1 = ShoppingCart()
cart2 = ShoppingCart()

cart1.add_item("Apple")

print("\nCorrected version:")
print("Cart 1:", cart1.items)
print("Cart 2:", cart2.items)



    
