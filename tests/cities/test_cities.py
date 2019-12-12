from apps.cities import cities
import settings

def testDataFirstLine():
    data = cities.read_cities_csv_data(settings.cities_csv_path)
    assert (data.iloc[0][3]) == "OZAN"

def testDataLength():
    data = cities.read_cities_csv_data(settings.cities_csv_path)
    assert len(data) == 36700

def testSorting():
    data = cities.read_cities_csv_data(settings.cities_csv_path)
    sorted_cities = cities.sort_cities_by_population(data)
    assert (sorted_cities.iloc[0][3]) == "PARIS"

