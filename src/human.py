class Human:
    def __init__(self, name, age):
        self.name= name
        self.age= age
        self.pocket= 0
    
    def introduce_self(self):
        print("Hi there, my name is %s and I am %s years old." % (self.name, self.age))
    
    def found_change(self, amount:"float"):
        self.pocket += amount

    def on_hand(self):
        """Returns how much money user has in wallet
        """
        return "$%s" % (self.pocket)
