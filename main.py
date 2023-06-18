from point import Point
from route import Route

p1 = Point(120, "hello", "hello")
p2 = Point(150, "hello", "hello")
route1 = Route(p1, p2, 6, 25, "RN2")
print(route1.calculer_prix())