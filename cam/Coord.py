class Coordinate:
    x: float
    y: float

    def __init__(self,x:float,y:float):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'
    
    def get_coords(self):
        return [self.x, self.y]
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
