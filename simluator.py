env = Environment(100, 80, .3, .1, 15, .05, .2)

for i in range(500):
    env.step()
    print(sum([s.base_health for s in env.shrimp])/100)
    print(sum([s.health for s in env.shrimp])/100)
    print('------')
