class func:
    def __init__(self):
        self.s = ""
    
    def getstring(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())
    
pr = func()
pr.getstring()
pr.printString()