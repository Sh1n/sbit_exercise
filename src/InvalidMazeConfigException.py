class InvalidMazeConfigException(Exception):
    def __init__(self, message):
        super(InvalidMazeConfigException, self).__init__(message)
        self.message = message