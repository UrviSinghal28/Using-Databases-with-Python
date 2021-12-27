#The primary purpose of the constructor is to set up some instance
# variable to have the proper initial values when obj is created.

class PartyAnimal:
    #attribute
    x=0
    name=""
    def __init__(self,z):
        self.name=z
        print('I am constructed')

    #method
    def party(self):
        self.x=self.x+1
        print(self.name,"party count",self.x)

    # def __del__(self):
    #     print('I am destructed',self.x)

#moment of construction
# an=PartyAnimal()

# #invoking of method within object
# an.party()
# an.party()

# an=42
# print('an contains',an)

s=PartyAnimal("Sally")
s.party()
j=PartyAnimal("Jim")
j.party()
s.party()
