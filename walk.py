from turtle import * 
import random

def randomWalk(t, turns, distance = 20):
	"""Rotates random  number of degress and moves a given distance for a fixed number of turns"""
	for x in range(turns):
		t.left(random.randint(0, 360))
		colormode(255)
		t.pencolor(random.randint(0,255),random.randint(0,255), random.randint(0,255))
		t.forward(distance)

def main():
	turns = int(input("How manys turns should the turtle make? "))
	distance = int(input("How far should it travel before turning?"))
	t = Turtle()
	randomWalk(t, turns, distance)


if __name__ == "__main__":
	main()