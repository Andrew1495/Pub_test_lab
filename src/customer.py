class Customer:
    def __init__(self, input_name, input_wallet, input_age):
        self.name = input_name
        self.wallet = input_wallet
        self.age = input_age
        self.current_drink = []
        self.drunk = 0 


    def remove_money(self, drink):
        self.wallet -= drink.price
        return self.wallet


    def can_afford_drink(self, drink):
        if self.wallet >= drink.price:
            return True 
        else:
            return False
        
    def add_drink_customer(self, drink):
        self.current_drink.append(drink)

    
    def buy_drink(self,pub,drink):
        drink = pub.find_drink(drink)
        if  drink != None  and self.can_afford_drink(drink) == True:
            self.add_drink_customer(drink)
            self.remove_money(drink)
            pub.add_money_till(drink)

    def increase_drunk(self, drink):
        self.drunk += drink.alcohol_level
        
