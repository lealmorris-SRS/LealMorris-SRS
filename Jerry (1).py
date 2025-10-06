import random

def bananabid(my_player_number, my_bananas, monkey_position, opponent_bananas, past_bid_list, turn_number):
	
	if opponent_bananas == 0 and my_bananas > 0:
		return 1
	else:
		if opponent_bananas >= 100:
			return random.randint(15, 100)
		elif my_bananas <= 99:
			return random.randint(30, 50)
		