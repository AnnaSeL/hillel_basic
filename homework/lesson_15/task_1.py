"""Program returns data on the requested airport"""
import csv
import argparse
import re

"""Classes for the exceptions"""
class AirportNotFoundError(Exception):
    def __init__(self, message, iata_code):
        super().__init__(message, iata_code)
        self.iata_code = iata_code


class CountryNotFoundError(Exception):
    def __init__(self, message, country):
        super().__init__(message, country)
        self.country = country


class IATACodeError(Exception):
    def __init__(self, message, iata_code=None):
        super().__init__(message, iata_code)
        self.iata_code = iata_code


class MultipleOptionsError(Exception):
    def __init__(self, message):
        super().__init__(message)


class NoOptionsFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)


"""Functions for getting data based on the requested argument"""
def search_airport_by_iata(iata_code, airports):
    for airport in airports:
        if airport['iata_code'] == iata_code:
            return airport
    raise AirportNotFoundError('Airport not found', iata_code)


def search_airports_by_country(country, airports):
    found_airports = []
    for airport in airports:
        if airport['iso_country'] == country:
            found_airports.append(airport)
    if not found_airports:
        raise CountryNotFoundError('Country not found', country)
    return found_airports


def search_airports_by_name(name, airports):
    found_airports = []
    pattern = re.compile(fr'\b\w*{name}\w*\b', re.I)
    for airport in airports:
            if pattern.search(airport['name']):
                found_airports.append(airport)
    if not found_airports:
        raise AirportNotFoundError('Airport not found', name)
    return found_airports

"""Imports airport data from the file and calls the function based on the request"""
def get_airport_data():
    parser = argparse.ArgumentParser(description="Airport Data Search")
    parser.add_argument("--iata_code", help="Search by IATA code (3 uppercase letters)")
    parser.add_argument("--country", help="Search by country")
    parser.add_argument("--name", help="Search by airport name (partial match included)")

    args = parser.parse_args()

    with open('airport-codes_csv.csv', mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        airports = list(csv_reader)

    try:
        required_args = [args.iata_code, args.country, args.name]
        if sum(1 for arg in required_args if arg) > 1:
            raise MultipleOptionsError('Multiple search options provided')
        elif args.iata_code:
            if len(args.iata_code) != 3 or not args.iata_code.isupper():
                raise IATACodeError('Invalid IATA code format', args.iata_code)
            result = search_airport_by_iata(args.iata_code, airports)
            print(result)
        elif args.country:
            result = search_airports_by_country(args.country, airports)
            for airport in result:
                print(airport)
        elif args.name:
            result = search_airports_by_name(args.name, airports)
            for airport in result:
                print(airport)
        else:
            raise NoOptionsFoundError('No search criteria provided')
    except (AirportNotFoundError, CountryNotFoundError, IATACodeError, MultipleOptionsError, NoOptionsFoundError) as e:
        print(e)


if __name__ == "__main__":
    get_airport_data()

