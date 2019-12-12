import pandas as pds

def read_highschools_csv_data(path):
    return pds.read_csv(path, low_memory=False, sep=";")

def filter_highschools(highschools):
    highschools_df = pds.DataFrame(highschools) 
    return highschools_df.filter(items=['Code commune', 'Taux Brut de Réussite Total séries'])
    
def reduce_highschools(highschools):
    return highschools.groupby(['Code commune']).mean()