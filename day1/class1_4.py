from mcpi.minecraft import Minecraft as mc
import time
mcs=mc.create()
x,y,z=mcs.player.getPos()
i=0
while i<5:
    mcs.player.setPos(x,y+ 100,z)
    time.sleep(0.5)
    y=y-1
    i=i=1