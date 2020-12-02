class City:
    city_list = ["Bari", "Cagliari", "Firenze", "Genova", "Milano", "Napoli", "Palermo", "Roma", "Torino",
                 "Venezia", "Tutte"]
    def __init__(self, city_number):
        self.user_city = City.city_list[city_number - 1]

    # this static method permits the user to choose a city by inserting its number
    @staticmethod
    def chooseCity():
        City.printCities()
        city_number = input("Insert the City (number required):  ")
        while True:
            # check if the number inserted by the user is valid
            if 1 <= int(city_number) <= len(City.city_list):
                return int(city_number)
            # if not, the user needs to reinsert the number
            else:
                city_number = input("Invalid Number. Please choose a Number between 1 and 11: ")

    # this static method shows the user all cities
    @staticmethod
    def printCities():
        # printing all elements in city_list
        for i in range(len(City.city_list)):
            print("{} - {}".format(i + 1, City.city_list[i]))
