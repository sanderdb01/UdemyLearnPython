class Name:
    #constructor method (not function because it is in a class def) - instantiation
    #usually the attributes have to be defined before the constructor, but not in python
    def __init__(self, first, middle, last):
        self.first = first
        self.middle = middle
        self.last = last
        
    #to-string method (allows for us to print the object and control what is returned eg. print(myName))
    def __str__(self):
        return self.first + ' ' + self.middle + ' ' + self.last
    
    def lastFirst(self):
        return self.last + ', ' + self.first + ' ' + self.middle
        
    def initials(self):
        return self.first[0] + self.middle[0] + self.last[0]

aName = Name("Mary", "Liz", "Smith")
print(aName)
print("aName is: " + str(aName))
print(aName.lastFirst())
print(aName.initials())
