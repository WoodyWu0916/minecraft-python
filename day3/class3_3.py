from mcpi.minecraft import Minecraft 
mc=Minecraft.create()
x,y,z = mc.player.getPos()
for i in range (60):
    mc.setBlock(x+i,y-i,z+i,1)