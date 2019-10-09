<<<<<<< HEAD
# -*- coding: utf-8 -*-
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
# -*- coding: utf-8 -*-
def dice(numsim):
    import random
    averagewon = 0
    gamewinnings = 0
    winninglist = []
    runtime = 0
    maxwon = 0
    
    while runtime < numsim:
        roll = random.randint(1,6)
        runtime += 1
        if roll <= 3:
            gamewinnings += 0;
        elif roll == 4:
            gamewinnings += roll
        elif roll == 5:
            gamewinnings += roll
        elif roll == 6:
            gamewinnings += roll
        winninglist.append(gamewinnings)
        
    averagewon = sum(winninglist)/len(winninglist)
    maxwon = max(winninglist)
    total = sum(winninglist)
    
    print("Average amount won= "+ "{0:.2f}".format(averagewon))
    print("Max amount won= " + str(maxwon))   
    return averagewon, maxwon  
    
dice(10000)

'''
For $3 a game, I would not play. With playing 10,000 different games at $3/game,
it'll cost you $30,000. When running 10,000 through my program, on average I would 
win close to $12000 with a max close to $25,000. This means that even when I do my best,
I still will be in the hole.
>>>>>>> 60cc574c995a8b1bf701b3372afef18a7fc9061f
'''