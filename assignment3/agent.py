import argparse
import random
#Example command line argument
#python 007.py --last_opponent_move "silent"
#It seems like the --command is used to specify which field each input applies to
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--init', help='called when new game')
    parser.add_argument('--iterations', help='number of iterations in game')
    parser.add_argument('--last_opponent_move', help='last opponent move')

    args = parser.parse_args()

    print(args.last_opponent_move)

    print( random.choice(['confess', 'silent']) )
    


