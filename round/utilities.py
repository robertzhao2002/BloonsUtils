class Cumulative_Round:
    def __init__(self, final_round, round_data):
        self.__final_round = final_round
        self.__round_data = round_data

    def total_damage(self):
        total_damage = 0
        for i in range(self.__final_round):
            total_damage+= self.__round_data[i]['RBE/Damage']

        return total_damage
    
    def total_money_from_pops(self):
        total_money = 0
        for i in range(self.__final_round):
            total_money+= self.__round_data[i]['Money from Bloons']

        return total_money

    def total_money_from_pops_and_income(self):
        total_money = self.total_money_from_pops() # Start with money earned from pops
        for i in range(self.__final_round):
            total_money+= self.__round_data[i]['Money from Income']
        return total_money

class Banana_Farm:
    pass