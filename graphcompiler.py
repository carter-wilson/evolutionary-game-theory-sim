import json
import grapher

file = 'goodsave{}.json'

for i in range(10):
    print(i)
    save = json.load(open(file.format(i)))
    print(min(save['biddif']))
    print(sum(save['biddif'])/len(save['biddif']))
    print(max(save['biddif']))
    grapher.multi(save)
    input('>')
