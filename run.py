import matplotlib.pyplot as plot
from apps.cities import cities
from apps.highschools import highschools
import settings
import pandas as pds
from pandas import DataFrame

if __name__ == '__main__':

    cities_data = cities.read_cities_csv_data(settings.cities_csv_path)
    
    sorted_cities = cities.sort_cities_by_population(cities_data)

    bar_data = cities.create_graph(sorted_cities)

    get_average(highschools.read_highschools_csv_data(settings.highschools_csv_path))

    print(reduced_highschools)