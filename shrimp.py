import math
import random


def generate_base_dna():
    return {'strength': random.lognormvariate(0, 1), 'sexiness': random.normalvariate(0, 1),
            'pdisc': random.normalvariate(0, 1), 'idisc': random.normalvariate(0, 1),
            'pdish': random.normalvariate(0, 1), 'idish': random.normalvariate(0, 1),
            'pbidc': random.normalvariate(0, 1), 'ibidc': random.normalvariate(0, 1),
            'pbidh': random.normalvariate(0, 1), 'ibidh': random.normalvariate(0, 1),
            'pbidd': random.normalvariate(0, 1), 'ibidd': random.normalvariate(0, 1)}


def exp(x):
    return x + 1 if x>=0 else math.exp(x)


class Shrimp:
    age = 0
    def __init__(self, start_health, base_health_dec, health_dec, dna=None):
        self.homeless = True
        self.fertile = 0
        self.base_health = start_health
        self.health = self.base_health
        self.health_dec = health_dec
        self.base_health_dec = base_health_dec
        if dna is None:
            dna = generate_base_dna()
        self.dna = dna

    def step(self, env):
        self.age += 1
        self.base_health -= self.base_health_dec
        self.health -= self.health_dec
        self.fertile += 1
        if self.homeless:
            env.search(self)
        elif self.fertile > 3:
            env.search_for_mate(self)
        env.find_food(self)

    def pos_display(self):
        return exp(self.health * self.dna['pdish'] + self.dna['pdisc'])

    def int_display(self):
        return exp(self.health * self.dna['idish'] + self.dna['idisc'])

    def pos_bid(self, display):
        return exp(self.health * self.dna['pbidh'] + self.dna['pbidc'] + display * self.dna['pbidd'])

    def int_bid(self, display):
        return exp(self.health * self.dna['ibidh'] + self.dna['ibidc'] + display * self.dna['ibidd'])
