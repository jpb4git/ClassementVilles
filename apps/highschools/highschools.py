import pandas as pds

def read_highschools_csv_data(path):
    return pds.read_csv(path, low_memory=False, sep=";")

def extract_highschools_columns(highschools):
    highschools_df = pds.DataFrame(highschools) 
    return highschools_df.filter(items=['Code commune', 'Taux Brut de Réussite Total séries'])
    
def average_by_insee(highschools):
    return highschools.groupby(['Code commune']).mean()