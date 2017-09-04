import sys
import json

from tabulate                       import tabulate
from src.PuzzleSolver               import PuzzleSolver

def printRoute(route):
    headings        = ['ID', 'Room', 'Objects']
    rows            = [(node[0], node[1], ",".join(node[2]) if len(node[2]) else 'None') for node in route] 
    print tabulate(rows, headings, tablefmt="grid")


def run():
    try:
        params      = sys.argv

        if len(params) < 3:
            print 'Required parameters are <maze file path> <starting room id> <item to look for+>'
            sys.exit(0)

        json_maze   = json.load(open(params[1]))


        startRoomId = int(params[2])
        if startRoomId <= 0:
            print 'Invalid starting room id'
            sys.exit(0)

        items       = [item for item in params[3:] if item]

        if len(items) == 0:
            print 'A set of items to search is required for solving the puzzle'
            sys.exit(0)

        puzzleSolver = PuzzleSolver()
        route        = puzzleSolver.solvePuzzle(json_maze, startRoomId, items)
        printRoute(route)
    
    except Exception as e:
        print e


if __name__ == "__main__":
    run()