class Bet:
    ticket_types = ["Ambata", "Ambo", "Terna", "Quaterna", "Cinquina"]
    def __init__(self, ticket_type_number):
        self.user_ticket_type = Bet.ticket_types[ticket_type_number]

    # this static method permits the user to insert the bet type
    @staticmethod
    def betType():
        Bet.printTicketTypes()
        ticket_type = input("Insert the Ticket type (number required): ")
        while True:
            # check if the number inserted by the user is valid or not
            if 1 <= int(ticket_type) <= len(Bet.ticket_types):
                return int(ticket_type)
            # if not, the user must reinsert a valid number
            else:
                ticket_type = input("Invalid Number. Please choose a number between 1 and 5: ")

    # this static method shows the user all ticket types
    @staticmethod
    def printTicketTypes():
        print("\nHere's the Ticket Types:")
        for i in range(len(Bet.ticket_types)):
            print("{} - {}".format(i + 1, Bet.ticket_types[i]))
