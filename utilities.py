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
    


