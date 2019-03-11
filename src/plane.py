''' Plane module '''


class Plane:
    ''' Creates Plane '''

    def __init__(self):
        self.grounded = False

    def land(self):
        ''' Sets grounded status to True if flying '''

        if self.grounded:
            raise TypeError('Cannot land plane: plane already landed')
        self.grounded = True

    def take_off(self):
        ''' Sets grounded status to False if grounded '''

        if not self.grounded:
            raise TypeError('Cannot take off: plane not grounded')
        self.grounded = False
