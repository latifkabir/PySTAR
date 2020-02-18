import uproot
import math, numpy
import matplotlib.pyplot as plt

# Open any MuDst or PicoDst root file file
file = uproot.open("~/GIT/BrightSTAR/dst/R15RpStream/AnRunAnTreeMaker_16092065.root")
tree = file["T"]

histogram = None
itr = 0
entries = 0
count = 0

#for data in tree.iterate(["rpTrack.mEta", "rpTrack.mPhi"], namedecode="utf-8"):
for data in tree.iterate("rpTrack*", namedecode="utf-8", entrysteps=3000):  
    # operate on a batch of data in the loop
    eta = data["rpTrack.mEta"] # eta is an array of  3000 x n_tracks entries
    #print(eta)

    n_tracks = data["rpTrack"] #n_tracks is an array of  30000 entries
    # print(n_tracks)

    itr = itr + 1
    entries = entries + len(eta)
    print("Iteration: ", itr)
    print("Total events processed: ", entries)
      
    # accumulate results
    for event in range(0, len(eta)):
        #print(eta[event])
        #You can loop over individual track as follows:
        #But it is preferred that you rather perform column by column operations to take advantage of the speed.   
        # for trk in range(0, n_tracks[event]):
        #     print("Track: ", trk, " eta: ", eta[event][trk])

        counts, edges = numpy.histogram(eta[event], bins=200, range=(-10, 10))

        if histogram is None:
            histogram = counts, edges
        else:
            histogram = histogram[0] + counts, edges
        
counts, edges = histogram
        
plt.step(x=edges, y=numpy.append(counts, 0), where="post")
plt.xlim(edges[0], edges[-1])
plt.ylim(0, counts.max() * 1.1)
plt.xlabel("eta")
plt.ylabel("events per bin")      

plt.show()
