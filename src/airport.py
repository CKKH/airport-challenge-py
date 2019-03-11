''' Airport module '''

class Airport:
    ''' Creates Airport '''

    hanger_capacity = 2

    def __init__(self):
        self.hanger = []

    def land(self, plane):
        ''' Lands planes in hanger if conditions met '''

        plane.land()
        if len(self.hanger) >= Airport.hanger_capacity:
            raise TypeError('Cannot land plane: hanger full')
        return self._add_plane_to_hanger(plane)

    def take_off(self, plane):
        ''' Takes planes off if conditions met '''

        return self._remove_plane_from_hanger_if_at_airport(plane)
        plane.take_off()

    def _add_plane_to_hanger(self, plane):
        ''' Appends planes to hanger '''

        return self.hanger.append(plane)

    def _remove_plane_from_hanger_if_at_airport(self, plane):
        ''' Checks if plane grounded at airport '''

        if plane in self.hanger:
            self.hanger.remove(plane)
        else:
            raise TypeError(
                'Cannot take off: plane not grounded at this airport')
