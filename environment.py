import random
from shrimp import Shrimp
from fight import fight


class Environment:
    born = 0
    dead = 0
    def __init__(self, num_shrimp, num_homes, housed_food_value, homeless_food_value, start_health, base_health_dec,
                 health_dec):
        self.biddiff = list()
        self.homes = [None for _ in range(num_homes)]
        self.shrimp = [Shrimp(start_health, base_health_dec, health_dec) for _ in range(num_shrimp)]
        self.born = num_shrimp
        self.housed_food_value, self.homeless_food_value = housed_food_value, homeless_food_value
        self.start_health = start_health

    def step(self):
        self.horny = set()
        dead = set()
        for s in range(len(self.shrimp)):
            self.shrimp[s].step(self)
            if self.shrimp[s].health <= 0:
                dead.add(self.shrimp[s])
                self.dead+=1
        self.shrimp[:] = [s for s in self.shrimp if not s in dead]
        h1 = random.sample(self.horny, min(len(self.horny), int(len(self.horny) // 2)+1))
        h2 = self.horny.difference(h1)
        for i, s in enumerate(h2):
            self.mate(h1[i], s)

    def search(self, s):
        i = random.randrange(len(self.homes))
        if self.homes[i] is None:
            s.homeless = False
            self.homes[i] = s
        else:
            wl = fight(self.homes[i], s)
            self.homes[i] = wl[0]
            wl[0].homeless = False
            wl[1].homeless = True
            self.biddiff.append(wl[2]-wl[3])

    def find_food(self, s):
        food = random.random() * self.homeless_food_value if s.homeless else random.random() * self.housed_food_value
        s.health = min(s.base_health, s.health + food)

    def search_for_mate(self, s):
        self.horny.add(s)

    def mate(self, a, b):
        dna = self.dna_merge(a.dna, b.dna)
        s = Shrimp(self.start_health, a.base_health_dec, a.health_dec, dna)
        a.fertile = 0
        b.fertile = 0
        self.shrimp.append(s)
        self.born+=1

    def dna_merge(self, a, b):
        dna = dict()
        for k in a:
            dna[k] = (a[k] + b[k]) / 2 + random.normalvariate(0,0.2)
        return dna
