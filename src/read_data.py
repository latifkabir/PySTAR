# Filename: read_data.py
# Description: 
# Author: Latif Kabir < kabir@bnl.gov >
# Created: Sun Jul 28 01:17:51 2019 (-0400)
# URL: jlab.org/~latif

import uproot
import matplotlib.pyplot as plt
import math, numpy

# Open any MuDst or PicoDst root file file
file = uproot.open("~/pwg/data/st_physics_15132017_raw_4500063.picoDst.root")

# Show Trees
k = file.keys()
print(k)
# Get trees
t = file["PicoDst"]

#Show branches of the tree
k = t.allkeys()
print(k)

#Get specific branch
#  You could also directly get the branch by doing: b = file["picoDst"]["Event"]["Event.mRunId"]
br = t["Event.mRunId"]
#Get branch entries as array
# ALternative option is: 
# print(file["PicoDst"].array("Event.mRunId"))
arr = br.array() 
print(arr)

p_x = file["PicoDst"]["Track"]["Track.mPMomentumX"].array()
p_y = file["PicoDst"]["Track"]["Track.mPMomentumY"].array()
p_z = file["PicoDst"]["Track"]["Track.mPMomentumZ"].array()

print(p_x, "\t", p_y, "\t", p_z)

#plt.hist(numpy.array(p_x))
#plt.show()

