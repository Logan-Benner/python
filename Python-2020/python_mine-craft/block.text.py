from mcpi.minecraft import Minecraft
from mcpi import block	  

mc = Minecraft.create()

mc.postToChat("Hello world")
mc.postToChat("Here's your dirt")
x, y, z = mc.player.getTilePos()                                                  
#x, y, z = mc.player.getPos()

mc.setBlock(x+1, y, z, 3)
mc.setBlock(x+2, y, z, 3)
mc.setBlock(x+3, y, z, 3)
mc.setBlock(x+4, y, z, 3)
mc.setBlock(x+5, y, z, 3)
mc.setBlock(x+6, y, z, 3)
mc.setBlock(x+7, y, z, 3)
mc.setBlock(x+8, y, z, 3)
mc.setBlock(x+9, y, z, 3)
mc.setBlock(x+10, y, z, 3)
mc.setBlock(x+11, y, z, 3)
mc.setBlock(x+12, y, z, 3)
mc.setBlock(x+13, y, z, 3)
mc.setBlock(x+14, y, z, 3)
mc.setBlock(x+15, y, z, 3)
mc.setBlock(x+16, y, z, 3)
mc.setBlock(x+17, y, z, 3)
mc.setBlock(x+18, y, z, 3)
mc.setBlock(x+19, y, z, 3)
mc.postToChat("COAL_ORE")
mc.setBlock(x+20, y, z, 3)

#COAL_ORE             16
#WOOD                 17
#LEAVES               18
