#
# Adithya Venkatesan, January 24, 2012
#
# Sobel Edge Detection smoothing
#
#   Input: pgm file
# Process: smooths the picture
#  Output: pgm file
#
wlist=open('CapnShreemo.pgm','r').read().split()



width = int(wlist[1])
height =  int(wlist[2])
maxpixel = int(wlist[3])

#need to weight edges and write directions
# 1 2 1
# 2 4 2
# 1 2 1

dirw2 = [-width,width, -1, 1]
dirw1 = [-width-1,-width+1, width-1, width+1]
#up, down, left right

print 'P2'
print str(width)+' '+str(height)
print str(maxpixel)

for x in range(4,int(width)*int(height)):
  curpix = int(wlist[x])
  finalcurpix = 0
  breakboolean = False

  
  for y in dirw2:#weight of 2
    temppix = x+y
    if temppix < 4 or temppix > len(wlist)-1:
      print curpix
      breakboolean = True
      break
    finalcurpix+=2*int(wlist[temppix])
  if breakboolean == True:
    continue
  
  for y in dirw1:#weight of 1
    temppix = x+y
    if temppix < 4 or temppix > len(wlist)-1:
      print curpix
      breakboolean = True
      break
    finalcurpix+=int(wlist[temppix])
  if breakboolean == True:
    continue
    
    
  finalcurpix+=4*curpix
  finalcurpix = int(finalcurpix/16)
  print finalcurpix
  
  
#
# end of file
#
# to run type in terminal: python lab11.py > MyComputer.pgm