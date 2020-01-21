from environment import Environment
import matplotlib.pyplot as plt
from grapher import plot

import json




savefile = 'goodsave{}.json'


for s in range(10):

    env = Environment(500, 500, .5, .1, 5, .1, .3)
    # Environment(ns,nh,hfv,hlfv,sh,bhd,hd)

    pop = []
    #age = []
    #born = []
    #dead = []
    #old = []

    for i in range(10000):
        try:
            env.step()
            pop.append(len(env.shrimp))
            # born.append(env.born)
            # dead.append(env.dead)
            #ages = [i.age for i in env.shrimp]
            #age.append(sum(ages)/len(env.shrimp))
            #old.append(max(ages))
            # plot(0,born)
            # plot(1,dead)
            # plot(2,pop)
            # plot(3,old)
            # plot(3,age,overwrite=False)
            # plot(0,env.pb)
            # plot(1,env.ib)
            # plt.show(block=False)
            if i % 1000 == 0:
                print(s,i)
        except ZeroDivisionError:
            pass

    d={'pop':pop,'biddif':env.biddiff}

    json.dump(d,open(savefile.format(s),'w'))
