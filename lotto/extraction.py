from lotto.city import City
from lotto.bet import Bet
from lotto.numbersgenerator import NumbersGenerator


class Extraction:
    def __init__(self):
        self.numbers_extracted_each_city = {}
        self.extraction()

    def extraction(self):
        for city in City.city_list:
            self.numbers_extracted_each_city[city] = NumbersGenerator(5)

    # this function will print all numbers (from self.table) for each city in city_list
    def printExtraction(self):
        for city in self.numbers_extracted_each_city.keys():
            print("{} - {}".format(city, self.numbers_extracted_each_city[city].generated_numbers))

    def results(self, tickets):
        winning_ticket = False
        for ticket in tickets:
            if ticket.city.user_city.lower() == 'tutte':
                winning_combination = {}
                for city in self.numbers_extracted_each_city.keys():
                    winning_numbers_list = []
                    for number in ticket.generated_numbers.generated_numbers:
                        if number in self.numbers_extracted_each_city[city].generated_numbers:
                            winning_numbers_list.append(number)
                    winning_combination[city] = winning_numbers_list
            else:
                winning_combination  = {}
                winning_numbers_list = []
                for number in ticket.generated_numbers.generated_numbers:
                    if number in self.numbers_extracted_each_city[ticket.city.user_city].generated_numbers:
                        winning_numbers_list.append(number)
                winning_combination[ticket.city.user_city] = winning_numbers_list
            for city in winning_combination.keys():
                if len(winning_combination[city]) > Bet.ticket_types.index(ticket.bet_type.user_ticket_type):
                    print("-- RESULTS --")
                    print("You Win :)")
                    print("Your Winning Ticket: ")
                    ticket.printTicket()
                    print("Winning City: {}".format(city))
                    winning_ticket = True
        if not winning_ticket:
            print("-- RESULTS --")
            print("You Lose :(")
