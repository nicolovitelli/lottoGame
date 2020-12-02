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
                win_dict = {}
                for city in self.numbers_extracted_each_city.keys():
                    win_list = []
                    for number in ticket.generated_numbers.generated_numbers:
                        if number in self.numbers_extracted_each_city[city].generated_numbers:
                            win_list.append(number)
                    win_dict[city] = win_list
            else:
                win_dict = {}
                win_list = []
                for number in ticket.generated_numbers.generated_numbers:
                    if number in self.numbers_extracted_each_citye[ticket.city.user_city].generated_numbers:
                        win_list.append(number)
                win_dict[ticket.city.user_city] = win_list
            for city in win_dict.keys():
                if len(win_dict[city]) > Bet.ticket_types.index(ticket.bet_type.user_ticket_type):
                    print("-- RESULTS --")
                    print("You Win :)")
                    print("Your Winning Ticket: ")
                    ticket.printTicket()
                    print("Winning City: {}".format(city))
                    winning_ticket = True
        if not winning_ticket:
            print("-- RESULTS --")
            print("You Lose :(")
