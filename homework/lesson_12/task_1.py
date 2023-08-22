"""Creation of city with possibility to create and delete streets, houses, fill them with people"""
import random
from tabulate import tabulate


class House:
    def __init__(self, number: int):
        self.number = number
        self.population = random.randint(1, 100)

    def __repr__(self):
        return f'Number {self.number} ; Population: {self.population}'


class Street:
    def __init__(self, number: int):
        self.number = number
        self.houses = []

    def __repr__(self):
        return f'Number {self.number} ; Houses: {self.houses}'

    def add_house(self):
        """Create new house"""
        house_num = len(self.houses) + 1
        house = House(house_num)
        return self.houses.append(house)

    def del_house(self, house_num: int):
        """Delete the given house"""
        if 1 <= house_num <= len(self.houses):
            del self.houses[house_num-1]
        else:
            print("House doesn't exit.")


class City:
    def __init__(self):
        self.streets = []

    def __repr__(self):
        return f'Streets: {self.streets}'

    def fill_city(self, streets_amount: int):
        """Fill city with streets, houses and people"""
        for street_num in range(1, streets_amount+1):
            street = Street(street_num)
            house_num = random.randint(5, 20)
            for house in range(house_num):
                street.add_house()
            self.streets.append(street)

    def add_street(self):
        """Create new street"""
        street_num = len(self.streets) + 1
        street = Street(street_num)
        return self.streets.append(street)

    def del_street(self, street_num: int):
        """Delete the given street"""
        if 1 <= street_num <= len(self.streets):
            del self.streets[street_num-1]
        else:
            print("Street doesn't exit.")

    @property
    def population(self):
        """Get information about population"""
        population = sum(house.population for street in self.streets for house in street.houses)
        return f'Population: {population}'

    def print_table(self):
        """Print table with information about city"""
        table_data = []
        for street in self.streets:
            for house in street.houses:
                table_data.append([street.number, house.number, house.population])
        table_headers = ["Street", "Building", "Population"]
        print(tabulate(table_data, headers=table_headers))


# usage example
if __name__ == "__main__":
    city = City()
    city.fill_city(3)
    city.print_table()
    city.streets[2].add_house()
    city.print_table()
    city.del_street(1)
    city.print_table()
    print(city.population)
