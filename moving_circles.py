"""
File: moving_circles.py 

Author: Alex Bae, Galen Forbes-Roberts, Josue Bautista

Date: 3/12/2021

Description: Program that gets two circle locations from the
user, then draws a line between them, and 
displays the distance between them midway along
the line.  The user can drag either circle around,
and the distance is kept updated.
"""

# Imports
import tkinter as tk
from enum import Enum
import math
    
class MovingCircles:
    def __init__(self):
        #Create window, frame, and buttons
        self.SIZE = 400
        self.window = tk.Tk()
        self.window.title("Moving Circles")
        self.canvas = tk.Canvas(self.window, width = self.SIZE, height = self.SIZE, borderwidth = 1, relief = 'solid')
        self.canvas.grid(row = 1, column = 1)

        self.control_frame = tk.Frame(self.window, width = self.SIZE, height = 50)
        self.control_frame.grid(row = 2, column = 1)

        self.clear_button = tk.Button(self.control_frame, text="Clear", command = self.clear)
        self.clear_button.grid(row = 1, column = 1)
        self.quit_button = tk.Button(self.control_frame, text="Quit", command = self.quit)
        self.quit_button.grid(row = 1, column = 2)

        #declare instance variable radius, bind left click to mousedown handler. 
        #current state is that of waiting for the first click
        self.radius = 20
        self.canvas.bind("<Button-1>", self.mousedown_handler)
        self.state = State.WAITING_FOR_FIRST_CLICK

        tk.mainloop()

    def clear(self):
        '''clear everything that is on the canvas and set to default set'''
        self.canvas.delete("all")
        self.state = State.WAITING_FOR_FIRST_CLICK

    def quit(self):
        '''terminate the program'''
        self.window.destroy()

    def mousedown_handler(self, event):
        #1st click creates the first circle, state is set to 'waiting for second click' to prepare to make second circle
        if self.state == State.WAITING_FOR_FIRST_CLICK:
            self.center1 = (event.x,event.y)
            x1 = event.x - self.radius
            y1 = event.y - self.radius
            x2 = event.x + self.radius
            y2 = event.y + self.radius
            self.circle1 = self.canvas.create_oval(x1,y1,x2,y2, fill = 'red', tags = 'circle1')

            self.state = State.WAITING_FOR_SECOND_CLICK
        #2nd click creates 2nd circle
        elif self.state == State.WAITING_FOR_SECOND_CLICK:
            self.center2 = (event.x,event.y)
            x1 = event.x - self.radius
            y1 = event.y - self.radius
            x2 = event.x + self.radius
            y2 = event.y + self.radius
            self.circle2 = self.canvas.create_oval(x1,y1,x2,y2, fill = 'red', tags = 'circle2')

            #now that both circles are made, we set to new state so that no additional circles are made
            #we also bind more mouse actions to separate methods
            self.canvas.tag_bind(self.circle1, "<B1-Motion>", self.move_circle1)
            self.canvas.tag_bind(self.circle2, "<B1-Motion>", self.move_circle2)
            self.get_line_text(self.center1, self.center2)
            self.state = State.DRAGGING_CIRCLES

    def get_line_text(self, center1, center2):
        #display distance and line between circles
        self.center_line = self.canvas.create_line(self.center1,self.center2, fill = 'red', tags = 'line')
        self.distance = math.sqrt((self.center1[0] - self.center2[0])**2 + (self.center1[1] - self.center2[1])**2)
        self.dist = "{:.2f}".format(self.distance)
        self.txt_center = ((self.center2[0] + self.center1[0])/2, (self.center2[1] + self.center1[1])/2)
        self.center_text = self.canvas.create_text(self.txt_center[0], self.txt_center[1], text = str(self.dist), font = 'Times 10', tags = 'text')

    def move_circle1(self, event):
        #once in dragging state, you can move 1st circle
        x = event.x - self.center1[0]
        y = event.y - self.center1[1]
        self.center1 = (event.x,event.y)
        self.canvas.move(self.circle1, x, y) 
        self.canvas.delete('line','text')
        self.get_line_text(self.center1, self.center2)
        
    def move_circle2(self, event):
        #once in dragging state, you can move 2nd circle
        x = event.x - self.center2[0]
        y = event.y - self.center2[1]
        self.center2 = (event.x, event.y)
        self.canvas.move(self.circle2, x, y)
        self.canvas.delete('line','text')
        self.get_line_text(self.center1,self.center2)

class State(Enum):
    #declare states. different state allows for different actions
    WAITING_FOR_FIRST_CLICK = 1
    WAITING_FOR_SECOND_CLICK = 2
    DRAGGING_CIRCLES = 3

if __name__ == "__main__":
    # Create GUI
    MovingCircles() 