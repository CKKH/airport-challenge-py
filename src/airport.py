class Airport:

    def __init__(self):
        self.hanger = []

    def land(self, plane):
        if len(self.hanger) == 1:
            return 'Cannot land plane: hanger full'
        else:
            return self.hanger.append(plane)

    def take_off(self, plane):
        return self.hanger.remove(plane)
