from lotto.city import City
from lotto.bet import Bet
from lotto.numbersgenerator import NumbersGenerator


class Extraction:
    def __init__(self):
        self.table = {}
        self.extraction()

    def extraction(self):
        for city in City.city_list:
            self.table[city] = NumbersGenerator(5)

    # this function will print all numbers (from self.table) for each city in city_list
    def printExtraction(self):
        for city in self.table.keys():
            print("{} - {}".format(city, self.table[city].generated_numbers))
