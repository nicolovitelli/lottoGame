from lotto.city import City
from lotto.bet import Bet
import random


class Ticket:
    def __init__(self, city_number, bet_type, tickets_number):
        self.city = City(city_number)
        self.bet_type = Bet(bet_type)
        self.generated_numbers = []
        self.generateTicket(tickets_number)

    """ this function will generate the numbers from 1 to 90 and insert the results into the generated_numbers
    array """
    def generateTicket(self, tickets_number):
        while len(self.generated_numbers) < tickets_number:
            number = random.randint(1, 90)
            if number not in self.generated_numbers:
                self.generated_numbers.append(str(number))

    """ this function shows the ticket to the user """
    def printTicket(self):
        print("+--------------+")
        print("|    TICKET    |")
        print("+--------------+")
        print("|    City: {}    ".format(self.city.user_city.upper()))
        print("|    Ticket Type: {}    ".format(self.bet_type.user_ticket_type.upper()))
        # printing all generated numbers
        for number in self.generated_numbers:
            print("     {} ".format(number), end="")
        print("\n")
