from apps.cities import tools

def testDataFirstLine():
    data = tools.readData()
    assert (data.iloc[0][3]) == "OZAN"

def testDataLength():
    data = tools.readData()
    assert len(data) == 36700

def testSorting():
    data = tools.readData()
    sortedData = tools.sortData(data)
    assert (sortedData.iloc[0][3]) == "PARIS"