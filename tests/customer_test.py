import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("bob", 4.50, 22)
        self.customer1 = Customer("Frank", 20.00 , 34)
        self.drink = Drink("Tennents", 3.50, 5, 100)
        self.drink1 = Drink("Carlsberg", 20, 4 , 50)
        self.pub =  Pub("The Prancing Pony", 100)
        self.food = Food("kebab", 8.00, 10, 20)
        self.food1 = Food("burger", 7.00, 7, 15)
        
        

    def test_cusotmer_has_name(self):
        self.assertEqual("bob", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(4.50, self.customer.wallet)

    def test_customer_remove_money(self):
        wallet = self.customer.remove_money(self.drink)
        self.assertEqual(1.00, wallet)

    def test_customer_has_drink(self):
        self.customer.add_drink_customer(self.drink)
        self.assertEqual(1, len(self.customer.current_drink))

    def test_can_afford_drink(self):
        can_afford = self.customer.can_afford_drink(self.drink)
        self.assertEquals(True, can_afford)

    def test_cant_afford_drink(self):
        can_afford = self.customer.can_afford_drink(self.drink1)
        self.assertEquals(False, can_afford)

    def test_buy_drink(self):
        self.pub.add_drink(self.drink)
        drink = self.pub.find_drink(self.drink)
        self.customer.buy_drink(self.pub,drink)
        self.assertEqual(1.00, self.customer.wallet)
        self.assertEqual(103.50, self.pub.till)
        self.assertEqual(1, len(self.customer.current_drink))

    def test_customer_drunk(self):
        self.assertEquals(0, self.customer.drunk)

    def test_customer_drunk_increase(self):
        self.customer.increase_drunk(self.drink)
        self.assertEqual(5, self.customer.drunk)


    def test_buy_food(self):
        self.pub.add_food(self.food)
        food = self.pub.find_food(self.food)
        self.customer1.buy_food(self.pub, food)
        self.assertEqual(12.00, self.customer1.wallet)
        self.assertEqual(108.00, self.pub.till)
        self.assertEqual(1, len(self.customer1.current_food))

            
