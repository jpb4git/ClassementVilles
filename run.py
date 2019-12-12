import matplotlib.pyplot as plot
from apps.cities import cities
from apps.highschools import highschools
import settings
import pandas as pds
from pandas import DataFrame

cities_data = cities.read_cities_csv_data(settings.cities_csv_path)
sorted_cities = cities.sort_cities_by_population(cities_data)

if __name__ == '__main__':

    bar_data = cities.create_graph(sorted_cities)

    highschools_data = highschools.read_highschools_csv_data(settings.highschools_csv_path)
    extracted_highschools = highschools.extract_highschools_columns(highschools_data)
    reduced_highschools = highschools.reduce_highschools(extracted_highschools)

    print(reduced_highschools)