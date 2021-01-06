# from topPackage.subPackageA.baseA import BaseA
from .baseA import BaseA
from ..subPackageB.baseB import BaseB

class ObjectA(BaseA):
    def __init__(self) -> None:
        super().__init__()
        print("init ObjectA which is child class of BaseA")
        print(BaseB())
if __name__ == "__main__":
    
    objA = ObjectA()
    print(objA)