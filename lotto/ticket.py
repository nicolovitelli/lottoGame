from lotto.city import City
from lotto.bet import Bet
from lotto.numbersgenerator import NumbersGenerator


class Ticket:
    def __init__(self, city_number, bet_type, num_gen):
        self.city = City(city_number)
        self.bet_type = Bet(bet_type)
        self.generated_numbers = NumbersGenerator(num_gen)

    """ this function shows the ticket to the user """
    def printTicket(self):
        print("+--------------+")
        print("|    TICKET    |")
        print("+--------------+")
        print("|    City: {}    ".format(self.city.user_city.upper()))
        print("|    Ticket Type: {}    ".format(self.bet_type.user_ticket_type.upper()))
        # printing all generated numbers
        for number in self.generated_numbers.generated_numbers:
            print("     {} ".format(number), end="")
        print("\n")
