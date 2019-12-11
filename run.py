# import pandas as pd 
# import matplotlib.pyplot as plt
# import settings

def readData(path):
    return pd.read_csv(path, low_memory=False, header=None) 

if __name__ == "__main__":
    data = readData(settings.path)

    df = pd.DataFrame(data) 

    df.sort_values(15, axis = 0, ascending = False, 
                    inplace = True, na_position ='last')
    print(df.head(50))

    graphData = df.head(25)
    graphData.plot(x = 2 , y = 15 , kind = 'bar')

