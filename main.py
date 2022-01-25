import turtle
from turtle import Vec2D
import time

trt = turtle.Turtle()
wn = turtle.Screen()

# wn.bgpic("toucan.gif")
wn.bgcolor("black")

trt.speed(0)

trt.ht()

# finds position of a point in order to make the Bézier curves easier
def buttonclick(x,y):
    print(f"({x}, {y})")

# defines the quadratic Bézier curve
def quadBeCurve(p0x, p0y, p1x, p1y, p2x, p2y):

  p0 = Vec2D(p0x, p0y)
  p1 = Vec2D(p1x, p1y)
  p2 = Vec2D(p2x, p2y)

  b = lambda t: p1 + (1 - t)**2 * (p0 - p1) + t**2 * (p2 - p1)

  trt.penup()

  trt.goto((p0x, p0y))

  trt.pendown()

  t = 0

  while t <= 1:
      position = b(t)

      trt.setheading(trt.towards(position))
      trt.goto(position)

      t += 0.05

# defines cubic Bézier curve
def cubeBeCurve(p0x, p0y, p1x, p1y, p2x, p2y, p3x, p3y):

  p0 = Vec2D(p0x, p0y)
  p1 = Vec2D(p1x, p1y)
  p2 = Vec2D(p2x, p2y)
  p3 = Vec2D(p3x, p3y)

  b = lambda t: (1 - t)**3 * p0 + 3 * (1 - t)**2 * t * p1 + 3 * (1 - t) * t**2 * p2 + t**3 * p3

  trt.penup()

  trt.goto((p0x, p0y))

  trt.pendown()

  t = 0

  while t <= 1:
      position = b(t)

      trt.setheading(trt.towards(position))
      trt.goto(position)

      t += 0.05

# "binds" butotnclick to the window
turtle.onscreenclick(buttonclick, 1)


# bottom of trunk
trt.color("gray")
quadBeCurve(-126, -34, -125, -38, -116, -42)
quadBeCurve(-115, -43, -105, -36, -90, -47)
quadBeCurve(-90, -46, -53, -47, -24, -61)
quadBeCurve(-24, -61, 19, -52, 43, -65)
quadBeCurve(43, -65, 75, -49, 115, -69)
quadBeCurve(115, -69, 121, -57, 131, -65)

trt.goto(130, -49)

quadBeCurve(130, -49, 74, -44, 104, -50)
quadBeCurve(93, -47, 82, -49, 75, -43)


# plant on right 
trt.color("lime green")
quadBeCurve(76, -45, 83, -54, 81, -62)
quadBeCurve(81, -62, 81, -53, 71, -45)
quadBeCurve(71, -45, 66, -50, 64, -45)
quadBeCurve(64, -45, 52, -38, 44, -41)
quadBeCurve(44, -41, 53, -34, 65, -41)
quadBeCurve(65, -41, 59, -30, 47, -31)

trt.penup()
trt.goto(65, -41)
trt.pendown()

quadBeCurve(65, -41, 65, -20, 47, -21)
quadBeCurve(65, -41, 68, -20, 46, -7)
quadBeCurve(65, -41, 76, -17, 55, 2)
quadBeCurve(68, -21, 67, -9, 75, -6)
quadBeCurve(75, -6, 71, -15, 74, -22)
quadBeCurve(74, -22, 76, -12, 83, -7)
quadBeCurve(83, -7, 81, -20, 76, -28)

trt.goto(76, -30)

cubeBeCurve(76, -30, 84, -23, 99, -21, 107, -17)
cubeBeCurve(107, -17, 101, -24, 85, -26, 79, -32)
quadBeCurve(79, -32, 89, -27,  106, -31)
quadBeCurve(106, -31, 86, -30, 78, -36)

trt.goto(82, -39)

cubeBeCurve(67, -33, 70, -18, 57, -8, 55, 1)
quadBeCurve(60, -22, 51, -18, 48, -13)
quadBeCurve(78, -36, 89, -40, 96, -45)
quadBeCurve(96, -45, 85, -38, 73, -42)


# top of trunk between plants
trt.color("gray")
trt.penup()
trt.goto(60, -43)
trt.pendown()
trt.goto(39, -45)

cubeBeCurve(39, -45, 23, -36, -7, -49, -18, -40)
quadBeCurve(-18, -40, -23, -38, -31, -39)
cubeBeCurve(-31, -39, -40, -45, -54, -34, -63, -32)
quadBeCurve(-63, -32, -69, -35, -75, -30)

trt.goto(-102, -22)


# plant on left
trt.color("lime green")
trt.goto(-105, -29)

trt.penup()
trt.goto(-111, -28)
trt.pendown()

quadBeCurve(-111, -28, -114, -7, -128, -5)
quadBeCurve(-128, -5, -115, -4, -110, -14)
quadBeCurve(-110, -14, -117, 8, -128, 15)
quadBeCurve(-128, 15, -111, 8, -109, -1)
quadBeCurve(-109, -1, -101, 21, -92, 21)

trt.goto(-97, 8)
trt.goto(-93, 10)
trt.goto(-100, -6)

quadBeCurve(-100, -6, -86, 5, -76, 4)

trt.goto(-93, -4)

quadBeCurve(-93, -4, -88, -4, -83, -6)
quadBeCurve(-83, -6, -99, -9, -100, -16)
quadBeCurve(-100, -16, -107, -31, -111, -28)

trt.goto(-105, -29)

#left corner of trunk after plant
trt.color("gray")
trt.penup()
trt.goto(-114, -19)
trt.pendown()
trt.goto(-129, -18)

trt.goto(-126, -34)


# bird !!!

# tail 
trt.color("white")
quadBeCurve(-50, -52, -54, -70, -46, -82)
trt.goto(-35, -82)
quadBeCurve(-35, -82, -29, -79, -32, -57)

# body
quadBeCurve(-54, -37, -58, -18, -51, -2)
quadBeCurve(-51, -2, -42, 34, -25, 30)
quadBeCurve(-34, -37, -23, -23, -24, -5)

# feet
trt.color("red")
quadBeCurve(-47, -38, -40, -34, -32, -39)
quadBeCurve(-32, -39, -39, -43, -47, -38)

# beak
trt.color("lawngreen")
quadBeCurve(-25, 30, 9, 29, 10, 6)
quadBeCurve(10, 6, 1, 15, -21, 13)
cubeBeCurve(-25, 30, -22, 24, -32, 18, -21, 13)

#line in middle of beak
trt.color("orange")
quadBeCurve(10, 6, -9, 22, -24, 24)

# red part on beak
trt.color("red")
quadBeCurve(2, 11, -2, 17, 6, 18)

# line under beak
trt.color("white")
trt.penup()
trt.goto(-20, 14)
trt.pendown()
trt.goto(-22, 8)

# chest
quadBeCurve(-23, -7, -18, 2, -22, 8)

# yellow part around eye
trt.color("gold")
quadBeCurve(-24, 28, -38, 28, -37, 17)

# yellow part on chest
cubeBeCurve(-37, 17, -62, -4, -16, -19, -23, 8)

# green part around eye
trt.color("lawngreen")
cubeBeCurve(-23, 27, -35, 28, -36, 18, -26, 20)

# eye
trt.color("white")
trt.penup()
trt.goto(-29, 23)
trt.dot()

trt.goto(37, 49)
trt.write("caw caw")