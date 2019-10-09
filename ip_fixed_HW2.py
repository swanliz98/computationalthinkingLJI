# -*- coding: utf-8 -*-
'''
DiceGame created 10/9/19
@ author: Isaac Perrilles, Liz Swanson, Jessica Tse
'''

def dicegame(numsim):
    import random
    averagewon = 0
    winninglist = []
    runtime = 0
    maxwon = 0
    
    while runtime < numsim:
        roll = random.randint(1,6)
        gamewinnings = 0
        runtime += 1
        if roll <= 3:
            gamewinnings += 0
        else:
            while roll > 3:
                if roll == 4:
                    gamewinnings += 4
                elif roll == 5:
                    gamewinnings += 5
                elif roll == 6:
                    gamewinnings += 6
                roll = random.randint(1,6)
        winninglist.append(gamewinnings)
    
    if len(winninglist) == 0:
        averagewon = 0
    else:
        averagewon = sum(winninglist)/len(winninglist)
        
    maxwon = max(winninglist)
    
    print("Average amount won= "+ "{0:.2f}".format(averagewon))
    print("Max amount won= " + str(maxwon)) 
    return averagewon, maxwon
 
dicegame(10000)
'''
For $3 a game, I would play. When running the simulation, the average amount you win
is usually close to 5. This being said, you still have good odds of making a profit of at least
$2 on average per game. Additionally, the max won that I received was close to $70, 
which is a great best case outcome for a $3 buy-in.
=======
