class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason = Enemy(9)
lucy = Enemy(20)

jason.get_energy()
lucy.get_energy()


