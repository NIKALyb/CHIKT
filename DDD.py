#connect library
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import mcpi.block as block
import time
#variable
d = 10
d1 = 11
d2 = 5
def CreateChikibamboni():
    pos = mc.player.getPos()
    x = round(pos.x)+d
    y = round(pos.y)+5
    z = round(pos.z)+d
    mc.setBlocks(x,y,z,x+d1,y+d2,z+d2,46)#tors
    mc.setBlocks(x,y,z,x+1,y-4,z+1,35)#legFR
    mc.setBlocks(x+10,y,z,x+11,y-4,z+1,35)#legRR
    mc.setBlocks(x,y,z+4,x+1,y-4,z+5,35)#legFL
    mc.setBlocks(x+10,y,z+4,x+11,y-4,z+5,35)#legRL
    mc.setBlock(x,y+3,z+1,57)
    mc.setBlock(x,y+3,z+4,57)
    mc.setBlocks(x,y+1,z+1,x,y+1,z+4,152)
    
CreateChikibamboni()
