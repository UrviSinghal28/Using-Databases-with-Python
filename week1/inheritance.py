# Class: a template
# Attribute: a variable within a class
# Method: a function within a class
# Object: a particular instance of a class
# Constructor: code that runs when an object is created
# Inheritance: the ability to extend a class to make a new class

class PartyAnimal:
    #attribute
    x=0
    name=""
    def __init__(self,nam):
        self.name=nam
        print(self.name,"constructed")

    #method
    def party(self):
        self.x=self.x+1
        print(self.name,"party count",self.x)

class FootballFan(PartyAnimal):
    points=0
    def touchdown(self):
        self.points+=7
        self.party()
        print(self.name,"points",self.points)

s=PartyAnimal("Sally")
s.party()

j=FootballFan('Jim')
j.party()
j.touchdown()