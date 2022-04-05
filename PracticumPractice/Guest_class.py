class Guest:

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.stamina = 0
        self.hunger = 0
        self.money_spent = 0.0

    def get_name(self):
        return self.name

    def get_money(self):
        return self.money

    def get_stamina(self):
        return self.stamina

    def get_hunger(self):
        return self.hunger

    def get_money_spent(self):
        return self.money_spent

    def set_name(self, name):
        self.name = name

    def set_money(self, money):
        self.money = money

    def set_stamina(self, stamina):
        self.stamina = stamina

    def set_hunger(self, hunger):
        self.hunger = hunger

    # COMPLETE set_money_spent() method in the space below

    def set_money_spent(self):

        percent_spent = (self.stamina + (self.hunger*2))/30
        self.money_spent = self.money * percent_spent
        return self.money_spent
