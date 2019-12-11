from run import readData
# import settings

# data = readData(settings.path)
# print (len(data))

def testDataFirstLine():
    assert (data.head(1)[3][0]) == "OZAN"

def testDataLength():
    assert len(data) == 36700