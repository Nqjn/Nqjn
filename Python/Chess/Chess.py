from tkinter import *
import math


class Board:
    def __init__(self):
        self.lol = 64
        self.arr = list(range(1, self.lol + 1))
        self.sq = math.isqrt(self.lol)
        self.rectangle_width = 100
        self.black = {
            "r1": [1,0],
            "r1": [1,1],
            "r1": [1,2],
            "r1": [1,3],
            "r1": [1,4],
            "r1": [1,5],
            "r1": [1,6],
            "r1": [1,7],            
        }
       
    def Field(self):
        cl1 = '#B58863'
        cl2 = '#F0D9B5'
        
        for i, num in enumerate(self.arr):
            
            x1 = i % self.sq * (self.rectangle_width)
            y1 = i // self.sq * (self.rectangle_width)
            x2 = x1 + self.rectangle_width
            y2 = y1 + self.rectangle_width
            if (i//8)%2 ==0:
                if num %2 ==0 :
                    w.create_rectangle(x1, y1, x2, y2, fill=cl1, outline=cl1)
                else:
                    w.create_rectangle(x1, y1, x2, y2, fill=cl2,outline=cl2)
            else:
                if num %2 ==0 :
                    w.create_rectangle(x1, y1, x2, y2, fill=cl2, outline=cl2)
                else:
                    w.create_rectangle(x1, y1, x2, y2, fill=cl1, outline=cl1)
                    
                    
    def Draw_Figures(self):
        x1 = self.black["r1"][0]% self.sq * (self.rectangle_width)
        y1 = self.black["r1"][1]// self.sq * (self.rectangle_width)
        x2 = x1 + self.rectangle_width
        y2 = y1 + self.rectangle_width
        w.create_rectangle(x1, y2, x2, y2, fill="red")




a1 = Board()
root = Tk()
root.title("Chess")
w = Canvas(root, width=800, height=800)
w.pack()

a1.Field()
# a1.Draw_Figures()
root.mainloop()