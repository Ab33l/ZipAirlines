from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase
from django.conf import settings

from zipairlines.calculations import ZipAirCalculations


class AirplaneUtilsTests(SimpleTestCase):

    def setUp(self):
        self.airplane = {
            'id': 2,
            'passengers': 150
        }
        self.airplane_utils = ZipAirCalculations(self.airplane)

    def test__tank_capacity(self):

        self.assertEqual(
            self.airplane_utils.tank_capacity,
            round(2 * 200, 4)
        )

    def test__per_passenger_consumption(self):

        self.assertEqual(
            self.airplane_utils.per_passenger_consumption,
            round(150 * 0.002, 4)
        )

    def test__airplane_consumption(self):

        self.assertEqual(
            self.airplane_utils.airplane_consumption,
            round(2 * 0.80, 4)
        )

    def test__per_minute_fuel_consumption(self):

        self.assertEqual(
            self.airplane_utils.per_minute_fuel_consumption,
            round(
                ((2 * 0.80) + (150 * 0.002)),
                4
            )
        )

    def test__max_fly_minutes(self):
        '''
        Test max_fly_minutes property
        '''

        self.assertEqual(
            self.airplane_utils.max_fly_minutes,
            round(
                (2 * 200) / ((2 * 0.80) + (
                    150 * 0.002)),
                4
            )
        )

    def test__fuel_required(self):

        for i in range(1, 10):
            airplane = {
                'id': i,
                'passengers': i*20
            }

            ap = ZipAirCalculations(airplane)

            airplane_consumption = airplane['id'] * settings.MULTIPLIED_VALUE
            per_passenger_consumption = airplane['passengers'] * settings.FUEL_BY_PASSENGER

            fuel_capacity = (airplane_consumption + (
                per_passenger_consumption * airplane['passengers']))

            self.assertEqual(ap.fuel_required, round(fuel_capacity, 4))