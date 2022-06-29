class Pub:
    

    def __init__(self, input_name, input_till):
        self.name = input_name
        self.till = input_till
        self.menu = []
        self.food_menu = []
        self.stock_value = 0 


    def add_drink(self, drink):
        self.menu.append(drink)

    def find_drink(self, drink):
        for item in self.menu:
            if item.name == drink.name:
                return item

    def add_money_till(self, drink):
        self.till += drink.price

    def check_age(self, customer):
        if customer.age >= 18:
            return True
        else: 
            False 

    def check_drunk(self, customer):
        if customer.drunk >= 30:
            return False
        else: 
            return True 

    def add_food(self, food):
        self.food_menu.append(food)

    def find_food(self, food):
        for item in self.food_menu:
            if item.name == food.name:
                return item

    def total_stock_value(self):
        total = 0
        for drinks in self.menu: 
            total += drinks.price * drinks.quantity
        for food in self.menu: 
            total += food.price * food.quantity
        
        




        




    

    