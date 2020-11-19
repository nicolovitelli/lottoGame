from lotto.city import City
import random

class Ticket:
    def __init__(self, amount, type, numbers, city):
        self.amount = amount
        self.type = type
        self.numbers = numbers
        self.city = city

    def printTicket(self):
        print("Number of Tickets: {}".format(self.amount))
        a = ["FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH"]
        types = {1: "Ambata", 2: "Ambo", 3: "Terna", 4: "Quaterna", 5: "Cinquina"}
        i = 0
        x = 0
        while i != self.amount:
            while x != len(self.type):
                while x != len(self.numbers):
                    while x != len(self.city):
                        print("{} TICKET".format(a[i]))
                        print("Type: {}".format(types[self.type[x]]))
                        print("Numbers to generate: {}".format(self.numbers[x]))
                        ticket = Ticket(self.amount, self.type, self.numbers[x], self.city)
                        ticket.generateTicket(self.numbers)
                        print("City: {}".format(self.city[x]))
                        print("-----------------")
                        x = x + 1
                        i = i + 1

    def generateTicket(self, numbers):
        generated = []
        x = 0
        print("Numbers Generated:")
        while x != self.numbers:
            generated.append(random.randint(1, 90))
            x = x + 1
        for element in generated:
            print("{}".format(element))
