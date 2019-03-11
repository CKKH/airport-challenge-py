from src.plane import Plane

class Airport:

    hanger_capacity = 2

    def __init__(self):
        self.hanger = []

    def land(self, plane):
        plane.land()
        if len(self.hanger) >= Airport.hanger_capacity: raise TypeError('Cannot land plane: hanger full')
        return self.hanger.append(plane)

    def take_off(self, plane):
        # if plane.grounded is False: raise TypeError('Cannot take off: plane not grounded')
        return self._take_off_if_plane_at_airport(plane)

    def _take_off_if_plane_at_airport(self, plane):
        if plane in self.hanger:
            plane.take_off()
            self.hanger.remove(plane)
            return plane
        else:
            raise TypeError('Cannot take off: plane not grounded at this airport')
