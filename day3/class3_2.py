from mcpi.minecraft import Minecraft 
mc=Minecraft.create()
import random
import time
mc = Minecraft. create()
x,y,z = mc.player.getPos()
while True:
    time. sleep(1)
    x = x+random.uniform(-20,20) #random.randint()
    y = x+random.uniform(-20,20)
    z = x+random.uniform(-20,20)
    mc.spawnEntity(x,y,z,64)


