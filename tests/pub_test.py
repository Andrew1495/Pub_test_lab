import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food
class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.pub1 = Pub("Bannermans", 200.00)
        self.drink1 = Drink("Tennents", 3.50, 5, 100)
        self.customer = Customer("bob", 4.50, 22)
        self.food = Food("kebab", 8.00, 10, 20)
        self.food1 = Food("burger", 7.00, 7, 15)


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

    def test_add_food_menu(self):
        self.pub.add_food(self.food)
        self.assertEquals(1, len(self.pub.food_menu))


    def test_find_food_by_name(self):
        self.pub.add_food(self.food)
        food = self.pub.find_food(self.food)
        self.assertEqual("kebab", food.name)


    def test_stock_value(self):
        self.pub.add_food(self.food)
        self.pub.add_drink(self.drink1)
        self.pub.stock_value = total_stock_value(self)
        self.assertEqual(510, self.pub.stock_value)

    



