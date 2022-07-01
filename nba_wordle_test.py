import random
import pandas as pd 
import numpy 






def processGuess(theAnswer, theGuess):
	
	position = 0
	clue = ""
	player_input = theGuess

	if player_input[0] == theAnswer[0]:
		clue += " Yes Name "
	else:
		clue += " No Name |"

	if player_input[1] == theAnswer[1]:
		clue += " Yes Position | "
	else:
		clue += " No Position | "

	if player_input[2] == theAnswer[2]:
		clue += " Yes All star appearances | "
	
	elif player_input[2] > theAnswer[2]:

		clue += " > All Star appearances |"

	elif player_input[2] < theAnswer[2]:

		clue += " < All Star appearances | "

	if player_input[3] == theAnswer[3]:
		clue += " Yes Height | "
	
	elif player_input[3] > theAnswer[3]:

		clue += " > Height | "

	elif player_input[3] < theAnswer[3]:

		clue += " < Height | "

	if player_input[4] == theAnswer[4]:
		clue += " Yes Weight | "
	
	elif player_input[4] > theAnswer[4]:

		clue += " > Weight | "

	elif player_input[4] < theAnswer[4]:

		clue += " < Weight | "

	if player_input[5] == theAnswer[4]:
		clue += " Date of Birth | "
	
	elif player_input[5] > theAnswer[5]:

		clue += " > Date of Birth | "

	elif player_input[5] < theAnswer[5]:

		clue += " < Date of Birth | "

	if player_input[0] == theAnswer[0]:
		clue = "Yes"	

	print(clue)
	return clue == "Yes" 

#reading nba hall of famers data
difficulty = input ("Choose your difficulty 1. Normal 2. GrandMaster ")
if difficulty == "GrandMaster":
	df_answer = pd.read_csv('NBA hall of famers all.csv')
	count_row = df_answer.shape[0]

elif difficulty == "Normal":
	df_answer = pd.read_csv('nba all star easy.csv')
	count_row = df_answer.shape[0]

else:
	print("please select a difficulty")






#pick a player

df_all = pd.read_csv('NBA hall of famers all.csv')
player_random = random.randint(1, count_row)

#geting answer
answer_player= df_answer.iloc[player_random -1].to_numpy()
answer_name = answer_player[0]

print(answer_player)





#clues
clue_position = answer_player[1]
clue_allstar = answer_player[2]
clue_height = answer_player[3]
clue_weight = answer_player[4]
clue_born = answer_player[5]




num_guesses = 0

guessed_correct = False 

while num_guesses < 6 and not guessed_correct:
	guess = input("Input a nba hall of famer and press enter:")
	print("You have guess", guess)
	num_guesses += 1 

	#process guess
	guess_input = (df_all.loc[df_all['Name'] == guess].to_numpy())
	guess = guess_input[0]
	print(guess)

	guessed_correct = processGuess(answer_player, guess)

if guessed_correct:
	print("Congrats you guessed the correct hall of famer in " , num_guesses, "times!")

else:
	print("You have used all your guesses the correct answer was", answer_name)




