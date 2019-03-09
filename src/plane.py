class Plane:

    def __init__(self):
        self.grounded = False

    def land(self):
        self.grounded = True

    def take_off(self):
        self.grounded = False
