import random

class Bill:
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
class Wheel:
    def __init__(self, numbers):
        self.numbers = numbers

    def randomWheel(self):
        generated = []
        x = 0
        while x != self.numbers:
            generated.append(random.randint(1, 90))
            x = x + 1
            print("Numbers Generated:")
            for element in generated:
                print("{}".format(element))

def main():
    num_gen = []
    type = []
    city = []
    x = 0
    city_list = ["Cagliari", "Firenze", "Genova", "Milano", "Napoli", "Palermo", "Roma", "Torino", "Venezia", "Tutte"]
    while True:
        bills = int(input("How many bills? (press 0 to Exit): "))
        error_message = "Number not valid. You can only insert a number between {} and {}"
        if bills >= 1 and bills <= 5:
            print("Here's the bill's types:")
            print("1: Ambata")
            print("2: Ambo")
            print("3: Terna")
            print("4: Quaterna")
            print("5: Cinquina")
            i = 0
            while i != bills:
                a = ["First", "Second", "Third", "Fourth", "Fifth"]
                t = int(input("Insert the type of the {} bill: ".format(a[i])))
                if t >= 1 and t <= 5:
                    type.append(t)
                    n = int(input("Insert the amount of numbers to generate: "))
                    num_gen.append(n)
                    if n >= 1 and n <= 10:
                        c = input("Insert the city name or 'Tutte': ")
                        for element in range(len(city_list)):
                            if c == city_list[element]:
                                city.append(c)
                                bill = Bill(bills, type, num_gen, city)
                                print("Bill correctly added.")
                                i = i + 1
                            elif c == city_list[element].lower():
                                city.append(c)
                                bill = Bill(bills, type, num_gen, city)
                                print("Bill correctly added.")
                                i = i + 1
                            elif c == city_list[element].upper():
                                city.append(c)
                                bill = Bill(bills, type, num_gen, city)
                                print("Bill correctly added.")
                                i = i + 1
                            else:
                                print(error_message.format(1, 10))
                        else:
                            print(error_message.format(1, 5))
            bill = Bill(bills, type, num_gen, city)
            bill.printBill()
        elif bills == 0:
            print("Closing..")
        else:
            print(error_message.format(1, 5))

if __name__ == '__main__':
    main()