import random, os
path = os.getcwd()

class Game:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.snake = Snake(300,300,15)
        #FIX IT (MAKE PIXELS GLOBAL)
        
    def show(self):
        stroke(205,205,205)
        fill(205,205,205)
        stroke(0)
        fill(140,208,125)
        self.snake.show()
        
class Element:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.ym = 0
        self. xm = 0

    def show(self):
        circle(self.x, self.y, self.r*2)
        
        
class Snake(Element):
    def __init__(self, x, y, r):
        Element.__init__(self,x, y, r)
        self.key_dict = {LEFT: False, RIGHT: False, UP: False, DOWN: False}
        
        def move(self):
            if self.key_dict == DOWN:
                self.ym = -5
                
            elif self.key_dict == UP:
                self.ym = 5
                
            elif self.key_dict == RIGHT:
                self.xm = 5
    
            elif self.key_dict == LEFT:
                self.xm = -5
                
            else:
                self.xm = -5
                
                
            self.x += self.xm
            self.y += self.ym
            
        def show(self):
            self.move()
            
                


play = Game(600,600)

def keyPressed():
    if keyCode == LEFT:
        play.snake.key_dict[LEFT] = True
        
    elif keyCode == RIGHT:
        play.snake.key_dict[RIGHT] = True
        
    elif keyCode == UP:
        play.snake.key_dict[UP] = True

    elif keyCode == DOWN:
        play.snake.key_dict[DOWN] = True
        
def keyReleased():
    if keyCode == LEFT:
        play.snake.key_dict[LEFT] = False
        
    elif keyCode == RIGHT:
        play.snake.key_dict[RIGHT] = False
        
    elif keyCode == UP:
        play.snake.key_dict[UP] = False

    elif keyCode == DOWN:
        play.snake.key_dict[DOWN] = False
        
        
def setup():
    size(play.w, play.h)
    background(205,205,205)
    
    
def draw():
    background(205,205,205)
    play.show()
    
