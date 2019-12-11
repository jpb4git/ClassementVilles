import matplotlib.pyplot as plot
from apps.cities import tools

data = tools.readData()

sortedData = tools.sortData(data)

if __name__ == '__main__':

    print(sortedData.head(50))

    barData = tools.createGraph(sortedData)

