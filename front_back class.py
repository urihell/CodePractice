class FrontBack():
    def __init__(self,string):
        self.string = string
        self.center = string[1:-1]
        self.last = string[-1]
        self.first = string[0]

    def front_back(self):
        if len(self.string) <= 1:
            print (self.string)
        else:
            print (self.last + self.center + self.first)