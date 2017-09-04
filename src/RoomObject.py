class RoomObject:
    name        = ''

    def __init__(self, name):
        self.setName(name)

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name