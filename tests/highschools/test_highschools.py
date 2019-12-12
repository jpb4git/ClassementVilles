from apps.highschools import highschools
import settings

def test_data_first_line():
    data = highschools.read_highschools_csv_data(settings.highschools_csv_path)
    assert (data['Etablissement'][0]) == "LYCEE PIERRE-GILLES DE GENNES"

def test_data_length():
    data = highschools.read_highschools_csv_data(settings.highschools_csv_path)
    assert len(data) == 16210

def test_reduced_data_length():
    data = highschools.read_highschools_csv_data(settings.highschools_csv_path)
    filtered_highschools = highschools.filter_highschools(data)
    reduced_highschools = highschools.reduce_highschools(filtered_highschools)
    assert len(reduced_highschools) == 1157



