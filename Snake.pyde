import random, os
path = os.getcwd()

class Game:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.snake = Snake(self.h/2, self.w/2, 15, "head_left.png", 30, 30, "head_up.png")
        
    def show(self):
        stroke(205,205,205)
        fill(205,205,205)
        
        if self.snake.alive == True:
            fill(80,153,32)
            self.snake.show()
            
        elif self.snake.alive == False:
            fill(0)
            textSize(16)
            textAlign(CENTER, CENTER)
            text("Game Over!",self.h/2,self.w/2)
            textSize(14)
            textAlign(CENTER,TOP)
            text("Press Any Key to Play Again :)", self.h/2, self.w/2+15)
            
            # if keyPressed == True:


class Element:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.ym = 0
        self. xm = 0
        
    def update(self):
        self.x += self.xm
        self.y += self.ym


    def show(self):
        circle(self.x+self.r, self.y+self.r, self.r*2)
    
        
class Snake(Element):
    def __init__(self, x, y, r, img, img_w, img_h, img2):
        Element.__init__(self,x, y, r)
        self.alive = True
        self.key_dict = {LEFT: False, RIGHT: True, UP: False, DOWN: False}
        self.img_w = img_w
        self.img_h = img_h
        self.img = loadImage(path + "/images/" + img)
        self.img2 = loadImage(path + "/images/" + img2)
        self.dir = RIGHT
        self.tail = []

    def move(self):
            if self.key_dict[DOWN] == True:
                self.ym = self.r
                self.y += self.ym + self.r
                self.dir = DOWN
                
            elif self.key_dict[UP] == True:
                self.ym = -self.r
                self.y += self.ym - self.r
                self.dir = UP
                
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
        #Makes sure that the snake doesn't go out of the board
        if (self.y) > play.h or (self.y) < 0 or (self.x) > play.w or (self.x) < 0:
            self.alive = False
            
    def head(self):
        if self.dir == LEFT:
            image(self.img, self.x, self.y, self.img_w, self.img_h)
           
        elif self.dir == RIGHT:
            image(self.img, self.x, self.y, self.img_w, self.img_h, self.img_w, 0, 0, self.img_h)
             
        elif self.dir == UP:
            image(self.img2, self.x, self.y, self.img_w, self.img_h)

        elif self.dir == DOWN:
            image(self.img2, self.x, self.y, self.img_w, self.img_h, self.img_w, self.img_h, 0, 0)
            
            
    # def tail(self):
        
    
                
    def show(self):
            Element.show(self)
            self.head()
            self.update()
            
# class Food:
#     def __init__(self, x, y, img, img_w, img_h



play = Game(600,600)

def keyPressed():
    if keyCode == LEFT:
        if play.snake.key_dict[RIGHT] == True:
            pass
            
        else:
            play.snake.key_dict[LEFT] = True
            play.snake.key_dict[UP] = False
            play.snake.key_dict[DOWN] = False
            play.snake.snake_dir = LEFT
        
    elif keyCode == RIGHT:
        if play.snake.key_dict[LEFT] == True:
            pass
            
        else:
            play.snake.key_dict[RIGHT] = True
            play.snake.key_dict[UP] = False
            play.snake.key_dict[DOWN] = False
            play.snake.snake_dir = RIGHT
        
    elif keyCode == UP:
        if play.snake.key_dict[DOWN] == True:
            pass
        
        else:
            play.snake.key_dict[UP] = True
            play.snake.key_dict[LEFT] = False
            play.snake.key_dict[RIGHT] = False
            play.snake.snake_dir = UP

    elif keyCode == DOWN:
        if play.snake.key_dict[UP] == True:
            pass
            
        else:
            play.snake.key_dict[DOWN] = True
            play.snake.key_dict[LEFT] = False
            play.snake.key_dict[RIGHT] = False
            play.snake.snake_dir = DOWN
        
        
def setup():
    size(play.w, play.h)
    background(205,205,205)
    
    
def draw():
    if frameCount % 12 == 0:
        background(205,205,205)
        play.show()
    
