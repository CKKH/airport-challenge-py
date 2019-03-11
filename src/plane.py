class Plane:

    def __init__(self):
        self.grounded = False

    def land(self):
        if self.grounded: raise TypeError('Cannot land plane: plane already landed')
        self.grounded = True

    def take_off(self):
        if not self.grounded: raise TypeError('Cannot take off: plane not grounded')
        self.grounded = False
