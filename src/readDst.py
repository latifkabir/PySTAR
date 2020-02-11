
import uproot
import matplotlib.pyplot as plt
import math, numpy

# Open any MuDst or PicoDst root file file
file = uproot.open("~/GIT/BrightSTAR/dst/R15RpStream/AnRunAnTreeMaker_16092065.root")
tree = file["T"]

eta_ = tree["rpTrack"]["rpTrack.mEta"].lazyarray(entrysteps=500)
eta = numpy.array(eta_)
print(eta)

plt.hist(eta, bins=50, range=(-10, 10))
plt.show()

