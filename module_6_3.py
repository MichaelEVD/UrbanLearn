class Horse:
    x_distance = 0
    sound = 'Frrr'
    def __init__(self, dx):
        self.dx = dx
        

    def run(self, dx):
        Horse.x_distance += dx

class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'
    def __init__(self,dy):
        self.dy = dy

    def fly(self, dy):
        Eagle.y_distance +=dy

class Pegasus(Horse,Eagle):
    def __init__(self):
        super().__init__(self)


    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return (super().x_distance,super().y_distance)
    def voice(self):
        self.sound = super().sound
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()