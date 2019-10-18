def fight(posseser, intruder):
    pbid = posseser.pos_bid(intruder.int_display())
    ibid = intruder.int_bid(posseser.pos_display())
    posseser.base_health -= min(pbid,ibid)
    posseser.health = min(posseser.health, posseser.base_health)
    intruder.base_health -= min(pbid,ibid)
    intruder.health = min(intruder.health, intruder.base_health)
    if pbid > ibid:
      return posseser, intruder
    else:
      return intruder, posseser
