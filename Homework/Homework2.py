# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 14:02:09 2019

@author: Jessica Tse, Liz Swanson, Issac Perrilles
"""
import random

def dicegame(numsim):
    averagewon = 0
    gamewinnings = 0
    winningslist = []
    maxwon = 0
    while numsim > 0:
        numsim -= 1
        roll = random.randint(1,6)
        if roll < 4:
            gamewinnings += 0
        elif roll > 3:
            if roll == 4:
                gamewinnings += roll
            elif roll == 5:
                gamewinnings += roll
            elif roll == 6:
                gamewinnings += roll
        winningslist.append(gamewinnings)
    averagewon = sum(winningslist) / len(winningslist)
    if winningslist != []:
        maxwon = max(winningslist)
    print(f"Average amount won = {round(averagewon, 2)}, max amount won per game = {maxwon}.")
    return averagewon and maxwon

dicegame(6)

'''
x = [9,0,7]
y = [0,9,8]
x.extend(y)
'''