from lotto.city import City
from lotto.bet import Bet
from lotto.numbersgenerator import NumbersGenerator


class Ticket:
    def __init__(self, city_number, bet_type, num_gen, amount_bet):
        self.city = City(city_number)
        self.bet_type = Bet(bet_type)
        self.generated_numbers = NumbersGenerator(num_gen)
        self.amount_bet = amount_bet

    """ this function shows the ticket to the user """
    def printTicket(self):
        print("+--------------+")
        print("|    TICKET    |")
        print("+--------------+")
        print("|    City: {}    ".format(self.city.name.upper()))
        print("|    Ticket Type: {}    ".format(self.bet_type.type.upper()))
        print("|    Amount Bet: {} €   ".format(self.amount_bet))
        # printing all generated numbers
        for number in self.generated_numbers.generated_numbers:
            print(" {} ".format(number), end="")
        print("\n")
