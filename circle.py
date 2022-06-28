
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """The radius property."""
        print("Get radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Set radius")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("Delete radius")
        del self._radius
        
    def __str__(self):
        return str(self.radius)
    
    
c = Circle(2)
print(c)
c.radius = 9
print(c.__init__)

print(c)

