def StartFootball():
    import pandas as pd
    thirdDownConversions = pd.read_csv('Sample Data/3rdDownConversions.csv')
    redZoneConversions = pd.read_csv('Sample Data/RedZoneConversions.csv')
    firstDowns = pd.read_csv('Sample Data/FirstDowns.csv')
    scoringDefense = pd.read_csv('Sample Data/ScoringDefense.csv')
    totalDefense = pd.read_csv('Sample Data/TotalDefense.csv')
    totalOffense = pd.read_csv('Sample Data/TotalOffense.csv')
    dfs = [redZoneConversions, firstDowns, scoringDefense, totalDefense, totalOffense]
    model = input("What model do you want to run? [Overall, One Team, Two Teams]: ")
    if model == "Overall":
        sFoverallstats(thirdDownConversions)
        sFoverallstats(firstDowns)
        sFoverallstats(redZoneConversions)
        sFoverallstats(scoringDefense)
        sFoverallstats(totalDefense)
        sFoverallstats(totalOffense)
    elif model == "One Team":
        team1 = input("What team would you like to compare? ")
        sFcompstats1(thirdDownConversions,team1)
        sFcompstats1(firstDowns,team1)
        sFcompstats1(redZoneConversions,team1)
        sFcompstats1(scoringDefense,team1)
        sFcompstats1(totalDefense,team1)
        sFcompstats1(totalOffense,team1)
    elif model == "Two Teams":
        team1 = input("What is the first team you would like to compare? ")
        team2 = input("What is the second team you would like to compare? ")
        sFcompstats2(thirdDownConversions,team1,team2)
        sFcompstats2(firstDowns,team1,team2)
        sFcompstats2(redZoneConversions,team1,team2)
        sFcompstats2(scoringDefense,team1,team2)
        sFcompstats2(totalDefense,team1,team2)
        sFcompstats2(totalOffense,team1,team2)
    else:
        print("Invalid Input - Please start again")

def cfbStatsTool():
    print("Welcome to the College Football Statistics tool.")
    print("You can run three statistical tests on CFB data from the 2018-2019 season.")
    print("'Overall' shows you the description of all teams performance.")
    print("'One Team' shows you one team compared to the performance of all teams.")
    print("'Two Teams' shows you two teams compared to each other and the performance of all other teams.")
    StartFootball()
    
def sFcompstats2(data,team1,team2):
    data_fil = data.drop([data.columns[0]], axis='columns')
    data_fil2 = data.drop([data.columns[0], data.columns[1], data.columns[2]],  axis='columns')
    d_one = data_fil[data_fil['Name']==team1]
    d_two = data_fil[data_fil['Name']==team2]
    d_desc = data_fil2.describe()
    print (d_one,d_two,d_desc)
    return (d_one,d_two,d_desc)


def sFcompstats1(data,team1):
    data_fil = data.drop([data.columns[0]], axis='columns')
    data_fil2 = data.drop([data.columns[0], data.columns[1], data.columns[2]],  axis='columns')
    d_one = data_fil[data_fil['Name']==team1]
    d_desc = data_fil2.describe()
    print (d_one,d_desc)
    return(d_one,d_desc)


def sFoverallstats(data):
    data_fil2 = data.drop([data.columns[0], data.columns[1], data.columns[2]], axis='columns')
    d_desc = data_fil2.describe()
    print(d_desc)
    return(d_desc)