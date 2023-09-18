#   a116_buggy_image_[BF].py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used


# this renames the turtle making it spider
spider = trtl.Turtle()
# Create a spider body
spider.pensize(40)
spider.circle(20)
# Configure spider legs
spider_legs = 4
spider_leg_length = 70
leg_distance  = 100 / spider_legs
spider.pensize(5)
counter = 0
#Draw legs
while (counter < spider_legs):
  spider.goto(0,20)
  spider.setheading(leg_distance *counter)
  spider.forward(spider_leg_length)
  counter = counter + 1

while(counter < 8):
  spider.goto(0,20)
  spider.setheading(leg_distance *counter - 260)
  spider.forward(spider_leg_length)
  counter = counter + 1
spider.penup()
spider.goto(20,20)
spider.pendown()
spider.pencolor("red")
spider.pensize(3)
spider.circle(8)
spider.
#hides the tutlre after the drawing is done 
spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()
