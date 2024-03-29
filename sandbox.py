thirdDownConversions = pd.read_csv('3rdDownConversions.csv')
redZoneConversions = pd.read_csv('RedZoneConversions.csv')
firstDowns = pd.read_csv('FirstDowns.csv')
scoringDefense = pd.read_csv('ScoringDefense.csv')
totalDefense = pd.read_csv('TotalDefense.csv')
totalOffense = pd.read_csv('TotalOffense.csv')
dfs = [redZoneConversions, firstDowns, scoringDefense, totalDefense, totalOffense]



def createDf():
    maindf = pd.DataFrame(thirdDownConversions)
    for df in dfs:
        maindf = pd.merge(maindf, df, on = 'Name')
    return maindf

print(createDf())

######## IDEA FOR STARTING FUNCTION #######

def startFootball():
    data = input('Enter the game data you want to compare: ')
    model = input("What model do you want to run? [Overall, One Team, Two Team Comparison]: ")
    if model == "Overall":
        sFoverallstats(data)
    elif model == "One Team":
        sFcompstats1(data)
    else:
        sFcompstats2(data)
    
# another idea for a starting function.
def cfbStatsTool():
    print("Welcome to the College Football Statistics tool.")
    print("You can run three statistical tests on CFB data from the 2018-2019 season.")
    print("overallstats() shows you the description of all teams performance.")
    print("compstats1() shows you one team compared to the performance of all teams.")
    print("compstats2() shows you two teams compared to each other and the performance of all other teams.")
    
cfbStatsTool()
    
    
    ###### EDITED THREE FUNCTIONS TO HAVE DATA AS AN INPUT #######
        
        # ANOHTER WAY TO DO IT WOULD BE THAT IT CREATES A NEW FILE?
        
        # OR PERHAPS IT HAS ALL THE DATA AND IS GROUPED BY TEAM? 
            # - THIS MIGHT HAVE TO BE IT SINCE I CAN'T FIGURE OUT HOW TO MAKE THE INPUT A DATA FRAME


def sFcompstats2(data):
    one = input('Enter the first team name: ')
    two = input('Enter the second team name: ')
    data_fil = data.drop([data.columns[0]], axis='columns')
    data_fil2 = data.drop([data.columns[0], data.columns[1], data.columns[2]],  axis='columns')
    d_one = data_fil[data_fil['Name']==one]
    d_two = data_fil[data_fil['Name']==two]
    d_desc = data_fil2.describe()
    return (d_one,d_two,d_desc)


def sFcompstats1(data):
    one = input('Enter a team name: ')
    data_fil = data.drop([data.columns[0]], axis='columns')
    data_fil2 = data.drop([data.columns[0], data.columns[1], data.columns[2]],  axis='columns')
    d_one = data_fil[data_fil['Name']==one]
    d_desc = data_fil2.describe()
    return(d_one,d_desc)


def sFoverallstats(data):
    data_fil2 = data.drop([data.columns[0], data.columns[1], data.columns[2]], axis='columns')
    d_desc = data_fil2.describe()
    return(d_desc)
    
    



################## THESE ARE THE GOOD ONES #######################

def compstats2(data):
    one = input('Enter the first team name: ')
    two = input('Enter the second team name: ')
    data_fil = data.drop([data.columns[0]], axis='columns')
    data_fil2 = data.drop([data.columns[0], data.columns[1], data.columns[2]],  axis='columns')
    d_one = data_fil[data_fil['Name']==one]
    d_two = data_fil[data_fil['Name']==two]
    d_desc = data_fil2.describe()
    return (d_one,d_two,d_desc)


def compstats1(data):
    one = input('Enter a team name: ')
    data_fil = data.drop([data.columns[0]], axis='columns')
    data_fil2 = data.drop([data.columns[0], data.columns[1], data.columns[2]],  axis='columns')
    d_one = data_fil[data_fil['Name']==one]
    d_desc = data_fil2.describe()
    return(d_one,d_desc)


def overallstats(data):
    data_fil2 = data.drop([data.columns[0], data.columns[1], data.columns[2]], axis='columns')
    d_desc = data_fil2.describe()
    return(d_desc)
    
###############################################    
    


######## UPDATED START FOOTBALL #########
def startFootball():
    model = input("What model do you want to run? [Overall, One Team, Two Team Comparison]: ")
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
    else:
        team1 = input("What is the first team you would like to compare? ")
        team2 = input("What is the second team you would like to compare? ")
        sFcompstats2(thirdDownConversions,team1,team2)
        sFcompstats2(firstDowns,team1,team2)
        sFcompstats2(redZoneConversions,team1,team2)
        sFcompstats2(scoringDefense,team1,team2)
        sFcompstats2(totalDefense,team1,team2)
        sFcompstats2(totalOffense,team1,team2)
        
        
######## UPDATED SF THREE FUNCTIONS ###############



def sFcompstats2(data,team1,team2):
    data_fil = data.drop([data.columns[0]], axis='columns')
    data_fil2 = data.drop([data.columns[0], data.columns[1], data.columns[2]],  axis='columns')
    d_one = data_fil[data_fil['Name']==team1]
    d_two = data_fil[data_fil['Name']==team2]
    d_desc = data_fil2.describe()
    return (d_one,d_two,d_desc)


def sFcompstats1(data,team1):
    data_fil = data.drop([data.columns[0]], axis='columns')
    data_fil2 = data.drop([data.columns[0], data.columns[1], data.columns[2]],  axis='columns')
    d_one = data_fil[data_fil['Name']==team1]
    d_desc = data_fil2.describe()
    return(d_one,d_desc)


def sFoverallstats(data):
    data_fil2 = data.drop([data.columns[0], data.columns[1], data.columns[2]], axis='columns')
    d_desc = data_fil2.describe()
    return(d_desc)
    
