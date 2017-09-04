import collections
from time import time

from .Room                       import Room
from .InvalidMazeConfigException import InvalidMazeConfigException

class PuzzleSolver:

    rooms       = {}

    def solvePuzzle(self, maze, startRoomId, items):

        if type(maze) is str or not isinstance(maze, collections.Iterable) or not ("rooms" in maze):
            raise InvalidMazeConfigException('Maze config should be a sequence containing the property "rooms"')
        
        if not type(startRoomId) is int :
            raise ValueError('Starting point should be a numeric identifier')
        
        if type(items) is str or not isinstance(items, collections.Iterable):
            raise ValueError('Items to gather should be an array')
        
        self._buildMaze(maze)

        if not startRoomId in self.rooms:
            raise ValueError('Starting point should exists in the maze configuration')
        
        route = self._collectItems(startRoomId, items)
        return route

    def _collectItems(self, roomId, items):
        if(len(items) == 0):
            return []
        if (roomId in self.rooms):
            route, pathStack    = [], [roomId]
            while pathStack and len(items):
                roomId          = pathStack.pop()
                roomObject      = self.rooms[roomId]
                containedItems  = roomObject.getContainedItems(items)
                routeNode       = [roomObject.getId(), roomObject.getName(), containedItems]
                route.append(routeNode)
                items           = [x for x in items if x not in containedItems]
                print items
                roomsToVisit    = [roomId for roomId in roomObject.getAvailableRooms() if roomId in self.rooms] 
                roomObject.cleanRooms()

                for i in roomsToVisit:
                    pathStack.append(i)

            return route
        else:
            return False;


    def _buildMaze(self, maze):
        self.rooms = {}
        for room in maze['rooms']:
            if not 'id' in room:
                raise InvalidMazeConfigException('Maze\' rooms should contain the id property')
            if not 'name' in room:
                raise InvalidMazeConfigException('Maze\' rooms should contain the name property')
            self.rooms[room['id']] = Room(room)
