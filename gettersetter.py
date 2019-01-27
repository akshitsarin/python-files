# getter and setter

class A():
    def __init__(self, name):
        self.name = name
    def setter(self,name):  # setting value
        self.name = name
    def getter(self):       # getting value
        print "name is ",self.name

obj = A("Hadoop")
obj.getter()

obj.setter("python")
obj.getter()
