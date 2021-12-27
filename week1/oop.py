#class= a template
#method or message= a defined capability of a class
#field or attribute= a bit of data in a class
#object or instance= a particular instance of a class
class PartyAnimal:
    #attribute
    x=0

    #method
    def party(self):
        self.x=self.x+1
        print("So far",self.x)

#moment of construction
an=PartyAnimal()

#invoking of method within object
an.party()
an.party()
an.party() 

#dir() lists the capabilities

print('Type', type(an))
print('Dir:',dir(an ))