
class StringClass:
    def __init__(self,estr):
        self.str=estr

    def getlen(self):
        print(len(self.str))

    def aslist(self):
        li=list(self.str)
        print(li)

obj1=StringClass('12314532')
obj1.getlen()
obj1.aslist()