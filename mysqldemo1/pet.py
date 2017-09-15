class Pet:
    def __init__(self):
        self.name = 'buffy'
        self.owner = 'Gwen'
        self.species = 'cat'
        self.sex = 'f'
        self.birth = '1990-8-05'
        self.death = None

    def __iter__(self):
        return iter([self.name, self.owner, self.species, self.sex, self.birth, None])

    def __str__(self):
        return ",".join([self.name,self.owner,self.species,self.sex,self.birth,self.death if self.death else 'None'])

