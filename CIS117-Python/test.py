class Point:
    'class that represents a point on the coordinate plane'
    def __init__(self, xcoord=0, ycoord=0):
        'initialize coordinates to (xcoord, ycoord)'
        self.x = xcoord
        self.y = ycoord
        
    def setx(self, xcoord):
        'set x coordinate to point'
        self.x = xcoord
        
    def sety(self, ycoord):
        self.y = ycoord
        
    def get(self):
        'return tuple with coordinates'
        return(self.x, self.y)
    
    def move(self,dx,dy):
        self.x += dx
        self.y += dy
        
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    def __str__(self):
        'return a string representation of the point'
        return f"({self.x}, {self.y})"
        
x = Point()
a = Point(5,6)
b = Point(1,2)

c = a + b
print(c)