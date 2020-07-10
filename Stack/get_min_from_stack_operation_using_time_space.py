class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        #CODE HERE
        if len(self.s) == 0:
            self.s.append(x)
            self.minEle = x
            return
        if x > self.minEle:
            self.s.append(x)
        else:
            self.s.append(2 * x - self.minEle)
            self.minEle = x

    def pop(self):
        #CODE HERE
        if len(self.s) == 0:
            return -1
        top = self.s.pop(-1)
        if len(self.s) == 0:
            self.minEle = None
            return top
        if top > self.minEle:
            return top
        else:
            x = self.minEle
            self.minEle = 2 * self.minEle - top
            return x
        

    def getMin(self):
        #CODE HERE
        if self.minEle:
            return self.minEle
        return -1



obj = stack()
obj.push(2)
obj.push(3)
print(obj.pop())
print(obj.getMin())
