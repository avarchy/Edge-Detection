#
# Adithya Venkatesan, January 24, 2012
#
# Sobel Edge Detection smoothing
#
#   Input: pgm file
# Process: finds edges of the smoothed picture
#  Output: ppm file with edges in red
#
import math

wlist=open('MyComputersmooth.pgm','r').read().split()



width = int(wlist[1])
height =  int(wlist[2])
maxpixel = int(wlist[3])

#need to weight edges and write directions
# 1 2 1
# 2 4 2
# 1 2 1

hweights = [-1, 0, 1, 2, 1, 0, -1, -2]
vweights = [1, 2, 1, 0, -1, -2, -1, 0]
dirs = [-width-1, -width, -width+1, 1, width+1, width, width-1, -1]
#up, down, left right

print 'P3'
print str(width)+' '+str(height)
print str(maxpixel)

for x in range(4,int(width)*int(height)):
  curpix = int(wlist[x])
  finalcurpix = 0
  breakboolean = False
  
  gx = 0#horizontal weights
  gy = 0#vertical weights
  
  for y in range(0,8):#weight of 2
    temppix = x+dirs[y]
    if temppix < 4 or temppix > len(wlist)-1:
      print str(curpix) + ' ' + str(curpix) + ' ' + str(curpix)
      breakboolean = True
      break
    gx+=hweights[y]*int(wlist[temppix])
    gy+=vweights[y]*int(wlist[temppix])
  if breakboolean == True:
    continue
  
  gsum = int(math.fabs(gx)) + int(math.fabs(gx))
  if gsum > 150:
    print str(255) + ' ' + str(0) + ' ' + str(0)
  else:
    print str(curpix) + ' ' + str(curpix) + ' ' + str(curpix)
  
    
  
  
#
# end of file
#
# to run type in terminal: python lab11.py > MyComputer.pgm