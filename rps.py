import os


class Game_mech():
	""" Behaviour of Rock, Paper and Scissors with each other. Who wins. """

	result = "to be defined later"
	
	def rock(opponent):
		# Rock results against others.
		if opponent == "scissors":
			result = "win" 
			return result
		elif opponent == "rock":
			result = "draw"
			return result
		elif opponent == "paper":
			result = "lose"
			return result
		else:
			pring("game bugged in Game_mech.rock()")    # Debug print

	def scissors(opponent):
		# Scissors results against others.
		if opponent == "scissors":
			result = "draw"
			return result
		elif opponent == "rock":
			result = "lose"
			return result
		elif opponent == "paper":
			result = "win"
			return result
		else:
			print("Game bugged in Game_mech.scissors()")    # Debug print


	def paper(opponent):
		# Paper results against others
		if opponent == "scissors":
			result = "lose"
			return result
		elif opponent == "rock":
			result = "win"
			return result
		elif opponent == "paper":
			result = "draw"
			return result
		else:
			print("Game buuged in Game_mech.paper()") # Debug print

	def who_won(players1_choice, players2_choice):
		if players1_choice == "rock":
			return Game_mech.rock(players2_choice)
		elif players1_choice == "paper":
			return Game_mech.paper(players2_choice)
		elif players1_choice == "scissors":
			return Game_mech.scissors(players2_choice)
		else:
			print("Game bugged =(")   # Debug print


class Newgame():
	# Game starting, game flow, returns who won
	
	def players_names():
		# Asks for players names
		Player1 = input("Player №1, what is your name? ")
		Player2 = input("Player №2, what is your name? ")
		Newgame.game_flow(Player1, Player2)
	def game_flow(Player1, Player2):	
		# Conducts the game
		print("\n===============================================================\n\
		The game is about to begin. Get Ready!\n")
		print("\n" + Player2 + ", close your eyes!\n")
		choice1 = input(Player1 + ", your turn! Type \"rock\", \"paper\" or \"scissors\"\n")
		os.system('cls')
		print("\n===============================================================\nWell done, "\
		 + Player1 + ". Tell " + Player2 + " to open his or her eyes!\n")
		print(Player1 + ", close your eyes!\n")
		choice2 = input(Player2 + ", your turn! Type \"rock\", \"paper\" or \"scissors\"\n")
		os.system('cls')
		print("\n===============================================================\n\nGreat! " + \
			Player2 + ", tell " + Player1 + " to open his or her eyes!")

		if Game_mech.who_won(choice1, choice2) == "win":
			print("\n+++++++++++++++\n"  + Player1 + " wins!\n+++++++++++++++")
		elif Game_mech.who_won(choice1, choice2) == "lose":
			print("\n+++++++++++++++\n " + Player2 + " wins!\n+++++++++++++++")
		elif Game_mech.who_won(choice1, choice2) == "draw":
			print("\n+++++++++++++++\n " + "Its a draw!\n+++++++++++++++")
		else:
			print("Game bugged in Newgame")    # Debug print

		Main.restart_game(Player1, Player2)


class Main():
	# main loop 
	def welcome():
		print("===============================================================\n\
		Welcome to the \"Rock, Papaer, Scissors game!\"\n\
	===============================================================\n ")
		Newgame.players_names()

		
	def restart_game(Player1, Player2):
		
		game_on = 1
		while game_on == 1:
			restart = input("\nDo you want to start a new game? (type \"yes\")\n")
			
			if restart == "yes":
				Newgame.game_flow(Player1, Player2)
			else:
				quit()

			

Main.welcome()
