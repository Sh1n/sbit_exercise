import collections

from .RoomObject import RoomObject

class Room:

    id          = ''
    name        = ''
    northId     = None
    southId     = None
    westId      = None
    eastId      = None
    objects     = []
    visits      = 0

    def __init__(self, roomObject):

        if not 'id' in roomObject:
            raise ValueError('Room definition should contain attribute id')

        try:
            roomId = int(roomObject['id'])
            self.setId(roomId)
        except:
            raise ValueError('Room identifier should be numeric') 

        if not 'name' in roomObject:
            raise ValueError('Room definition should contain attribute name')


        self.setName(roomObject['name'])
        
        if('north' in roomObject):
            self.setNorthRoomId(roomObject['north'])

        if('east' in roomObject):
            self.setEastRoomId(roomObject['east'])

        if('south' in roomObject):
            self.setSouthRoomId(roomObject['south'])

        if('west' in roomObject):
            self.setWestRoomId(roomObject['west'])

        if type(roomObject['objects']) is str or not isinstance(roomObject['objects'], collections.Iterable):
            raise ValueError('Room\'s definition of contained objects should be a list')

        if('objects' in roomObject):
            self.setObjects([roomItem['name'] for roomItem in roomObject['objects'] if 'name' in roomItem])

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getObjects(self):
        return self.objects

    def setObjects(self, objects):
        self.objects = objects

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def getNorthRoomId(self):
        return self.northId

    def getSouthRoomId(self):
        return self.southId

    def getWestRoomId(self):
        return self.westId

    def getEastRoomId(self):
        return self.eastId

    def setNorthRoomId(self, roomId):
        self.northId = roomId

    def setSouthRoomId(self, roomId):
        self.southId = roomId

    def setWestRoomId(self, roomId):
        self.westId = roomId

    def setEastRoomId(self, roomId):
        self.eastId = roomId

    def hasNorthRoom(self):
        return not (self.northId is None)

    def hasSouthRoom(self):
        return not (self.southId is None)

    def hasWestRoom(self):
        return not (self.westId is None)

    def hasEastRoom(self):
        return not (self.eastId is None)

    def getAvailableRooms(self):
        rooms = []
        if self.hasEastRoom():
            rooms.append(self.getEastRoomId())
        if self.hasWestRoom():
            rooms.append(self.getWestRoomId())
        if self.hasSouthRoom():
            rooms.append(self.getSouthRoomId())
        if self.hasNorthRoom():
            rooms.append(self.getNorthRoomId())
        return rooms

    def cleanRooms(self):
        self.setSouthRoomId(None)
        self.setNorthRoomId(None)
        self.setEastRoomId(None)
        self.setWestRoomId(None)

    def getContainedItems(self, requestedItems):
        return [reqItem for reqItem in requestedItems if reqItem in self.getObjects()]

    def enter(self):
        self.visits = self.visits + 1
        