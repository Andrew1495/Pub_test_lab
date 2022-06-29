class Customer:
    def __init__(self, input_name, input_wallet, input_age):
        self.name = input_name
        self.wallet = input_wallet
        self.age = input_age
        self.current_drink = []
        self.drunk = 0 
        self.current_food = []


    def remove_money(self, item):
        self.wallet -= item.price
        return self.wallet


    def can_afford_drink(self, item):
        if self.wallet >= item.price:
            return True 
        else:
            return False
        
    def add_drink_customer(self, item):
        self.current_drink.append(item)

    
    def buy_drink(self,pub,drink):
        drink = pub.find_drink(drink)
        if  drink != None  and self.can_afford_drink(drink) == True and pub.check_drunk(self) == True:
            self.add_drink_customer(drink)
            self.remove_money(drink)
            pub.add_money_till(drink)
            self.increase_drunk(drink)
            

    def increase_drunk(self, drink):
        self.drunk += drink.alcohol_level


    def buy_food(self, pub, food):
        food = pub.find_food(food)
        if food != None and self.can_afford_drink(food) == True:
            self.add_food_customer(food)
            self.remove_money(food)
            pub.add_money_till(food)
            self.increase_rj_level



    def increase_rj_level(self, food):
        self.drunk -= food.rj_level

    def add_food_customer(self, food):
        self.current_food.append(food)


    

        

