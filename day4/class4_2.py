from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
number = 10
for i in range(8):
    for j in range(number):
        mc.spawnEntity(x,y,z,63)
    number = number * 2
    mc.postToChat("生成了"+str(number)+"FISH")