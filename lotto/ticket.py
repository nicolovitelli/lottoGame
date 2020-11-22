import random


class Ticket:
    def __init__(self, amount, type, numbers, city):
        self.amount = amount
        self.type = type
        self.numbers = numbers
        self.city = city

    def ticketTypes(self):
        print("Here's the ticket's types:")
        print("1: Ambata")
        print("2: Ambo")
        print("3: Terna")
        print("4: Quaterna")
        print("5: Cinquina")

    def printTicket(self):
        a = ["FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH"]
        types = {1: "Ambata", 2: "Ambo", 3: "Terna", 4: "Quaterna", 5: "Cinquina"}
        i = 0
        x = 0
        print("+ --------------- +")
        print("+ Italian Lottery +")
        print("+ --------------- +")
        while i != self.amount:
            while x != len(self.type):
                while x != len(self.numbers):
                    while x != len(self.city):
                        print("+   {} TICKET  ".format(a[i]))
                        print("+ --------------- +")
                        print("+    Type:  {}  ".format(types[self.type[x]].upper()))
                        print("+    City:  {}  ".format(self.city[x]).upper())
                        ticket = Ticket(self.amount, self.type, self.numbers[x], self.city)
                        ticket.generateTicket(self.numbers)
                        print("\n+ --------------- +")
                        x = x + 1
                        i = i + 1

    def generateTicket(self, numbers):
        generated = []
        x = 0
        while x != self.numbers:
            generated.append(random.randint(1, 90))
            x = x + 1
        print("+", end="")
        print("    ",end="")
        for element in generated:
            print("{} ".format(element), end=" ")
