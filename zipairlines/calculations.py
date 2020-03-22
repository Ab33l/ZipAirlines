from django.conf import settings


class ZipAirCalculations(object):

    def __init__(self, airplane):
        self.airplane = airplane

    @property
    def tank_capacity(self):
        value = self.airplane['id'] * settings.TANK_LITERS
        return round(value, 4)

    @property
    def fuel_required(self):
        value = self.airplane_consumption + self.per_passenger_consumption * self.airplane['passengers']
        return round(value, 4)

    @property
    def per_passenger_consumption(self):
        value = self.airplane['passengers'] * settings.FUEL_BY_PASSENGER
        return round(value, 4)

    @property
    def airplane_consumption(self):
        value = self.airplane['id'] * settings.MULTIPLIED_VALUE
        return round(value, 4)

    @property
    def per_minute_fuel_consumption(self):
        value = self.airplane_consumption + self.per_passenger_consumption
        return round(value, 4)

    @property
    def max_fly_minutes(self):
        value = self.tank_capacity / self.per_minute_fuel_consumption
        return round(value, 4)
