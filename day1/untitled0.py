from mcpi.minecraft import Minecraft as mc
mcs=mc.create()    
print(mcs.player.getTilePos())
mcs.player.setTilePos(200-100,100,200)