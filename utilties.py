import pandas as pd

thirdDownConversions = pd.read_csv('Sample Data/3rdDownConversions.csv')
redZoneConversions = pd.read_csv('Sample Data/RedZoneConversions.csv')
firstDowns = pd.read_csv('Sample Data/FirstDowns.csv')
scoringDefense = pd.read_csv('Sample Data/ScoringDefense.csv')
totalDefense = pd.read_csv('Sample Data/TotalDefense.csv')
totalOffense = pd.read_csv('Sample Data/TotalOffense.csv')
dfs = [redZoneConversions, firstDowns, scoringDefense, totalDefense, totalOffense]



def createDf():
    maindf = pd.DataFrame(thirdDownConversions)
    for df in dfs:
        maindf = pd.merge(maindf, df, on = 'Name')
    return maindf

print(createDf())
