from src.plane import Plane

class Airport:

    hanger_capacity = 2

    def __init__(self):
        self.hanger = []

    def land(self, plane):
        if plane.grounded == True: return 'Cannot land plane: plane already landed'
        if len(self.hanger) >= Airport.hanger_capacity: return 'Cannot land plane: hanger full'
        plane.land()
        return self.hanger.append(plane)

    def take_off(self, plane):
        if plane.grounded == False: return 'Cannot take off: plane not grounded'
        if len(self.hanger) == 0: return 'Cannot take off: hanger empty'
        plane.take_off()
        return self.hanger.remove(plane)
