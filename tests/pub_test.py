import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.pub1 = Pub("Bannermans", 200.00)
        self.drink1 = Drink("Tennents", 3.50, 5)
        self.customer = Customer("bob", 4.50, 22)
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till )
        self.assertEqual(200.00, self.pub1.till )

    def test_add_drink_menu(self):
        self.pub.add_drink(self.drink1)
        self.assertEquals(1, len(self.pub.menu))

    def test_find_drink_by_name(self):
        self.pub.add_drink(self.drink1)
        drink = self.pub.find_drink(self.drink1)
        self.assertEqual("Tennents", drink.name)

        
    def test_find_drink_by_name_2(self):
        drink = self.pub.find_drink(self.drink1)
        self.assertEqual(None, drink)

    def test_add_money_till(self):
        self.pub.add_money_till(self.drink1)
        self.assertEqual(103.50, self.pub.till)

    def test_check_age(self):
        age = self.pub.check_age(self.customer)
        self.assertEqual(True, age)

    def test_check_drunkenness(self):
        drunk = self.pub.check_drunk(self.customer)
        self.assertEquals(True, drunk)




