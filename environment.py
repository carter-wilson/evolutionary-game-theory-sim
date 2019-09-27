import random

from shrimp import Shrimp, States
from fight import fight

class Environment:
    def __init__(self, num_shrimp, num_homes, housed_food_value, homeless_food_value, start_health, base_health_dec, health_dec):
        self.homes = [None for _ in range(num_homes)]
        self.shrimp = [Shrimp(start_health, base_health_dec, health_dec) for _ in range(num_shrimp)]
        self.housed_food_value, self.homeless_food_value = housed_food_value, homeless_food_value
    
    def step(self):
        dead = set()
        for s in range(self.shrimp):
            self.shrimp[s].step(self)
            if self.shrimp[s].health <= 0:
                dead.add(s)
        self.shrimp[:] = [s for s in self.shrimp if not s in d]
        
    def search(self,s):
        i = random.randrange(len(self.homes))
        if self.homes[i] is None:
            s.set_state(State.housed)
            self.homes[i] = s
        else:
            wl = fight(self.homes[i],s)
            self.homes[i] = wl[0]
            wl[0].set_state(State.housed)
            wl[1].set_state(State.homeless)

    def find_food(self,s):
        food = random.random()*self.housed_food_value if s.state==State.housed else random.random()*self.homeless_food_value
        s.health = min(s.base_health, s.health+food)
    
    def mate(self,s):
        pass
