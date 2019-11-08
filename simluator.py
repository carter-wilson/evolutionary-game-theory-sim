from environment import Environment
import matplotlib.pyplot as plt
from grapher import plot


env = Environment(50, 45, .6, .1, 5, .1, .3)
# Environment(ns,nh,hfv,hlfv,sh,bhd,hd)

pop = []
age = []


for i in range(5000):
    env.step()
    pop.append(len(env.shrimp))
    # age.append(sum([]))
    plot(0,pop)
    plt.show(block=False)
