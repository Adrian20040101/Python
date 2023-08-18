from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


@dataclass(order=True)
class circle:
    c: Point
    r: float

    def move(self, dx, dy): pass

    def area(self): pass

   # def __lt__(self, other): pass
