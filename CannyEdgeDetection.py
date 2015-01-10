#
# Adithya Venkatesan, January 24, 2012g
#
# Canny Edge Detection smoothing
#
#   Input: pgm file
# Process: finds edges of the smoothed picture
#  Output: ppm file with edges in black sharp edges
#
import math



def round45(angle):
  lastsmallest = 0
  for a in range(0, 360, 45):
    if (math.fabs(angle - lastsmallest)) > (math.fabs(angle - a)):
      lastsmallest = a
    else:
      break
  return lastsmallest

def floodfill(place,ang):
  global identpixels
  global width
  global wlist
  if place < 3+width or place > len(wlist)-width or (place%width)==0 or ((place+1)%width)==0:
    return
  dirs = [-width-1, -width, -width+1, 1, width+1, width, width-1, -1]
  dirs2=[1, -width+1, -width, -width-1, -1, width+1,  width, width-1] #angle/45 -> pos of arr, (+-2)%8 gives two perp dirs
  ang/=45
  lookindirs = [dirs2[(ang+2)%8], dirs2[(ang-2)%8] ]
  othlookindirs = [ dirs2[(ang)%8], dirs2[(ang+4)%8] ]

  gx = 0#horizontal weights
  gy = 0#vertical weights
  for y in range(0,8):#weight of 2
    breakboolean = False
    temppix = place+dirs[y]
    if temppix < 4 or temppix > len(wlist)-1:
      breakboolean = True
      break
    gx+=hweights[y]*int(wlist[temppix])
    gy+=vweights[y]*int(wlist[temppix])
    if breakboolean == True:
      continue
    mesumma = int(math.fabs(gx)) + int(math.fabs(gx))
  
  
  for d in lookindirs:
    tffv = d+place
    
    if tffv < 4 or tffv > len(wlist)-1:
      break
    
    gx = 0#horizontal weights
    gy = 0#vertical weights
    
    for y in range(0,8):#weight of 2
      breakboolean = False
      temppix = tffv+dirs[y]
      if temppix < 4 or temppix > len(wlist)-1:
	breakboolean = True
	break
      gx+=hweights[y]*int(wlist[temppix])
      gy+=vweights[y]*int(wlist[temppix])
    if breakboolean == True:
      return
    if gx == 0:
      tangle = 0
    else:
      tangle = round45(math.degrees((math.atan2(int((math.fabs(gy))), int(math.fabs(gx))))))
    gsum = int(math.fabs(gx)) + int(math.fabs(gx))
    if gsum < 10: # high threshold: 250, low threshold: 100
      continue
    if x not in identpixels:
      identpixels.append(x)
      floodfill(tffv, tangle)
      
   #
   #for nonmaximum surpression
   #
  for d in othlookindirs:
    tffv = d+place
    
    if tffv < 4 or tffv > len(wlist)-1:
      break
    
    gx = 0#horizontal weights
    gy = 0#vertical weights
    
    for y in range(0,8):#weight of 2
      breakboolean = False
      temppix = tffv+dirs[y]
      if temppix < 4 or temppix > len(wlist)-1:
	breakboolean = True
	break
      gx+=hweights[y]*int(wlist[temppix])
      gy+=vweights[y]*int(wlist[temppix])
    if breakboolean == True:
      return
    if gx == 0:
      tangle = 0
    else:
      tangle = round45(math.degrees((math.atan2(int((math.fabs(gy))), int(math.fabs(gx))))))
    gsum = int(math.fabs(gx)) + int(math.fabs(gx))
    if gsum > mesumma: # high threshold: 250, low threshold: 100
      identpixels.remove(place)
      break

  

identpixels = []

wlist=open('CapnShreemosmooth.pgm','r').read().split()

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
  if gx == 0:
    angle = 0
  else:
    angle = round45(math.degrees((math.atan2(int((math.fabs(gy))), int(math.fabs(gx))))))
  gsum = int(math.fabs(gx)) + int(math.fabs(gx))
  if gsum < 250: # high threshold: 250, low threshold: 100
    continue
  identpixels.append(x)
  floodfill(x,angle)
  
print 'P3'
print str(width)+' '+str(height)
print str(maxpixel)
identpixels.sort()
curidpix = 0
for integerzzz in range(4,len(wlist)):
  if integerzzz == identpixels[curidpix]:
    print str(0) + ' ' + str(0) + ' ' + str(0)
    if not( curidpix+1 == len(identpixels)):
      curidpix+=1
  else:
    print str(255) + ' ' + str(255) + ' ' + str(255)
