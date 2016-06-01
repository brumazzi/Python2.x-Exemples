#!/usr/bin/env python
#*-* coding:utf-8 *-*

import turtle

faces = input("Faces: ")
wn = turtle.Screen()
wn.bgcolor("black");
wn.title("circle");

point = turtle.Turtle()
point.pensize(1)
point.speed(10)

#point.position(180, 180)
colors = ["yellow","red","purple","blue","green","orange","pink"]
point.color(colors[4])


for x in range(len(colors)):
    point.color(colors[x])
    for y in range(18):
        for z in range(faces):
            point.forward((x+1)*20)
            point.left(360/faces)
        point.left(20)

point.penup()
point.goto(-1000,-1000)
import time as t

turtle.done()
