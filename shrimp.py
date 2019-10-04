from enum import Enum

State = Enum('State', 'homeless housed pregnant')


class Shrimp:
    def __init__(self, start_health, base_health_dec, health_dec, dna):
        self.state = State.homeless
        self.base_health = start_health
        self.health = self.base_health
        self.health_dec = health_dec
        self.base_health_dec = base_health_dec
        self.dna = dna
    
    def step(self, env):
        self.base_health -= self.base_health_dec
        self.health -= self.health_dec
        if self.state == State.homeless:
            env.search(self)
        elif self.state == State.pregnant:
            self.set_state(State.housed)
        elif self.state == State.housed:
            env.search_for_mate(self)
        env.find_food(self)
        
    def set_state(self,state):
        self.state = state

    def bid(self):
        pass
