import math
def area_of_triangle(x, y, z):
  p=(x+y+z)/2
  area = math.sqrt(p*(p-x)*(p-y)*(p-z))
  print("Area of the triangle: ", area)


print("Please, enter the three sides of a triangle,")
a=float(input('a = '))
b=float(input('b = '))
c=float(input('c = '))

area_of_triangle(a, b, c)