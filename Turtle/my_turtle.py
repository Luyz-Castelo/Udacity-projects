import turtle

BLACK = (0, 0, 0)
BROWN = (210, 105, 30)
LIGHT_YELLOW = (255,255,224)

def change_turtle(shape='turtle', color=BLACK, speed=2, pensize_width=2):
  turtle.shape(shape)
  turtle.color(color)
  turtle.speed(speed)
  turtle.pensize(pensize_width)

def go_to_position(x: float, y: float):
  turtle.hideturtle()
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  turtle.showturtle()

def draw_to_position(x: float, y: float):
  turtle.goto(x, y)

def draw_carthesian_plane(x: int, y: int):
  draw_to_position(x, y)
  draw_to_position(-x, y)
  go_to_position(0,0)
  draw_to_position(y, x)
  draw_to_position(y, -x)

def draw_house():
  change_turtle(speed=2)

  # draw square

  go_to_position(-150, 0)

  turtle.fillcolor(LIGHT_YELLOW)

  turtle.begin_fill()

  draw_to_position(-150, 150)
  draw_to_position(150, 150)
  draw_to_position(150,-150)
  draw_to_position(-150,-150)
  draw_to_position(-150, 0)

  turtle.end_fill()

  for i in range(5):
    go_to_position(-150, -30*i)
    draw_to_position(150, -30*i)

  for i in range(5):
    go_to_position(-150, 30*i)
    draw_to_position(150, 30*i)

  # end draw square
  
  # draw door

  go_to_position(-40, -150)

  turtle.fillcolor(BROWN)
  
  turtle.begin_fill()

  draw_to_position(-40, -40)
  draw_to_position(40, -40)
  draw_to_position(40, -150)

  turtle.end_fill()

  # end draw door

  # draw roof

  go_to_position(-150, 151)

  turtle.fillcolor(BROWN)

  turtle.begin_fill()

  draw_to_position(0, 300)
  draw_to_position(150, 151)

  turtle.end_fill()

  # end draw roof

def draw_square():
  go_to_position(-150, 100)
  
  for _ in range(4):
    turtle.forward(300)
    turtle.right(90)
   
  turtle.hideturtle()  

def main():
  window = turtle.Screen()
  window.bgcolor('white')

  turtle.colormode(255)
  
  # draw_square()
  draw_house()

  window.exitonclick()

main()