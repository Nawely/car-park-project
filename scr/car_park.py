from sensor import Sensor
from display import Display


class CarPark:

    def __init__(self, location="Moondalup", capacity=100, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    @property
    def available_bays(self):
        return self.capacity - len(self.plates)

    def __str__(self):
        return f'Please enjoy your stay at {self.location} car park with {self.capacity}bays '

    def register_sensor(self, sensor):
        self.sensors.append(sensor)

    def register_display(self, display):
        self.sensors.append(display)

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Invalid component type,Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()

    def update_displays(self):
        data = {"Bays": self.available_bays, "temperature": 48}
        for display in self.displays:
            display.update(data)
            print(f"Updating: {display}")



