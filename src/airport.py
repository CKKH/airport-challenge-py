from src.plane import Plane

class Airport:

    hanger_capacity = 2

    def __init__(self):
        self.hanger = []

    def land(self, plane):
        if plane.grounded is True: return 'Cannot land plane: plane already landed'
        if len(self.hanger) >= Airport.hanger_capacity: return 'Cannot land plane: hanger full'
        plane.land()
        return self.hanger.append(plane)

    def take_off(self, plane):
        if plane.grounded is False: return 'Cannot take off: plane not grounded'
        return self._take_off_if_plane_at_airport(plane)

    def _take_off_if_plane_at_airport(self, plane):
        if plane in self.hanger:
            plane.take_off()
            self.hanger.remove(plane)
            return plane
        else:
            return 'Cannot take off: plane not grounded at this airport'
