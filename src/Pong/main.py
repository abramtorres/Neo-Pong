import turtle
from random import randint
wn=turtle.Screen()
wn.bgcolor("pink")
wn.setup(width=850,height=650)
wn.tracer(1)
#data
colorarray=["yellow","blue","orange","green","brown","pink"]
#score
scorea=0
scoreb=0
score=turtle.Turtle()
score.penup()
score.hideturtle()
score.color("blue")
score.sety(156)
score.write("score A:0 score B:0",align="center",font=("courier",15,"normal"))
#paddlea{}
paddlea=turtle.Turtle()
paddlea.speed(3)
paddlea.shape("square")
paddlea.color("pink","blue")
paddlea.shapesize(stretch_len=1,stretch_wid=25)
paddlea.penup()
paddlea.goto(-340,6)
#paddleb{}
paddleb=turtle.Turtle()
paddleb.speed(3)
paddleb.shape("square")
paddleb.color("red", "green")
paddleb.shapesize(stretch_len=1,stretch_wid=25)
paddleb.penup()
paddleb.goto(350,0)
#ball{}
ball=turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("orange")
ball.penup()
ball.goto(10,60)
ball.dx = 5
ball.dy = 2
#padlle a movement 
def paddle_a_up():
    y=paddlea.ycor()
    y += 21
    paddlea.sety(y)
def paddle_a_down():
    y=paddlea.ycor()
    y -= 21
    paddlea.sety(y)
def paddle_b_down():
    y=paddleb.ycor()
    y -= 21
    paddleb.sety(y)
def paddle_b_up():
    y=paddleb.ycor()
    y += 21
    paddleb.sety(y)
#keyboard binding
wn.listen()
wn.onkey(paddle_a_up,"w")
wn.onkey(paddle_a_down,"s")
wn.onkey(paddle_b_up,"Up")
wn.onkey(paddle_b_down,"Down")
# Main game loop
while "true" and scorea<=5 and scoreb<=5:
    wn.update()
    #move the ball
    ball.setx(ball.xcor()-ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #border checking 
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy = ball.dy* (-1)
        ball.color(colorarray[randint(0,4)])

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy* (-1)
        ball.color(colorarray[randint(0,4)])

    if ball.xcor() > 290:
        score.clear()
        scoreb +=1
        score.write("score Epic A:{} score  Epic B:{}".format(scorea,scoreb),align="center",font=("futura",24,"normal"))
        ball.goto(0,0)
        ball.dx=ball.dx*(1)
    if ball.xcor() < -390:
        score.clear()
        scorea +=1
        score.write("score A:{} score B:{}".format(scorea,scoreb),align="center",font=("futura",24,"normal"))
        ball.goto(1,150)
        ball.dx=ball.dx*(-1)
    #ball and paddle collisions
    if ball.xcor()==-292 and ball.ycor()>paddlea.ycor()-50 and ball.ycor()<paddlea.ycor()+50:
        ball.dx=ball.dx*(-1)
        ball.color(colorarray[randint(1,6)])
       
    if ball.xcor()==292 and ball.ycor()>paddleb.ycor()-40 and ball.ycor()<paddleb.ycor()+40:
        ball.dx=ball.dx*(-1)
        ball.color(colorarray[randint(0,4)])
