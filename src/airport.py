class Airport:
    """ Releases and docks bikes """

    def __init__(self):

        self.hanger = []

    def land(self, plane):
        return self.hanger.append(plane)
