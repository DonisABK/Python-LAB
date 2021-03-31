import circle

from rectangle import *
from Graphics._3D_graphics import cuboid,sphere

l=float(input('Enter length of rectangle : '))
b=float(input('Enter breadth of rectangle : '))
perimeter(a,b)

r=float(input('Enter the radius of circle : '))
circle.circumference(r)

lc=float(input('Enter length of cuboid : '))
bc=float(input('Enter breadth of cuboid : '))
hc=float(input('Enter height of cuboid : '))
cuboid.perimeter(lc,bc,hc)

r=float(input('Enter the radius of sphere : '))
sphere.perimeter(r)