#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:07:27 2019

@author: swanliz98
"""

import pandas as pd

'''
def yearlyimput(year):

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
 '''   
    
    
    
#def yearlyimput(year):
    
#    thirdDownConversions.year = pd.read_csv('national_team-2019-3rdDownConversions.csv')
#    fourthDownConversions.year = pd.read_csv('national_team-2019-4thDownConversions.csv')
#    fieldGoals.year = pd.read_csv('national_team-2019-FieldGoals.csv')
#    firstDowns.year = pd.read_csv('national_team-2019-FirstDowns.csv')
#    fumblesForced.year = pd.read_csv('national_team-2019-FumblesForced.csv')
#    return(1)
    

######################
# THIS WORKS - ADD ALL OF THE THINGS TO THE LIST TO GET THE FILE NAMES.

variable_names= ['thirdDownConversions','fourthDownConversions','fieldGoals','firstDowns','fumblesForced']
file_names= ['national_team-2019-3rdDownConversions.csv','national_team-2019-4thDownConversions.csv','national_team-2019-FieldGoals.csv','national_team-2019-FirstDowns.csv','national_team-2019-FumblesForced.csv']


base = 'national_team-'

years=['2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']


ending = []
for name in file_names:
    ending.append(name[18:])


# THIS SUCCESSFULLY TAKES THE BASE, YEAR, AND ENDING AND COMBINES THEM
year_file_names = []
for i in years:
    for j in ending:
        year_file_names.append((base+i+j))
        
        
# THIS SUCCESSFULLY TAKES THE VARIABLE NAME AND ADDS THE YEAR AT THE END         
v_yearly = []        
for i in years:
    for j in variable_names:
        v_yearly.append((j+i))



def readallcsv(varnames,csvfiles):
    counter = len(varnames)
    while counter >=0:
        vn = varnames[counter]
        cf = csvfiles[counter]
        return(vn=pd.read_csv(cf))
        counter -=1


######################
        
        
for file in 