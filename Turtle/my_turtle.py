import turtle

def draw_square():
  square_maker = turtle.Turtle()
  square_maker.shape('turtle')
  square_maker.color("green")
  square_maker.speed(100)

  i = 0
  while i < 100:
    square_maker.right(2)
    square_maker.forward(200)
    square_maker.right(90)
    i += 1
  square_maker.hideturtle()  

def main():
  window = turtle.Screen()
  window.bgcolor("black")

  draw_square()

  window.exitonclick()

main()