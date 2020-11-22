class City:
    def __init__(self, city, cities_list, user_cities):
        self.city = city
        self.cities_list = cities_list
        self.user_cities = user_cities

    def pickCity(self):
        for element in range(len(self.cities_list)):
            if self.city == self.cities_list[element]:
                self.user_cities.append(self.city)
                return True
            elif self.city == self.cities_list[element].lower():
                self.user_cities.append(self.city)
                return True
            elif self.city == self.cities_list[element].upper():
                self.user_cities.append(self.city)
                return True
            else:
                pass

