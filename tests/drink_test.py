import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Tennents", 3.50, 5, 100)
        self.drink1 = Drink("Sex on the beach", 5.00, 10, 15)

    def test_drink_has_name(self):
        self.assertEquals("Tennents", self.drink.name)
    
    def test_drink_has_price(self):
        self.assertEquals(3.50, self.drink.price)

    def test_alcohol_level(self):
        self.assertEquals(5, self.drink.alcohol_level)
        self.assertEquals(10, self.drink1.alcohol_level)


    def test_drink_quanity(self):
        self.assertEqual(100, self.drink.quantity)
        self.assertEqual(15, self.drink1.quantity)









