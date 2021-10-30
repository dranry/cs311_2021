#Example command line argument
#python agent.py --last_opponent_move "silent"
#The --command is used to specify which field each input applies to

#	Plans:
#	The first time I like the idea of either always cooperating or at least having a high chance to.
#	When receiving opponent's previous move, store it into a data structure
#	Loop through the data structure to see how the game is going
# 	Decide from there if the person is not to be coordinated with anymore.
#	To keep things recent, might do a limited structure that will forgot after 4 or so moves
#	The above should hopefully prevent someone from playing nice a little too much to fool me but not enough to let me come out ahead
#	After a certain amount of "betrayals" in a row, might just completely write off opponent and refuse to cooperate further.
#	Keep Track of iterations because, ofc, we're all going to play the bad guy on the last iteration considering there are no penalties from there,
#		Maybe even play the bad guy for the last like, maybe 10, iterations of the game considering the farther you get into the game, the less chance they have to retaliate


#	Maybe, thought will be to play well, unless opponent plays rudely, sprinkling in a couple confesses here and there 
#	Based on what the opponent is doing, then play super rude for the last 10 or so iterations

#TLDR:	Play nicely with a relatively short term memory to try and prevent people from playing just slightly favorably enough to keep my agent favorable.
#			Potentially a lot of details to sort out in the end.
#			Need to figure out which structure is gonna be used, htinking a limited space stack.
#		Might keep track of how every iteration goes just to have a general overview of how the game is going.
#		Probably a good idea to track mine and my opponents points
#		Save all of this to a json
import argparse
import random
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--init', help='called when new game')
    parser.add_argument('--iterations', help='number of iterations in game')
    parser.add_argument('--last_opponent_move', help='last opponent move')

    args = parser.parse_args()

    past_moves = []
    #To make sure that the file exists
    with open("grievances.json", "a") as f: 
        pass
    #Reads past opponent moves into past_moves list
    with open("grievances.json", "r") as openfile: 
        try:
            past_moves = json.load(openfile)
        except:
            past_moves = []
            pass

    last_move = args.last_opponent_move 

    #Appends current iteration's past move
    if last_move != None:
        past_moves.append(last_move) 

    #Puts moves into save_moves in json format to be saved into file
    save_moves = json.dumps(past_moves) 

    #Saves the past moves list into a file for use in next iteration
    with open("grievances.json", "w") as outfile:
        outfile.write(save_moves)

    #Prints output decision
    print( random.choice(['confess', 'silent']) )
    #print(decision) #decision being the string output, either 'confess' or 'silent' based on algorithm
    
