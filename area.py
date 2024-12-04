squarearea=lambda side:side**2
Rectanglearea=lambda length,width:length*width
Trianglearea=lambda base,height:0.5*base*height
side=float(input("Enter side of square:"))
length=float(input("Enter length of Rectangle:"))
width=float(input("Enter width of Rectangle:"))
base=float(input("Enter base of Triangle:"))
height=float(input("Enter height of Triangle:"))
print("Area of square:",squarearea(side))
print("Area of Rectangle:",Rectanglearea(length,width))
print("Area of triangle:",Trianglearea(base,height))

