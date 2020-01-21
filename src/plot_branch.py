import numpy
import uproot
import matplotlib.pyplot as plt

file = uproot.open("/star/u/kabir/pwg/data/st_physics_18053099_raw_0000004.MuDst.root")

## Know the Tree contents, step by step:

print("=====================================================================")
print(file.keys())
#print(file["MuDst"].keys())
file["MuDst"].show()

print("=====================================================================")
#print(file["MuDst"]["FmsHit"].keys())
file["MuDst"]["FmsHit"].show()

print("=====================================================================")
file["MuDst"]["FmsHit"].show()

print("=====================================================================")
print(file["MuDst"]["FmsHit"]["FmsHit.mAdc"].array())

# adc = file["MuDst"]["FmsHit"]["FmsHit.mAdc"].array()
# print(len(adc))

adc = file["MuDst"]["FmsHit"]["FmsHit.mAdc"].array(entrystart=10, entrystop=2000)
print(len(adc))

#print(adc)
print(numpy.array(adc))
plt.hist(adc, 100, [-50, 50])  ##------------------> Eats up all memory
plt.show()


for arrays in file["MuDst"].iterate("FmsHit.mAdc"):
    print(arrays)
