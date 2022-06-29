class Pub:
    

    def __init__(self, input_name, input_till):
        self.name = input_name
        self.till = input_till
        self.menu = []


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

        




    

    