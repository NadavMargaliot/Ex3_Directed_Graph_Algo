import MyPoint3d

class MyNode:
    def __init__(self ,id :int ,tag : int = 0, location: tuple = None):
        self.id = id
        self.tag = tag;
        if location is not  None:
            self.location = location
        else:
            self.location = (0,0,0)
        self.info = ""
        self.neighbors = {}
        self.edges = {}


