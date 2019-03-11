''' Plane module '''


class Plane:
    ''' Creates Plane '''

    def __init__(self):
        self.grounded = False

    def land(self):
        ''' Sets grounded status to True if flying '''

        self._raise_error_if_plane_grounded()
        self.grounded = True

    def take_off(self):
        ''' Sets grounded status to False if grounded '''

        self._raise_error_if_plane_not_grounded()
        self.grounded = False

    # Private

    def _raise_error_if_plane_grounded(self):
        ''' Stops plane landing if grounded already '''

        if self.grounded:
            raise TypeError('Cannot land plane: plane already landed')

    def _raise_error_if_plane_not_grounded(self):
        ''' Stops plane taking off if flying '''

        if not self.grounded:
            raise TypeError('Cannot take off: plane not grounded')
