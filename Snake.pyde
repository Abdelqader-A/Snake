import random, os
path = os.getcwd()

class Game:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.snake = Snake(self.h/2,self.w/2,15)
        
    def show(self):
        stroke(205,205,205)
        fill(205,205,205)
        
        if self.snake.alive == True:
            fill(140,208,125)
            self.snake.show()
            
        elif self.snake.alive == False:
            fill(0)
            textSize(16)
            text("Game Over!", self.h/2, self.w/2)
        
class Element:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.ym = 0
        self. xm = 0

    def show(self):
        circle(self.x+self.r, self.y+self.r, self.r*2)
    
        
class Snake(Element):
    def __init__(self, x, y, r):
        Element.__init__(self,x, y, r)
        self.alive = True
        self.key_dict = {LEFT: False, RIGHT: False, UP: False, DOWN: False}
            
    def update(self):
            if self.key_dict[DOWN] == True:
                self.ym = self.r
                self.y += self.ym + self.r
                
            elif self.key_dict[UP] == True:
                self.ym = -self.r
                self.y += self.ym - self.r
                
            elif self.key_dict[RIGHT] == True:
                self.xm = self.r
                self.x += self.xm +self.r
    
            elif self.key_dict[LEFT] == True:
                self.xm = -self.r
                self.x += self.xm - self.r
                
    def show(self):
            Element.show(self)
            self.update()
            

        

play = Game(600,600)

def keyPressed():
    if keyCode == LEFT:
        play.snake.key_dict[LEFT] = True
        play.snake.key_dict[RIGHT] = False
        play.snake.key_dict[UP] = False
        play.snake.key_dict[DOWN] = False
        
    elif keyCode == RIGHT:
        play.snake.key_dict[RIGHT] = True
        play.snake.key_dict[LEFT] = False
        play.snake.key_dict[UP] = False
        play.snake.key_dict[DOWN] = False
        
    elif keyCode == UP:
        play.snake.key_dict[UP] = True
        play.snake.key_dict[DOWN] = False
        play.snake.key_dict[LEFT] = False
        play.snake.key_dict[RIGHT] = False

    elif keyCode == DOWN:
        play.snake.key_dict[DOWN] = True
        play.snake.key_dict[UP] = False
        play.snake.key_dict[LEFT] = False
        play.snake.key_dict[RIGHT] = False
        
        
def setup():
    size(play.w, play.h)
    background(205,205,205)
    
    
def draw():
    if frameCount % 12 == 0:
        background(205,205,205)
        play.show()
    
