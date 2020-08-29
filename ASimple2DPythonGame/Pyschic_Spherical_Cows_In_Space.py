# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:45:46 2020

@author: CodeAndQuarks

Desc: A simple first person shooter, that randomises objects
      (Pyschic Spherical Cows), for a Space Explorer to defend against.
      Very Similar in functionality to Pong, the game ends once 
      the (Pyschic Spherical Cows) 'board' the 'ship', which is a collison.
------------------------------------------------------------------------------
      There are no sprites as such, but each 'character' is determined by 
      a basic shape. Pirates are circles, 
      and the Defending Explorer is a triangle, and shoots small square lasers.
------------------------------------------------------------------------------
      It's not quite the spherical cow in a vacuum routine but it does help
      provide the means to test a very simple physics engine.
"""
#imports
import turtle as trt
import time
import random as rd
import math as mt
#functions
def is_collided(t1,t2):
    distance=mt.sqrt(mt.pow(t1.xcor()-t2.xcor(), 2)+mt.pow(t1.ycor()-t2.ycor(), 2))
    if distance< 15:
        return True
    else:
        return False
def Fire_laser():
    global Laser_state
    if Laser_state=="ready":
        Laser_state="fire"
        #create laser
        x=player.xcor()
        y=player.ycor()+10
        Laser.setposition(x,y)
        Laser.showturtle()
def travel_up():
    y=player.ycor()
    y+=player_speed
    if y>280:
        y=280
    player.sety(y)    
def travel_down():
    y=player.ycor()
    y-=player_speed
    if y<-280:
        y=-280
    player.sety(y)
def travel_left():
    x=player.xcor()
    x-=player_speed
    if x<-280:
        x=-280
    player.setx(x)
def travel_right():
    x=player.xcor()
    x+=player_speed
    if x>280:
        x=280
    player.setx(x)

def rotate_ship():
    player.rt(90)
    Laser.rt(90)

delay=0.001
#
score=0
high_score=0

Laser_state="ready"
#screen
screen=trt.Screen()
screen.title("Pyschic Spherical Cows in Space by CodeAndQuarks")
screen.bgcolor("black")
screen.setup(width=750, height=700)
screen.tracer(0)
#barrier
barrier=trt.Turtle()
barrier.speed(0)
barrier.color("violet")
barrier.penup()
barrier.setposition(-300,-300)
barrier.pendown()
barrier.pensize(3)
for side in range(4):
   barrier.fd(600)
   barrier.lt(90)
barrier.hideturtle()
#create player
player=trt.Turtle()
player.color("green")
player.shape("triangle")
player.penup()
player.speed(0)
player.goto(0,0)
player.setheading(90)
#Laser
Laser=trt.Turtle()
Laser.color("green")
Laser.shape("square")
Laser.penup()
Laser.speed(0)
Laser.setheading(90)
Laser.shapesize(0.2,0.2)
Laser.hideturtle()
#create the game variables
enemies=[]
number_enemies=50
player_speed=20
enemy_speed_x=3
enemy_speed_y=-3
Laser_Speed=10

message="Start"
y_ranges=[(50, 250),(-250, -50)]
for i in range(number_enemies):
    enemies.append(trt.Turtle())
for enemy in enemies:
    enemy.color("white")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    dy1, dy2=rd.choice(y_ranges)
    x=rd.randint(-200, 200)
    y=rd.randint(dy1,dy2)
    enemy.goto(x,y)
    enemy.da=rd.randint(-7,7)

#score-board
pen=trt.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,310)
pen.write("Score: 0, High Score: 0",
          align="center", font=("Courier", 24, "normal"))
#Map directions to arrow keys
screen.listen()
screen.onkeypress(travel_up, "Up")
screen.onkeypress(travel_down, "Down")
screen.onkeypress(travel_left, "Left")
screen.onkeypress(travel_right, "Right")
screen.onkeypress(Fire_laser, "space")
screen.onkeypress(rotate_ship, "z")
while True:
    #There are better ways to do this, but I run before and after
    #Check all enemies positions against player position at loop start
    for E in enemies:
        if player.distance(E)<10:
            for E_obj in enemies:
                E_obj.goto(1000,1000)
                E_obj.clear()
            player.goto(0,0)
            Laser_state="ready"
            Laser.hideturtle()
            message="Game Over."
            score=0
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score,high_score),
                      align="center", font=("Courier", 24, "normal"))
            pen.goto(0,-350)
            pen.write("Game Over.", align="center", font=("Courier", 24, "normal"))
            break
    for enemy in enemies:
        enemy.rt(enemy.da*0.9)
        x=enemy.xcor()
        x+=enemy_speed_x
        enemy.setx(x)
        if enemy.xcor()>280:
            enemy_speed_x*=-1
            for e in enemies:
                x=e.xcor()
                y=e.ycor()
                x+=enemy_speed_x
                y+=enemy_speed_y
                e.setx(x)
                e.sety(y)
                if e.xcor()>280:
                    enemy_speed_x*=-1
                    e.setx(e.xcor()+enemy_speed_x)
                elif e.xcor()<-280:
                    enemy_speed_x*=-1
                    e.setx(e.xcor()+enemy_speed_x)
               
        if enemy.xcor()<-280:
            enemy_speed_x*=-1
            for e in enemies:
               x=e.xcor()
               y=e.ycor()
               x+=enemy_speed_x
               y+=enemy_speed_y
               e.setx(x)
               e.sety(y)
               if e.xcor()>280:
                   enemy_speed_x*=-1
                   e.setx(e.xcor()+enemy_speed_x)
               elif e.xcor()<-280:
                   enemy_speed_x*=-1
                   e.setx(e.xcor()+enemy_speed_x)
        if enemy.ycor()>280:
            enemy_speed_y*=-1
            for e in enemies:
                y=e.ycor()
                y+=enemy_speed_y
                e.sety(y)
                if e.ycor()>280:
                    enemy_speed_y*=-1
                    e.sety(e.ycor()+enemy_speed_y)
                elif e.ycor()<-280:
                    enemy_speed_y*=-1
                    e.sety(e.ycor()+enemy_speed_y)
        if enemy.ycor()<-280:
            enemy_speed_y*=-1
            for e in enemies:
                y=e.ycor()
                y+=enemy_speed_y
                e.sety(y)
                if e.ycor()>280:
                    enemy_speed_y*=-1
                    e.sety(e.ycor()+enemy_speed_y)
                elif e.ycor()<-280:
                    enemy_speed_y*=-1
                    e.sety(e.ycor()+enemy_speed_y)
        #check laser and enemy collsion
        if is_collided(Laser,enemy):
            #Reset laser
            Laser_state="ready"
            Laser.hideturtle()
            Laser.setposition(0,-400)
            dy1, dy2=rd.choice(y_ranges)
            x=rd.randint(-200, 200)
            y=rd.randint(dy1,dy2)
            enemy.goto(x,y)
             #increase score
            score+=10
            if score> high_score:
                high_score=score
                pen.clear()
                pen.write("Score: {} High Score: {}".format(score,high_score),
                          align="center", font=("Courier", 24, "normal"))
        if score>99999:
            message="Game Over."
            pen.goto(0,-350)
            pen.write("You win!!!, The Spherical Space Cows are defeated!",
                      align="center", font=("Courier", 24, "normal"))
            break
        if message=="Game Over.":
            break
        #move bullet
    if Laser_state=="fire":
        if Laser.heading()==90:
           y=Laser.ycor()
           y+=Laser_Speed
           Laser.sety(y)
        elif Laser.heading()==180:
           x=Laser.xcor()
           x-=Laser_Speed
           Laser.setx(x)
        elif Laser.heading()==270:
           y=Laser.ycor()
           y-=Laser_Speed
           Laser.sety(y)
        elif Laser.heading()==0:
           x=Laser.xcor()
           x+=Laser_Speed
           Laser.setx(x)
    #Check after movement
    for E in enemies:
        if player.distance(E)<10:
            for E_obj in enemies:
                E_obj.goto(1000,1000)
                E_obj.clear()
            player.goto(0,0)
            Laser_state="ready"
            Laser.hideturtle()
            message="Game Over."
            score=0
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score,high_score),
                      align="center", font=("Courier", 24, "normal"))
            pen.goto(0,-350)
            pen.write("Game Over.", align="center", font=("Courier", 24, "normal"))
            break
    if Laser.ycor()>275 or Laser.ycor()<-275:
        Laser_state="ready"
        Laser.hideturtle()
    if Laser.xcor()>275 or Laser.xcor()<-275:
        Laser_state="ready"
        Laser.hideturtle()
    #check after respawn
    for E in enemies:
        if player.distance(E)<10:
            for E_obj in enemies:
                E_obj.goto(1000,1000)
                E_obj.clear()
            player.goto(0,0)
            Laser_state="ready"
            Laser.hideturtle()
            message="Game Over."
            score=0
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score,high_score),
                      align="center", font=("Courier", 24, "normal"))
            pen.goto(0,-350)
            pen.write("Game Over.", align="center", font=("Courier", 24, "normal"))
            break
    if message=="Game Over.":
        print(message)
        break   
    time.sleep(delay)
    screen.update()
screen.exitonclick()
screen.mainloop()