"""In raquetball, a player continues to serve as long as she is winning; 
a point is scored only when a player is serving and wins the volley. 
The first player to win 21 points wins the game. 
Assume that you serve first and have a probability .6 of winning a volley when you serve and probability .5 when your opponent serves. 
Estimate, by simulation, the probability that you will win a game.
"""

import random
# n is the number of big games played
def probability(n):
	result = 0
	for i in range (n):
		#Our point 
		you = 0
		#Opponent's point 
		opponent = 0
		turn = 0
		#When no one reaches 21 yet, the game continues 
		while you < 21 and opponent < 21: 
			#Our turn 
			if turn == 0:
				result1 = random.random()
				#If we win, turn still equals 0, we gain one point and continue serving 
				if result1 > 0.4:
					you += 1
				#If we lose, turn becomes 1, our opponent serves next time
				else: 
					turn = 1
			#Opponent's turn
			else:
				result2 = random.random()
				#If opponent wins, turn still equals 1, opponent gains one point and continues serving 
				if result2 > 0.5:
					opponent += 1
				#If opponent loses, turn becomes 0, we serve next time
				else: 
					turn = 0
		if you == 21: 
			result += 1
#prob is the probability that we win in n games we play 
	prob = result/ float(n)
	return prob

print probability(10000)


import random 
def probability(n):
    count = 0
    for i in range (n):
        score = ''
        shot=0
        while shot < 20:
            p = random.random()
            shot+=1
            if p > 0.5:
                score+='1'
            else:
                score+='0'
        t = score.count('11111')   
        if t > 0:
            count += 1
    prop = (float(count)/int(n))*100
    return prop 


	