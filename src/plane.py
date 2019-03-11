class Plane:

    def __init__(self):
        self.grounded = False

    def land(self):
        # if self.grounded is True: raise TypeError('Cannot land plane: plane already landed')
        self.grounded = True

    def take_off(self):
        self.grounded = False
