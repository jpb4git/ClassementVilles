import pandas as pds
from pandas import DataFrame
import settings


def readData():
    return pds.read_csv(settings.path, low_memory=False, header=None)

def sortData(data):
    return data.sort_values(by=15, ascending=False)

def createGraph(sortedData):
    barData = DataFrame(sortedData.head(25))
    return barData.plot(x=2, y=15, kind='bar')
