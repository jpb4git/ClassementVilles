from apps.highschools import highschools
import settings
import pandas as pds 

def test_data_first_line():
    data = highschools.read_highschools_csv_data(settings.highschools_csv_path)
    assert (data['Etablissement'][0]) == "LYCEE PIERRE-GILLES DE GENNES"

def test_data_length():
    data = highschools.read_highschools_csv_data(settings.highschools_csv_path)
    assert len(data) == 16210

def test_reduced_data_length():
    data = highschools.read_highschools_csv_data(settings.highschools_csv_path)
    extracted_highschools = highschools.extract_highschools_columns(data)
    averages = highschools.average_by_insee(extracted_highschools)
    assert len(averages) == 1157

def test_one_line_per_insee():
    data = {'Code commune': ['99999','99999','99999'], 'réussite' : [50.0, 75.0, 100.0]}
    df = pds.DataFrame(data)
    print(df)
    averages = highschools.average_by_insee(df)
    print(averages)
    assert averages.iloc[0]['réussite'] == 75.0



