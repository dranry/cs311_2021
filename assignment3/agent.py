#Example command line argument
#python agent.py --last_opponent_move "silent"
#The --command is used to specify which field each input applies to
import argparse
import random
import json

#   Plans:
#   The plan is to make my agent randomly choose based on previous iterations
#   By keeping track of opponent's previous confessions or silents my age will decide whether to remain silent or confess
#       But in order to avoid being appeased just enough to keep my agent happy, the confessions will be weighted slightly more than silence
#       This means that each time the opponent confesses will have more impact on the agent than when they are cooperative
#   By keeping track of up to ten past iterations, this means any confession against the agent will last 10 moves
#
#   There will also be a base chance of 30% to confess just to keep things lively

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--init', help='called when new game')
    parser.add_argument('--iterations', help='number of iterations in game')
    parser.add_argument('--last_opponent_move', help='last opponent move')

    args = parser.parse_args()

    #num_moves = 0
    past_moves = []
    #To make sure that the file exists
    with open("grievances.json", "a") as f: 
        pass
    #Reads past opponent moves into past_moves list
    with open("grievances.json", "r") as openfile: 
        try:
            past_moves = json.load(openfile)
            #num_moves = (past_moves.pop())
        except:
            past_moves = []

    #Keeps track of what iteration we're in
    #num_moves += 1
    #Loads last move argument into last_move
    last_move = args.last_opponent_move 

    #Appends current iteration's past move, only if it was a recognized input
    if last_move == 'silent' or last_move == 'confess':
        past_moves.insert(0, last_move)

    #Keeps total recorded moves limited, essentially this will determine the lifespan of each past iteration
    if len(past_moves) > 10:
    	past_moves.pop() #Pops oldest iteration off the list

    ######################################################################### Primary work in here
    decision = 'silent'#Default to silent
    if len(past_moves) > 0: #On the first move we won't really be dealing with any decison making, silence by default
        #Counts opponent's previous moves
        num_silent = 0
        num_confess = 0
        for i in past_moves:
            if i == 'silent':
                num_silent += 1
            elif i == 'confess':
                num_confess += 1

        #This is where of decisions of how to act are made
        #Confessions will be weighted differently
        num_confess = int(num_confess * 1.5)
        #This will mean that even when not wronged at all, there will be a chance to confess
        if num_confess < 3:
            num_confess = 3
        #Using a random number to determine how favorable to play given what's happened to this point
        determinator = random.randint(1,10)
        if (num_confess) >= determinator: 
            decision = 'confess'

    #########################################################################

    #Saves number of moves into the list to be saved into the json for potential use in next iteration
    #past_moves.append(num_moves)
    #Converts the moves to a json format to be written to a file
    save_moves = json.dumps(past_moves) 

    #Saves the past moves list into a file for use in next iteration
    with open("grievances.json", "w") as outfile:
        outfile.write(save_moves)

    #Prints output decision, being the string output, either 'confess' or 'silent' based on the decisions made
    print(decision) 
    
