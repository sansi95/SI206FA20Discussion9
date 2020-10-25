import requests
import json
import unittest

def get_data(country_code, year):
    """
    This function takes a country code (e.g. USA, BRA) and year (e.g. 2004).
    Call the World Bank API to get population data searched by country and year.
    Return the data from API after converting to a python list
    that has population related information.
    Once you receive data from the API, paste the data to
    JSON Online Editor and look at the contents.

    Things that will help you create the request url:
    1. What is the base URL of World Bank API?
    2. What is the code for population indicator - http://datatopics.worldbank.org/world-development-indicators/themes/people.html
    3. How should the parameters about population, country, and year be combined with the base URL?
    """
    pass

def population_year(country_code, year):
    """
    This function receives two parameters. One is a country code and the other is a year.
    Call get_data and analyze the returned list.
    This function returns the population of the country.
    """
    pass

class TestDiscussion11(unittest.TestCase):
    def test_check_data(self):
        data1 = get_data('BRA', 2000)
        self.assertEqual(type(data1), type([]))
        self.assertEqual(data1[0]['page'], 1)
        self.assertEqual(data1[1][0]['countryiso3code'], "BRA")

    def test_population_year(self):
        self.assertEqual(type(population_year('CAN', 1998)), type(1))
        self.assertEqual(population_year('USA', 2005), 295516599)
        self.assertEqual(population_year('CAN', 2008), 33247118)


def main():
    # CO2 emission in the US in 2014 (tons per capita)
    print("-----Population-----")
    country = "JPN"
    year = "2014"
    value1 = population_year(country, year)
    print("The population in {} in {} is {}".format(country, year, value1))

    print("-----Unittest-------")
    unittest.main(verbosity=2)
    print("------------")

if __name__ == "__main__":
    main()
