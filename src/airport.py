class Airport:

    hanger_capacity = 1

    def __init__(self):
        self.hanger = []

    def land(self, plane):
        if len(self.hanger) == Airport.hanger_capacity:
            return 'Cannot land plane: hanger full'
        else:
            return self.hanger.append(plane)

    def take_off(self, plane):
        return self.hanger.remove(plane)
