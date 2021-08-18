class Human:
    def __init__(self, name, age):
        self.name= name
        self.age= age
    
    def introduce_self(self):
        return("Hi there, my name is %s and I am %s years old." % (self.name, self.age))
    

