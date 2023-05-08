import turtle
import math
import random
#two improvements I made were making the screen loop ie go off left come back on the right side and made it more fair so that no obstacles will spawn within 50 units of the spaceship
class SpaceCraft(turtle.Turtle):
    '''
    Purpose: A controllable spaceship object using turtle
    Instance variables: x and y position and velocity
    Methods: move, moves based on x and y velocity and gravity
    thrust: increases velocity in the direction spaceship is facing
    turnleft: turns left
    turnright:you'll never guess.... turns right
    '''

    def __init__(self, xp, yp, vx, vy):
        self.xposition = xp
        self.yposition = yp
        self.vx = vx
        self.vy = vy
        self.fuel = 50
        turtle.Turtle.__init__(self)
        self.left(90)
        self.speed(0)
        self.penup()
        self.setpos(xp, yp)
        self.turtlesize(2)
    def move(self):
        self.vy -= 0.0486
        self.xposition = self.xcor()+self.vx
        self.yposition = self.ycor() + self.vy
        if self.xcor() > 1000:
            self.xposition = 4
        if self.xcor()<2:
            self.xposition = 980
        self.setpos(self.xposition, self.yposition)
    def thrust(self):
        if self.fuel>0:
            self.fuel-=1
            angle= math.radians(self.heading())
            self.vx += math.cos(angle)
            self.vy += math.sin(angle)
            print(str(self.fuel)+' fuel remaining')
        else:
            print('Out Of Fuel (OOF)')
    def turnleft(self):
        if self.fuel>0:
            self.fuel-=1
            self.left(15)
            print(str(self.fuel)+' fuel remaining')
        else:
            print('Out Of Fuel (OOF)')
    def turnright(self):
        if self.fuel>0:
            self.fuel-=1
            self.right(15)
            print(str(self.fuel)+' fuel remaining')
        else:
            print('Out Of Fuel (OOF)')
class obstacle(turtle.Turtle):
    '''
    Purpose: Obstacle to be avoided
    Instance variables: x and y position
    Methods: move, moves the obstacle up, so that it is constantly coming at you. Once reaching the top of the screen it returns to the bottom
    '''
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.pencolor('deep sky blue')
        self.up()
        self.x = x
        self.y = y
        self.setpos(x,y)

    def move(self):
        if self.y<980:
            self.y = self.ycor() + 5

            self.setpos(self.x, self.y)
        else:
            self.y = 5
            self.setpos(self.x, self.y)
class Game:
    '''
    Purpose: Runs a game using spaceship
    Instance variables:NONE
    Methods: gameloop, loops the game until completion.
    '''

    def __init__(self):
        turtle.setworldcoordinates(0,0,1000,1000)
        turtle.delay(0)
        self.obstaclelist = []
        x = random.randint(100, 900)
        y = random.randint(500, 900)
        self.player = SpaceCraft(x, y, random.randint(-5, 5),
                                 random.randint(-5, 5))
        while len(self.obstaclelist)<13:
            newcoords = [random.randint(5, 995), random.randint(5, 995)]
            while abs(newcoords[0] - x)<50 or abs(newcoords[1] - y)<50:
                newcoords = [random.randint(5, 995), random.randint(5, 995)]
            newobst = obstacle(random.randint(5,995), random.randint(5,995))
            self.obstaclelist.append(newobst)
        self.gameloop()
        turtle.onkeypress(self.player.thrust, 'Up')
        turtle.onkeypress(self.player.turnleft, 'Left')
        turtle.onkeypress(self.player.turnright, 'Right')
        turtle.listen()
        turtle.mainloop()

    def gameloop(self):
        for i in self.obstaclelist:
            if abs(self.player.xcor() -i.xcor())<20:
                if abs(self.player.ycor() -i.ycor()) <20:
                    print('You Crashed!')
                    turtle.done()
        if self.player.ycor()>10:
            self.player.move()
            turtle.ontimer(self.gameloop, 30)
            for obstacle in self.obstaclelist:
                obstacle.move()
        if self.player.ycor()<10:
            if self.player.vy>4 or self.player.vx>4 or self.player.vy<-4 or self.player.vx<-4:
                print('You Crashed!')
                turtle.done()
            else:
                print('Successful landing!')
                turtle.done()
x = Game()
