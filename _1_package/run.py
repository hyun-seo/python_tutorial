from moduleA import moduleAfun
import moduleA
import topPackage
from topPackage.subPackageA.objectA import ObjectA

ObjectA()
print(moduleAfun())



print(topPackage.__spec__)
# print(moduleA.__path__)
## error!
print(topPackage.__path__)