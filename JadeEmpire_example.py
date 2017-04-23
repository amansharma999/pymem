import pymem
from time import sleep
jadeHandle = pymem.openProcName("JadeEmpire.exe")
#cheataddr section

#bases
baseptr = 0x0076C924
baseOffset = [0xA0,0x0,0x0]

#offsetLists
xOffset = baseOffset[:]
xOffset.append(0x44) #float
yOffset = baseOffset[:]
yOffset.append(0x48) #float
zOffset = baseOffset[:]
zOffset.append(0x4c) #float
#end cheataddr

#resolve ptr's
def resolvePtrs():
	x_p = pymem.resolvePointer(jadeHandle, baseptr, xOffset)
	y_p = pymem.resolvePointer(jadeHandle, baseptr, yOffset)
	z_p = pymem.resolvePointer(jadeHandle, baseptr, zOffset)
	return (x_p,y_p,z_p)
#end

history = []
ptrs_list = resolvePtrs()
print("Recording player movement for 20 seconds")
for i in range(2000):
	x = pymem.readFloat(jadeHandle, ptrs_list[0])
	y = pymem.readFloat(jadeHandle, ptrs_list[1])
	z = pymem.readFloat(jadeHandle, ptrs_list[2])
	history.append((x,y,z))
	sleep(0.01)

print("Playing movement back")
for hist in reversed(history):
	pymem.writeFloat(jadeHandle, ptrs_list[0],hist[0])
	pymem.writeFloat(jadeHandle, ptrs_list[1],hist[1])	
	pymem.writeFloat(jadeHandle, ptrs_list[2],hist[2])
	sleep(0.01)