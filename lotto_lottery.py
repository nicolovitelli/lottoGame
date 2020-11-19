import random
import argparse
from ticket import Ticket

def main():
    num_gen = []
    type = []
    city = []
    x = 0
    error_message = "Number not valid. You can only insert a number between {} and {}"
    city_list = ["Cagliari", "Firenze", "Genova", "Milano", "Napoli", "Palermo", "Roma", "Torino", "Venezia", "Tutte"]
    parser = argparse.ArgumentParser(description="Lotto Game")
    parser.add_argument("ticket", type=int, help="Amount of Ticket")
    args = parser.parse_args()
    ticket = args.bills
    while True:
        if ticket >= 1 and ticket <= 5:
            print("Here's the ticket's types:")
            print("1: Ambata")
            print("2: Ambo")
            print("3: Terna")
            print("4: Quaterna")
            print("5: Cinquina")
            i = 0

            while i != ticket:
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
                                user_ticket = Ticket(ticket, type, num_gen, city)
                                print("Bill correctly added.")
                                i = i + 1

                            elif c == city_list[element].lower():
                                city.append(c)
                                user_ticket = Ticket(ticket, type, num_gen, city)
                                print("Bill correctly added.")
                                i = i + 1

                            elif c == city_list[element].upper():
                                city.append(c)
                                user_ticket = Ticket(ticket, type, num_gen, city)
                                print("Bill correctly added.")
                                i = i + 1

                            else:
                                print(error_message.format(1, 10))

                        else:

                            print(error_message.format(1, 5))
            user_ticket = Ticket(ticket, type, num_gen, city)
            user_ticket.printTicket()

        elif ticket == 0:
            print("Closing..")

        else:
            print(error_message.format(1, 5))

if __name__ == '__main__':
    main()
