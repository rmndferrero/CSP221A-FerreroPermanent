class Robot:
    manufacturer = "ReymondRobotics"
    
    population_count = 0

    def __init__ (self, name, battery = 100):
        self.name = name
        self.battery = battery

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

    def __str__(self):
        return f"{self.name} ({self.battery}% battery)"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.battery!r})"

    
