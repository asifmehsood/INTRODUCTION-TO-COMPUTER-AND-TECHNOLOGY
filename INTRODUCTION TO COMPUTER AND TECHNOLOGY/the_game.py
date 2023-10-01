from cgitb import text
import turtle
def one():
    print("ggg")
wind = turtle.Screen() #الي يشغل الشاشة
wind.title("bing bong game") # العنوان
wind.bgcolor("white") # لون الخلفية
wind.setup(width=800 , height=600) # المقاسات
wind.tracer(0) #الي يمنعها من التحديث

ping1 = turtle.Turtle()
ping1.shape("square")
ping1.color("blue")
ping1.penup()
ping1.goto(-350,0)
ping1.shapesize(stretch_wid=5,stretch_len=1)

ping2 = turtle.Turtle()
ping2.shape("square")
ping2.color("red")
ping2.penup()
ping2.goto(350,0)
ping2.shapesize(stretch_wid=5,stretch_len=1)

ball = turtle.Turtle()
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0,0)
x=.1
y=.1
def ping_movement(upordown,oneortwo):
    if(oneortwo == 1):
        if(upordown=="w"):
            y = ping1.ycor()
            y += 20
            ping1.sety(y)
        elif (upordown=="s"):
            y = ping1.ycor()
            y -= 20
            ping1.sety(y)

    elif(oneortwo == 2):
        if(upordown=="w"):
            y = ping2.ycor()
            y += 20
            ping2.sety(y)
        elif (upordown=="s"):
            y = ping2.ycor()
            y -= 20
            ping2.sety(y)

wind.listen()
wind.onkeypress(lambda: ping_movement("w",1),"w")
wind.onkeypress(lambda: ping_movement("s",1),"s")
wind.listen()
wind.onkeypress(lambda: ping_movement("w",2),"Up")
wind.onkeypress(lambda: ping_movement("s",2),"Down")


canvas = wind.getcanvas() 
root = canvas.winfo_toplevel()
def to_main_windowe():
    wind.bye()
    
    
root.protocol("WM_DELETE_WINDOW",to_main_windowe)
while True:
    wind.update()

    ball.setx(ball.xcor() + x)
    ball.sety(ball.ycor() + y)
    if(ball.ycor()>290):
        ball.sety(290)
        y *= -1 
    elif(ball.ycor()<-290):
        ball.sety(-290)
        y *= -1 
    if(ball.xcor()>390):
        ball.goto(0,0)
        x*=-1
    elif(ball.xcor()<-390):
        ball.goto(0,0)    
        x*=-1

    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < ping2.ycor() + 40 and ball.ycor() > ping2.ycor() - 40 ):
        print(ball.xcor())
        x *= -1
    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < ping1.ycor() + 40 and ball.ycor() > ping1.ycor() - 40 ):
        print(ball.xcor())
        x *= -1
