from environment import Environment
import matplotlib.pyplot as plt
from grapher import plot


env = Environment(10, 10, .6, .1, 5, .1, .3)
# Environment(ns,nh,hfv,hlfv,sh,bhd,hd)

pop = []
age = []
born = []
dead = []

for i in range(5000):
    env.step()
    pop.append(len(env.shrimp))
    # born.append(env.born)
    # dead.append(env.dead)
    # age.append(sum([]))
    # plot(0,born)
    # plot(1,dead)
    plot(2,pop)
    plot(0,env.pb)
    plot(1,env.ib)
    plt.show(block=False)
