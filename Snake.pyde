import random, os
path = os.getcwd()

class Game:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.snake = Snake(self.h/2, self.w/2, 15, "head_left.png", 30, 30)
        
    def show(self):
        stroke(205,205,205)
        fill(205,205,205)
        
        if self.snake.alive == True:
            fill(140,208,125)
            self.snake.show()
            
        elif self.snake.alive == False:
            fill(0)
            textSize(16)
            textAlign(CENTER, CENTER)
            text("Game Over!",self.h/2,self.w/2)
            textSize(14)
            textAlign(CENTER,TOP)
            text("Press Any Key to Play Again :)", self.h/2, self.w/2+15)
        
class Element:
    def __init__(self, x, y, r, img, img_w, img_h):
        self.x = x
        self.y = y
        self.r = r
        self.ym = 0
        self. xm = 0
        self.img_w = img_w
        self.img_h = img_h
        self.img = loadImage(path + "/images/" + img)
        self.dir = RIGHT


    def show(self):
        circle(self.x+self.r, self.y+self.r, self.r*2)
    
        
class Snake(Element):
    def __init__(self, x, y, r, img, img_w, img_h):
        Element.__init__(self,x, y, r, img, img_w, img_h)
        self.alive = True
        self.key_dict = {LEFT: False, RIGHT: False, UP: False, DOWN: False}

            
    def move(self):
            if self.key_dict[DOWN] == True:
                self.ym = self.r
                self.y += self.ym + self.r
                
            elif self.key_dict[UP] == True:
                self.ym = -self.r
                self.y += self.ym - self.r
                
            elif self.key_dict[RIGHT] == True:
                self.xm = self.r
                self.x += self.xm +self.r
                self.dir = RIGHT
    
            elif self.key_dict[LEFT] == True:
                self.xm = -self.r
                self.x += self.xm - self.r
                self.dir = LEFT
                        
                
    def update(self):
        self.move()
        if (self.y) > play.h or (self.y) < 0 or (self.x) > play.w or (self.x) < 0:
            self.alive = False
            
        if self.dir == RIGHT:
            image(self.img, self.x, self.y, self.img_w, self.img_h, self.x + self.img_w, self.y + self.img_h, self.x, self.y)
        
        elif self.dir == LEFT:
            image(self.img, self.x, self.y, self.img_w, self.img_h)
      
          
                
                
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
    
