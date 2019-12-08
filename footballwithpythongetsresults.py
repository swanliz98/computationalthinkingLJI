#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 10:56:38 2019

@author: swanliz98
"""

##########
tdc = thirdDownConversions.drop([thirdDownConversions.columns[0], thirdDownConversions.columns[1]], axis='columns')
fstd = firstDowns.drop([firstDowns.columns[0], firstDowns.columns[1]], axis='columns')
rzc = redZoneConversions.drop([redZoneConversions.columns[0], redZoneConversions.columns[1]], axis='columns')
scod = scoringDefense.drop([scoringDefense.columns[0], scoringDefense.columns[1]], axis='columns')
totd = totalDefense.drop([totalDefense.columns[0], totalDefense.columns[1]], axis='columns')
toto = totalOffense.drop([totalOffense.columns[0], totalOffense.columns[1]], axis='columns')
############




import pandas as pd
import matplotlib.pyplot as plt


#read the csv file to create a dataframe
#third_Down_Conversions = pd.read_csv('national_team-2019-3rdDownConversions.csv')

variable_names = []
file_names = ['national_team-2019-3rdDownConversions.csv','national_team-2019-4thDownConversions.csv','national_team-2019-FieldGoals.csv','national_team-2019-FirstDowns.csv','national_team-2019-FumblesForced.csv','national_team-2019-FumblesLost.csv','national_team-2019-FumblesRecovered.csv','national_team-2019-Interceptions.csv','national_team-2019-KickoffReturns.csv','national_team-2019-Kickoffs.csv','national_team-2019-KicksPuntsBlocked.csv','national_team-2019-LongKickoffReturnPlays.csv','national_team-2019-LongPassingPlays.csv','national_team-2019-LongPuntReturnPlays.csv','national_team-2019-LongRushingPlays.csv','national_team-2019-LongScrimmagePlays.csv','national_team-2019-Opponent3rdDownConversions.csv','national_team-2019-Opponent4thDownConversions.csv','national_team-2019-OpponentFieldGoals.csv','national_team-2019-OpponentFirstDowns.csv','national_team-2019-OpponentKickoffReturns.csv','national_team-2019-OpponentKickoffs.csv','national_team-2019-OpponentLongKickoffReturnPlays.csv','national_team-2019-OpponentLongPassingPlays.csv','national_team-2019-OpponentLongPuntReturnPlays.csv','national_team-2019-OpponentLongRushingPlays.csv','national_team-2019-OpponentLongScrimmagePlays.csv','national_team-2019-OpponentPATKicking.csv','national_team-2019-OpponentPenalties.csv','national_team-2019-OpponentPunting.csv','national_team-2019-OpponentPuntReturns.csv','national_team-2019-OpponentRedZoneConversions.csv','national_team-2019-PassesDefended.csv','national_team-2019-PassingDefense.csv','national_team-2019-PassingOffense.csv','national_team-2019-PATKicking.csv','national_team-2019-Penalties.csv','national_team-2019-Punting.csv','national_team-2019-PuntReturns.csv','national_team-2019-RedZoneConversions.csv','national_team-2019-RushingDefense.csv','national_team-2019-RushingOffense.csv','national_team-2019-Sacks.csv','national_team-2019-SacksAllowed.csv','national_team-2019-ScoringDefense.csv','national_team-2019-ScoringOffense.csv','national_team-2019-TacklesForLoss.csv','national_team-2019-TacklesForLossAllowed.csv','national_team-2019-TimeOfPossession.csv','national_team-2019-TotalDefense.csv','national_team-2019-TotalOffense.csv','national_team-2019-TurnoverMargin.csv']

for i in file_names:
    variable_names.append(i[19:-4])

  
counter = 0
while counter < 52:
    i = counter
    print(variable_names[i] = pd.read_csv(file_names[i]))    
    counter +=1


newlittle_list = []
little_list = ['national_team-2019-3rdDownConversions.csv','national_team-2019-4thDownConversions.csv']
for i in little_list:
    newlittle_list.append(i[19:-4])
#dfc = pd.read_csv('titanic.csv')


for i in variable_names:
    print(f"{i} = pd.read_csv(")

liz = pd.read_csv('national_team-2019-3rdDownConversions.csv')




# IS THERE A BETTER WAY TO LOAD THE FILES IF I WANT THE NAMES OF THE VARIABLES HOLDING THE
# DATA TO MATCH THE END OF THE STRING OF THE FILE NAME? 



thirdDownConversions = pd.read_csv('national_team-2019-3rdDownConversions.csv')
fourthDownConversions = pd.read_csv('national_team-2019-4thDownConversions.csv')
fieldGoals = pd.read_csv('national_team-2019-FieldGoals.csv')
firstDowns = pd.read_csv('national_team-2019-FirstDowns.csv')
fumblesForced = pd.read_csv('national_team-2019-FumblesForced.csv')
fumblesLost = pd.read_csv('national_team-2019-FumblesLost.csv')
fumblesRecovered = pd.read_csv('national_team-2019-FumblesRecovered.csv')
interceptions = pd.read_csv('national_team-2019-Interceptions.csv')
kickoffReturns = pd.read_csv('national_team-2019-KickoffReturns.csv')
kickoffs = pd.read_csv('national_team-2019-Kickoffs.csv')
kicksPuntsBlocked = pd.read_csv('national_team-2019-KicksPuntsBlocked.csv')
longKickoffReturnPlays = pd.read_csv('national_team-2019-LongKickoffReturnPlays.csv')
longPassingPlays = pd.read_csv('national_team-2019-LongPassingPlays.csv')
longPuntReturnPlays = pd.read_csv('national_team-2019-LongPuntReturnPlays.csv')
longRushingPlays = pd.read_csv('national_team-2019-LongRushingPlays.csv')
longScrimmagePlays = pd.read_csv('national_team-2019-LongScrimmagePlays.csv')
opponent3rdDownConversions = pd.read_csv('national_team-2019-Opponent3rdDownConversions.csv')
opponent4thDownConversions = pd.read_csv('national_team-2019-Opponent4thDownConversions.csv')
opponentFieldGoals = pd.read_csv('national_team-2019-OpponentFieldGoals.csv')
opponentFirstDowns = pd.read_csv('national_team-2019-OpponentFirstDowns.csv')
opponentKickoffReturns = pd.read_csv('national_team-2019-OpponentKickoffReturns.csv')
opponentKickoffs = pd.read_csv('national_team-2019-OpponentKickoffs.csv')
opponentLongKickoffReturnPlays = pd.read_csv('national_team-2019-OpponentLongKickoffReturnPlays.csv')
opponentLongPassingPlays = pd.read_csv('national_team-2019-OpponentLongPassingPlays.csv')
opponentLongPuntReturnPlays = pd.read_csv('national_team-2019-OpponentLongPuntReturnPlays.csv')
opponentLongRushingPlays = pd.read_csv('national_team-2019-OpponentLongRushingPlays.csv')
opponentLongScrimmagePlays = pd.read_csv('national_team-2019-OpponentLongScrimmagePlays.csv')
opponentPATKicking = pd.read_csv('national_team-2019-OpponentPATKicking.csv')
opponentPenalties = pd.read_csv('national_team-2019-OpponentPenalties.csv')
opponentPunting = pd.read_csv('national_team-2019-OpponentPunting.csv')
opponentPuntReturns = pd.read_csv('national_team-2019-OpponentPuntReturns.csv')
opponentRedZoneConversions = pd.read_csv('national_team-2019-OpponentRedZoneConversions.csv')
passesDefended = pd.read_csv('national_team-2019-PassesDefended.csv')
passingDefense = pd.read_csv('national_team-2019-PassingDefense.csv')
passingOffense = pd.read_csv('national_team-2019-PassingOffense.csv')
pATKicking = pd.read_csv('national_team-2019-PATKicking.csv')
penalties = pd.read_csv('national_team-2019-Penalties.csv')
punting = pd.read_csv('national_team-2019-Punting.csv')
puntReturns = pd.read_csv('national_team-2019-PuntReturns.csv')
redZoneConversions = pd.read_csv('national_team-2019-RedZoneConversions.csv')
rushingDefense = pd.read_csv('national_team-2019-RushingDefense.csv')
rushingOffense = pd.read_csv('national_team-2019-RushingOffense.csv')
sacks = pd.read_csv('national_team-2019-Sacks.csv')
sacksAllowed = pd.read_csv('national_team-2019-SacksAllowed.csv')
scoringDefense = pd.read_csv('national_team-2019-ScoringDefense.csv')
scoringOffense = pd.read_csv('national_team-2019-ScoringOffense.csv')
tacklesForLoss = pd.read_csv('national_team-2019-TacklesForLoss.csv')
tacklesForLossAllowed = pd.read_csv('national_team-2019-TacklesForLossAllowed.csv')
timeOfPossession = pd.read_csv('national_team-2019-TimeOfPossession.csv')
totalDefense = pd.read_csv('national_team-2019-TotalDefense.csv')
totalOffense = pd.read_csv('national_team-2019-TotalOffense.csv')
turnoverMargin = pd.read_csv('national_team-2019-TurnoverMargin.csv')



####### FILE NAMES #######

'national_team-2019-FieldGoals.csv'
'national_team-2019-FirstDowns.csv'
'national_team-2019-FumblesForced.csv'
'national_team-2019-FumblesLost.csv'
'national_team-2019-FumblesRecovered.csv'
'national_team-2019-Interceptions.csv'
'national_team-2019-KickoffReturns.csv'
'national_team-2019-Kickoffs.csv'
'national_team-2019-KicksPuntsBlocked.csv'
'national_team-2019-LongKickoffReturnPlays.csv'
'national_team-2019-LongPassingPlays.csv'
'national_team-2019-LongPuntReturnPlays.csv'
'national_team-2019-LongRushingPlays.csv'
'national_team-2019-LongScrimmagePlays.csv'
'national_team-2019-Opponent3rdDownConversions.csv'
'national_team-2019-Opponent4thDownConversions.csv'
'national_team-2019-OpponentFieldGoals.csv'
'national_team-2019-OpponentFirstDowns.csv'
'national_team-2019-OpponentKickoffReturns.csv'
'national_team-2019-OpponentKickoffs.csv'
'national_team-2019-OpponentLongKickoffReturnPlays.csv'
'national_team-2019-OpponentLongPassingPlays.csv'
'national_team-2019-OpponentLongPuntReturnPlays.csv'
'national_team-2019-OpponentLongRushingPlays.csv'
'national_team-2019-OpponentLongScrimmagePlays.csv'
'national_team-2019-OpponentPATKicking.csv'
'national_team-2019-OpponentPenalties.csv'
'national_team-2019-OpponentPunting.csv'
'national_team-2019-OpponentPuntReturns.csv'
'national_team-2019-OpponentRedZoneConversions.csv'
'national_team-2019-PassesDefended.csv'
'national_team-2019-PassingDefense.csv'
'national_team-2019-PassingOffense.csv'
'national_team-2019-PATKicking.csv'
'national_team-2019-Penalties.csv'
'national_team-2019-Punting.csv'
'national_team-2019-PuntReturns.csv'
'national_team-2019-RedZoneConversions.csv'
'national_team-2019-RushingDefense.csv'
'national_team-2019-RushingOffense.csv'
'national_team-2019-Sacks.csv'
'national_team-2019-SacksAllowed.csv'
'national_team-2019-ScoringDefense.csv'
'national_team-2019-ScoringOffense.csv'
'national_team-2019-TacklesForLoss.csv'
'national_team-2019-TacklesForLossAllowed.csv'
'national_team-2019-TimeOfPossession.csv'
'national_team-2019-TotalDefense.csv'
'national_team-2019-TotalOffense.csv'
'national_team-2019-TurnoverMargin.csv'
##########################


# use iloc - location --> to slice and select data
'df = dfc.iloc[:5,2:5]'

#you can use the name of the column to get the data from that column - kind of like a key value
'titanic_names = dfc["Name"]'


####### TESTING FILTERING #######
print(thirdDownConversions.count())

thirdDownConversions_fil = thirdDownConversions[['Name','G','Attempts','Conversions','Conversion %']]
print(thirdDownConversions_fil)

thirdDownConversions_iowa = thirdDownConversions_fil[thirdDownConversions['Name']=='Iowa']
print(thirdDownConversions_iowa)
print(thirdDownConversions_fil.describe())
#################################





def compstats(data):
    data_fil = data.drop([data.columns[0]], axis='columns')
    data_fil2 = data.drop([data.columns[0], data.columns[1], data.columns[2]],  axis='columns')
    d_count = data_fil.count()
    d_iowa = data_fil[data_fil['Name']=='Iowa']
    d_neb = data_fil[data_fil['Name']=='Nebraska']
    d_desc = data_fil2.describe()
    return (d_iowa,d_neb,d_desc)


# test
print(compstats(fourthDownConversions))


#seeing all outputs of the function

# IS THERE A WAY TO PUT ALL OF THESE RESULTS IN A NEW FILE?
# https://datatofish.com/export-dataframe-to-csv/

print(compstats(fieldGoals))
print(compstats(firstDowns))
print(compstats(fumblesForced))
print(compstats(fumblesLost))
print(compstats(fumblesRecovered))    
print(compstats(thirdDownConversions))
print(compstats(interceptions))
print(compstats(kickoffReturns))
print(compstats(kickoffs))
print(compstats(kicksPuntsBlocked))
print(compstats(longKickoffReturnPlays))
print(compstats(longPassingPlays))
print(compstats(longPuntReturnPlays))
print(compstats(longRushingPlays))
print(compstats(longScrimmagePlays))
print(compstats(opponent3rdDownConversions))
print(compstats(opponent4thDownConversions))
print(compstats(opponentFieldGoals))
print(compstats(opponentFirstDowns))
print(compstats(opponentKickoffReturns))
print(compstats(opponentLongPassingPlays))
print(compstats(opponentLongPuntReturnPlays))





# IF ALL OF THE TEAMS HAVE INDIVIDUAL STATS IN THE DIFFERENT FILES...
# HOW WOULD I COMBINE ALL OF THEM TO CREATE AN OVERALL COMPARISON INSTEAD OF ONE 
# AT A TIME




# FOR A COMPARISON FROM YEAR TO YEAR... I HAVE DATA BACK TO 2009
# FIRST, EASIER WAY TO READ THE DATA INTO PYTHON 
# NEXT, SIMILAR TO ABOVE, HOW TO COMPARE FROM YEAR TO YEAR




# FOR LATER...
# WHAT TOOL OR PACKAGE WOULD WORK BEST TO CREATE A MODEL TO PREDICT THE SPREAD BASED ON UPCOMING GAMES





 	
# HOW TO...
# Delete columns at index 1 & 2
#modDfObj = dfObj.drop([dfObj.columns[1] , dfObj.columns[2]] ,  axis='columns')   


'''
survivors = dfc.count()

#use this to remove columns and select only the ones that you want
df_filtered = dfc[['Survived','Pclass','Name','Gender','Age','Fare']]

df_first = dfc[dfc['Pclass'] == 1]

"df_firstalive = dfc[dfc['Pclass'] == 1,dfc['Survived'] == 1]"

#distribution of column values
print(df_filtered.describe())


print(df_filtered['Survived'].value_counts())

#distribution of column values
print(df_filtered['Survived'].value_counts()) 

#distribution of column values
print(df_filtered['Gender'].value_counts()) 

#distribution of column values
print(df_filtered['Pclass'].value_counts()) 
'''



'''
#visualization
plt.figure() #reset plot
#a scatter plot of age and fare
df_filtered.plot(kind='scatter', x='Age', y='Fare')


plt.figure() #reset plot
# a histogram of 'Age'
df_filtered['Age'].hist()
plt.xlabel('Age') #from matplotlib
plt.savefig('age.pdf') #frommatplotlib


plt.figure() #reset plot
# a histogram of 'Survived'
df_filtered['Survived'].value_counts().plot('bar')


#grouping data
#Equivalent SQL: SELECT AVG(col3), AVG(col4) FROM df_fil GROUPBY col1
df_group1 = df_filtered.groupby('Gender').mean()
print(df_group1)

#group by TWO thigs
#Equivalent SQL: SELECT AVG(col3), AVG(col4) FROM df_fil GROUPBY col1,col2
df_group2 = df_filtered.groupby(['Gender','Pclass']).mean()
print(df_group2)

plt.figure()
df_group2['Survived'].plot('bar')


df_group3 = df_filtered.groupby('Age').mean()
print(df_group3)
'''
