class Sensor:
    def __init__(self, id, car_park,is_active=False):
        self.is_active = is_active
        self.id = id
        self.car_park = car_park

    def __str__(self):
        return f'{self.id}: Sensor is {"displaying" if self.is_active else "is not active"}'


class EntrySensor(Sensor):
        ...

class ExitSensor(Sensor):
            ...


