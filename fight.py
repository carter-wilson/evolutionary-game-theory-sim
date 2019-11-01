def fight(posseser, intruder):
    id = intruder.int_display()
    pbid = posseser.pos_bid(id)
    pd = posseser.pos_display()
    ibid = intruder.int_bid(pd)
    # print(round(pd,1), round(id,1), round(pbid,1), round(ibid,1), sep='\t\t\t')
    posseser.base_health -= min(pbid,ibid)
    posseser.health = min(posseser.health, posseser.base_health)
    intruder.base_health -= min(pbid,ibid)
    intruder.health = min(intruder.health, intruder.base_health)
    if pbid > ibid:
      return posseser, intruder
    else:
      return intruder, posseser
