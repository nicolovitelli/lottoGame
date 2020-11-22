import argparse
from lotto.ticket import Ticket
from lotto.city import City


def main():
    num_gen = []
    type = []
    user_cities = []
    error_message = "Number not valid. You can only insert a number between {} and {}"
    city_list = ["Cagliari", "Firenze", "Genova", "Milano", "Napoli", "Palermo", "Roma", "Torino", "Venezia", "Tutte"]
    parser = argparse.ArgumentParser(description="Lotto Game")
    parser.add_argument("tickets", type=int, help="Amount of Ticket")
    args = parser.parse_args()
    ticket = args.tickets
    if 1 <= ticket <= 5:
        print("Here's the ticket's types:")
        print("1: Ambata")
        print("2: Ambo")
        print("3: Terna")
        print("4: Quaterna")
        print("5: Cinquina")
        i = 0
        while i != ticket:
            a = ["First", "Second", "Third", "Fourth", "Fifth"]
            t = int(input("Insert the type of the {} ticket: ".format(a[i])))
            if 1 <= t <= 5:
                type.append(t)
                n = int(input("Insert the amount of numbers to generate: "))
                num_gen.append(n)
                if 1 <= n <= 10:
                    c = input("Insert the city name or 'Tutte': ")
                    user_city = City(c, city_list, user_cities)
                    if user_city.pickCity():
                        user_ticket = Ticket(ticket, type, num_gen, user_cities)
                        print("Ticket correctly added.")
                        i = i + 1
                    else:
                        print("City non valid. Try again.")
                else:
                    print(error_message.format(1, 10))
                    return
            else:
                print(error_message.format(1, 5))
                return
        user_ticket = Ticket(ticket, type, num_gen, user_cities)
        user_ticket.printTicket()
    elif ticket == "0":
        print("Closing..")
        return
    else:
        print(error_message.format(1, 5))
        return


if __name__ == '__main__':
    main()
