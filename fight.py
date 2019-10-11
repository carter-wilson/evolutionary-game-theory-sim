def fight(posseser, intruder):
    pbid = posseser.pos_bid(intruder.int_display)
    ibid = intruder.int_bid(posseser.pos_display)
    if pbid > ibid:
      return posseser, intruder
    else:
      return intruder, posseser
