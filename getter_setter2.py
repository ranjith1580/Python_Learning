class ranjith:
    name = str
    number = int
    def __init__(self, name, number):
        self.name = name
        self.number = number
        
    def getname(self):
        return self.name
        
    def getnumber(self):
        return self.number
        
obj1 = ranjith("ranjith", 9865878844)
obj2 = ranjith("ram", 8989898989)
obj3 = ranjith("sam", 7654321987)
print(ranjith.getnumber(obj1))
