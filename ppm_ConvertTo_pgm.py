#
# Adithya Venkatesan, January 24, 2012
#
# Sobel Edge Detection
#
#   Input: ppm file
# Process: converts to grayscale
#  Output: pgm file
#
wlist=open('CapnShreemo.ppm','r').read().split()



width = wlist[1]
height =  wlist[2]
maxpixel = int(wlist[3])
print 'P2'
print str(width)+' '+str(height)
print str(maxpixel)

for x in range(4,int(width)*int(height)*3,3):
  print int(0.30*int(wlist[x]) + 0.59*int(wlist[x+1]) + 0.11*int(wlist[x+2]))
  
#
# end of file
#
# to run type in terminal: python lab11.py > MyComputer.pgm