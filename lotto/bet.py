class Bet:

    def __init__(self, ticket_type_number):
        ticket_types = ["Ambata", "Ambo", "Terna", "Quaterna", "Cinquina"]
        self.user_ticket_type = ticket_types[ticket_type_number]

    # this static method permits the user to insert the bet type
    @staticmethod
    def betType():
        ticket_types = ["Ambata", "Ambo", "Terna", "Quaterna", "Cinquina"]
        Bet.printTicketTypes()
        ticket_type = input("Insert the Ticket type (number required): ")
        while True:
            # check if the number inserted by the user is valid or not
            if 1 <= int(ticket_type) <= len(ticket_types):
                return int(ticket_type)
            # if not, the user must reinsert a valid number
            else:
                ticket_type = input("Invalid Number. Please choose a number between 1 and 5: ")

    # this static method shows the user all ticket types
    @staticmethod
    def printTicketTypes():
        ticket_types = ["Ambata", "Ambo", "Terna", "Quaterna", "Cinquina"]
        print("\nHere's the Ticket Types:")
        for i in range(len(ticket_types)):
            print("{} - {}".format(i + 1, ticket_types[i]))
