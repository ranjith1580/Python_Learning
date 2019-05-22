class ram:
    name = str
    num = int
    dep = str
 
    def getname(self):
        return self.name
        
    def getnum(self):
        return self.num
        
    def getdep(self):
        return self.dep
        
    def setname(self, name):
        self.name = name
        
    def setnum(self, num):
        self.num = num
        
    def setdep(self, dep):
        self.dep = dep
        
f = open('file.txt','r')
lis = []
for line in f:
    if "start" in line:
        obj = ram()
    if "name" in line:
        obj.setname(line)
    if "num" in line:
        obj.setnum(line)
    if "dep" in line:
        obj.setdep(line)
    if "end" in line:
        lis.append(obj)
        
for obj in lis:
    print(ram.getname(obj))
    print(ram.getnum(obj))
    print(ram.getdep(obj))
