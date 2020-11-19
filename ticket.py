class Ticket:
    def __init__(self, amount, type, numbers, city):
        self.amount = amount
        self.type = type
        self.numbers = numbers
        self.city = city

    def printBill(self):
        print("Number of Bills: {}".format(self.amount))
        a = ["FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH"]
        types = {1: "Ambata", 2: "Ambo", 3: "Terna", 4: "Quaterna", 5: "Cinquina"}
        i = 0
        x = 0

        while i != self.amount:
            while x != len(self.type):
                while x != len(self.numbers):
                    while x != len(self.city):
                        print("----------------")
                        print("{} BILL".format(a[i]))
                        print("Type: {}".format(types[self.type[x]]))
                        print("Numbers to generate: {}".format(self.numbers[x]))
                        wheel = Wheel(self.numbers[x])
                        wheel.randomWheel()
                        print("City: {}".format(self.city[x]))
                        x = x + 1
                        i = i + 1