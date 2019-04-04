
class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromPoint(self,point):
        return ((self.x) - (point))

    def reflect(self):
        return (self.x, (self.y- (self.y*2)))


    def slope_from_origin(self):
        if self.x == 0:
           return None
        else:
           return self.y / self.x

    def get_line_to_point(self, posX, posY):
        x = posX - self.x
        b = posX/x
        return x, b


print(Point(4,10).get_line_to_point(6,15))


