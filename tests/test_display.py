import unittest
from display import Display
from car_park import CarPark

# ... inside the TestDisplay class


class TestCarPark(unittest.TestCase):

    def setUp(self):
        self.car_park = CarPark("Moondalup", 100)

        self.display = Display(1, CarPark(), message="Welcome to the car park", is_on=False)

    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.message, "Welcome to the car park")
        self.assertEqual(self.display.is_on, False)
        self.assertIsInstance(self.display.car_park, CarPark)

    # ... inside the TestDisplay class
    def test_update(self):
        self.display.update({"message": "Goodbye"})
        self.assertEqual(self.display.message, "Goodbye")

