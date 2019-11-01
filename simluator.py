from environment import Environment

env = Environment(100, 80, .6, .1, 5, .1, .3)
# Environment(ns,nh,hfv,hlfv,sh,bhd,hd)

for i in range(5000):
    env.step()
    print(len(env.shrimp),end='\t')
    # print(sum([s.dna['strength'] for s in env.shrimp])/len(env.shrimp))
    # print(round(sum([s.dna['pbidc'] for s in env.shrimp])/len(env.shrimp),1),end='\t')
    # print(round(sum([s.dna['ibidc'] for s in env.shrimp])/len(env.shrimp),1),end='\t')
    print(round(sum([s.dna['pbidh'] for s in env.shrimp])/len(env.shrimp),1),end='\t')
    print(round(sum([s.dna['ibidh'] for s in env.shrimp])/len(env.shrimp),1),end='\t')
    # print(sum([s.health for s in env.shrimp])/len(env.shrimp))
    # print('------')
    print()
