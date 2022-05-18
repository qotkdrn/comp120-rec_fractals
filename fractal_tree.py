"""
File: fractal_tree.py
Author: Alex Bae, Galen Forbes-Roberts, Josue Bautista
Date: 3/12/21
Description: Displays fractal tree using tkinter and recursion
"""
import tkinter as tk
import math

class FractalTree:
    def __init__(self):
        """ Initialize the fractal object. """
        self.SIZE = 400
        # Create window, canvas, control frame, buttons
        self.window = tk.Tk()
        self.window.title("Fractal Tree")
        self.canvas = tk.Canvas(self.window, width = self.SIZE, height = self.SIZE, 
                        borderwidth = 1, relief = 'solid')
        self.canvas.grid(row = 1, column = 1)

        self.control_frame = tk.Frame(self.window, width = self.SIZE, height = 50)
        self.control_frame.grid(row = 2, column = 1)
        self.control_frame.grid_propagate(False)

        self.advance_button = tk.Button(self.control_frame, text="Advance", command = self.advance)
        self.advance_button.grid(row=1, column=1)
        self.reset_button = tk.Button(self.control_frame, text="Reset", command = self.reset)
        self.reset_button.grid(row=1, column=2)
        self.quit_button = tk.Button(self.control_frame, text="Quit", command = self.quit)
        self.quit_button.grid(row=1, column=3)
        self.control_frame.grid_rowconfigure(1, weight = 1)
        self.control_frame.grid_columnconfigure(1, weight = 1)
        self.control_frame.grid_columnconfigure(2, weight = 1)
        self.control_frame.grid_columnconfigure(3, weight = 1)

        #declare instance variables
        self.angleFactor = math.pi/5
        self.sizeFactor = 0.58
        self.xval = 400
        self.yval = 400
        self.branch_l = self.SIZE / 3

        # Init current levels of recursion, and draw the intial fractal
        self.current_levels_of_recursion = 0  
        self.canvas.create_line(self.xval/2, self.yval, self.xval/2, self.yval - self.branch_l, tags = 'branches', fill = 'brown')

        tk.mainloop()

    def advance(self):
        """ Advance one level of recursion """
        #self.canvas.delete('branches')
        self.current_levels_of_recursion += 1
        self.draw_fractal(self.xval/2, self.yval, self.branch_l, math.pi/2, self.current_levels_of_recursion)

    def draw_fractal(self, x1, y1, branch_l, angle, current_levels_of_recursion):
        """ 
        Draw fractal tree using recursion. The 'parent' branch is always present no matter what the level of recursion and is a 
        third of the canvas size. Following 'child' branches are 0.58 times the 'parent' branch(es) that came from the previous 
        level of recursion. Additionally, with each advance in level of recursion, the angle in relation to the x axis to the 
        right of the initial branch is adjusted by an angle factor of pi/5.
        """
        
        if current_levels_of_recursion >= 0:
            current_levels_of_recursion -= 1

            x2 = x1 + float(math.cos(angle) * branch_l)
            y2 = y1 - float(math.sin(angle) * branch_l)

            self.canvas.create_line(x1,y1,x2,y2,tags = 'branches', fill = 'green')

            self.draw_fractal(x2, y2, branch_l * self.sizeFactor, angle + self.angleFactor, current_levels_of_recursion)
            self.draw_fractal(x2, y2, branch_l * self.sizeFactor, angle - self.angleFactor, current_levels_of_recursion)
           
    def reset(self):
        """ Reset to 0 levels of recursion """
        self.canvas.delete("all")
        self.current_levels_of_recursion = 0
        self.draw_fractal(self.xval/2, self.yval, self.branch_l, math.pi/2, self.current_levels_of_recursion)
        
    def quit(self):
        """ Quit the program """
        self.window.destroy()

if __name__ == "__main__":
    FractalTree()