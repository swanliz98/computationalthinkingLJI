#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:25:05 2019
@author: swanliz98
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
        else:
            while roll > 3:
                if roll == 4:
                    gamewinnings += roll
                elif roll == 5:
                    gamewinnings += roll
                elif roll == 6:
                    gamewinnings += roll
                roll = random.randint(1,6) 
        winningslist.append(gamewinnings)
        gamewinnings = 0
    averagewon = sum(winningslist) / len(winningslist)
    if winningslist != []:
        maxwon = max(winningslist)
    print(f"Average amount won = ${averagewon:0.2f}, max amount won per game = ${maxwon}.")
    return (averagewon, maxwon)
dicegame(10000)

'''
================================
For $3 a game, we would play. When running the simulation, the average amount you win
is usually close to 5. This being said, you still have good odds of making a profit of at least
$2 on average per game. Additionally, the max winnings went up above $100 in some outcomes, 
which is a great best case outcome for a $3 buy-in!

Initially it's a risky gamble. With 6 chances on the first roll only half of them win and the average
amount of money is 2.50 (the sum of 0,0,0,4,5,6 is 15... divided by 6 is 2.5) so you're immediately
thinking that you will on average lose 50 cents a game. However it's the fact that you get to keep
playing after a 4, 5, and 6 roll that make it worth playing. After running 10,000 simulations of the game
even though you still end up with zero 50% of the time, the average amount won increases to $5 - this is
due to the fact that your ability to keep winning is the same ability that sweetens the pot each time.
================================
'''
