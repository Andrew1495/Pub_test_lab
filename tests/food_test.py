from src.food import Food
import unittest

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("kebab", 8.00, 10, 20)
        self.food1 = Food("burger", 7.00, 7, 15)

    
    def test_food_has_name(self):
        self.assertEqual("kebab", self.food.name)
        self.assertEqual("burger", self.food1.name)

    def test_food_price(self):
        self.assertEqual(8.00, self.food.price)
        self.assertEqual(7.00, self.food1.price)

    def test_food_rj_level(self):
        self.assertEqual(10, self.food.rj_level)
        self.assertEqual(7, self.food1.rj_level)

    def test_food_quantity(self):
        self.assertEqual(20, self.food.quantity)
        self.assertEqual(15, self.food1.quantity)

    





    