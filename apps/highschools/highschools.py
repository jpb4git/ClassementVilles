import pandas as pds

def read_highschools_csv_data(path):
    return pds.read_csv(path, low_memory=False, sep=";")

def group_cities_districts(highschools):
    return highschools.groupby(highschools['Ville'].str.startswith("PARIS")).mean()

def extract_highschools_columns(highschools):
    highschools_df = pds.DataFrame(highschools) 
    return highschools_df.filter(items=['Code commune', 'Taux Brut de Réussite Total séries'])

def average_by_insee(highschools):
    return highschools.groupby(['Code commune']).mean()

def get_average(highschools):
    highschools_grouped_cities = group_cities_districts(highschools)
    highschools_extracted_columns = extract_highschools_columns(highschools_grouped_cities)
    return average_by_insee(highschools_extracted_columns)