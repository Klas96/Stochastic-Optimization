class particle():

    def __init__(self):
        self.pos = (0, 0)
        self.vel = (0, 0)

    def move(self):
        self.pos += self.vel