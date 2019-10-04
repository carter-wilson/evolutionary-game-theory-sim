import random

from shrimp import Shrimp, State
from fight import fight


class Environment:
    def __init__(self, num_shrimp, num_homes, housed_food_value, homeless_food_value, start_health, base_health_dec,
                 health_dec):
        self.homes = [None for _ in range(num_homes)]
        self.shrimp = [Shrimp(start_health, base_health_dec, health_dec, self.random_dna()) for _ in range(num_shrimp)]
        self.housed_food_value, self.homeless_food_value = housed_food_value, homeless_food_value

    def random_dna(self):
        return {'sexiness': random.random()}

    def step(self):
        self.horny = set()
        dead = set()
        for s in range(self.shrimp):
            self.shrimp[s].step(self)
            if self.shrimp[s].health <= 0:
                dead.add(s)
        self.shrimp[:] = [s for s in self.shrimp if not s in dead]
        h1 = random.sample(self.horny, len(self.horny) // 2)
        h2 = self.horny.difference(h1)
        for i, s in enumerate(h2):
            self.mate(h1[i], h2)

    def search(self, s):
        i = random.randrange(len(self.homes))
        if self.homes[i] is None:
            s.set_state(State.housed)
            self.homes[i] = s
        else:
            wl = fight(self.homes[i], s)
            self.homes[i] = wl[0]
            wl[0].set_state(State.housed)
            wl[1].set_state(State.homeless)

    def find_food(self, s):
        food = random.random() * self.housed_food_value if s.state == State.housed else random.random() * self.homeless_food_value
        s.health = min(s.base_health, s.health + food)

    def search_for_mate(self, s):
        self.horny.add(s)

    def mate(self, a, b):
        dna = self.dna_merge(a.dna, b.dna)
        s = Shrimp(a.start_health, a.base_health_dec, a.health_dec, dna)
        a.set_state(State.pregnant)
        b.set_state(State.pregnant)

    def dna_merge(self, a, b):
        return a
