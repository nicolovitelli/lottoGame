from lotto.bet import Bet
from lotto.city import City
from lotto.ticket import Ticket


class Lotto:
    def __init__(self, tickets_amount):
        self.tickets = []
        self.user_Ticket(tickets_amount)

    """ this function generates the ticket. First of all, recall the chooseCity() function from the Class City,
    (it asks the user the City number), then, asks the user the Bet Type (Ambata, Quaterna, ecc.) and how many
    numbers the user wants to generate (1 to 10, a While/If cycle will control that). In the end, the tickets generated
    will be added to the tickets array."""
    def user_Ticket(self, tickets_amount):
        ticket_number = ["First", "Second", "Third", "Fourth", "Fifth"]
        for x in range(tickets_amount):
            print("   -- {} Ticket --  ".format(ticket_number[x]))
            city_number = City.chooseCity()
            bet_type = Bet.betType()
            num_gen = input("Insert how many numbers to generate: ")
            while True:
                if int(bet_type) <= int(num_gen) <= 10:
                    num_gen = int(num_gen)
                    print()
                    break
                else:
                    num_gen = input("Invalid Number. Please choose a number between {} and 10: ".format(bet_type))
            self.tickets.append(Ticket(city_number, bet_type, num_gen))
