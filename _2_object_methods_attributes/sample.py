
class Sample(object):
    """sample class"""
    def __init__(self) -> None:
        super().__init__()
        print("init")
        self.att1 = 1
        self.att2 = [1,2,3]
        self.att3 = "abc"

    def __call__(self):
        super().__call__()
        print("call")
        
    def __str__(self) -> str:
        
        return "AAAA"


a = Sample()
print(a.__dict__)
print(a.__dir__())
print(a.__doc__)
print(a.__getattribute__('att1'))
print(a.__module__)
print(a.__setattr__('att2',1))
print(a.__str__())
print(a)
# print(a())

