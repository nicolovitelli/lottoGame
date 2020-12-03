import argparse
from lotto.lotto import Lotto
from lotto.extraction import Extraction

""" once the user launched the program by inserting the amount of tickets, it checks if the numbers is between
1 and 5, so it will convert the value inserted by the user to a int value. Then, the program creates a Lotto object from
the Lotto class and will print the Tickets"""


def main():
    parser = argparse.ArgumentParser(description="Lotto Game")
    parser.add_argument("-n", type=int, help="Amount of Tickets")
    args = parser.parse_args()
    tickets_amount = args.n
    if 1 <= tickets_amount <= 5:
        tickets_amount = int(tickets_amount)
    # if the user inserts 0, the program closes
    elif tickets_amount == 0:
        print("Closing..")
        quit()
    else:
        tickets_amount = input("Number non valid. Please enter a number between 1 and 5. \n -> ")
    lotto = Lotto(tickets_amount)
    for ticket in lotto.tickets:
        ticket.printTicket()
    print("-- EXTRACTION --")
    extraction = Extraction()
    extraction.printExtraction()
    extraction.results(lotto.tickets)


if __name__ == '__main__':
    main()
