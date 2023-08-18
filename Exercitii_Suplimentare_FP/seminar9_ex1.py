import math

#ex1
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return math.sort((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __st__(self):
        return f'Point ( x = {self.x}, y = {self.y}'

class Circle:
    def __init__(self, x, y, r):
        self.c = Point(x, y)
        self.r = r

    def move(self, dx, dy):
        self.c.y += dx
        self.c.y += dy

    def area(self): return math.pi * self.r **2

    def __lt__(self, other):
        return self.area() < other.area()

def sort_c1(Pc):
    Pc.sort(key = lambda c : c.area())
    #list(map(Pc, lambda c : c. area()).sort()
    #Pc.sort() -> functioneaza doar daca este implementata metoda __lt__

def sort_c2(Pc):
    return sorted(Pc, key = lambda c : c.area())

def main():
    p1 = Point(1, 2)
    p2 = Point(2, 5)
    d = p1 - p2
    print (d)
    print (p2)
    k = [Circle(1, 2, p2), Circle(1, 5, 7), Circle(1, 1, 3)]
    sort_c1(p1)
    for c in p1: print (c)
    cn = sort_c2(p2)
    for c in p2: print (c)


