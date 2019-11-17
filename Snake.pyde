import random, os
path = os.getcwd()

ROWS = 20
COLS = 20

class Game:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.snake = Snake()
        # self.fruit = Food()
        
    def show(self):
        if self.snake.alive == True:
            self.snake.show()
            
        elif self.snake.alive == False:
            fill(0)
            textSize(16)
            textAlign(CENTER, CENTER)
            text("Game Over!",self.h/2,self.w/2)
            textSize(14)
            textAlign(CENTER,TOP)
            text("Click to Restart!", self.h/2, self.w/2+15)
            

class Element:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.ym = 0
        self.xm = 0
        self.color = color
        
    def update(self):
        self.x += self.xm
        self.y += self.ym

    def show(self):
        if self.color == "yellow":
            fill(251, 226, 76)
        elif self.color == "green":
            fill(80, 153, 32)
        elif self.color == "red":
            fill(173, 48, 32)
            
        circle(self.x+15, self.y+15, 30)
    
        
class Snake():
    def __init__(self):
        self.r = 15
        self.alive = True
        self.key_dict = {LEFT: False, RIGHT: True, UP: False, DOWN: False}
        self.img2 = loadImage(path + "/images/head_up.png" )
        self.img = loadImage(path + "/images/head_left.png")
        self.dir = RIGHT
        self.tail = [Element(300, 300, "green"), Element(270, 300, "green"), Element(240, 300, "green"), Element(210, 300, "green")]

    def move(self):
            if self.key_dict[DOWN] == True:
                self.ym = self.r
                self.tail[0].y += self.ym + self.r
                self.dir = DOWN
                
            elif self.key_dict[UP] == True:
                self.ym = -self.r
                self.tail[0].y += self.ym - self.r
                self.dir = UP
                
            elif self.key_dict[RIGHT] == True:
                self.xm = self.r
                self.tail[0].x += self.xm +self.r
                self.dir = RIGHT
  
    
            elif self.key_dict[LEFT] == True:
                self.xm = -self.r
                self.tail[0].x += self.xm - self.r
                self.dir = LEFT
                
            for i in range(1, len(self.tail)):
                self.tail[-i].x = self.tail[-i-1].x
                self.tail[-i].y = self.tail[-i-1].y
                
                        
    def update(self):
        self.move()
        #Makes sure that the snake doesn't go out of the board
        if (self.tail[0].y) >= play.h or (self.tail[0].y) < 0 or (self.tail[0].x) >= play.w or (self.tail[0].x) < 0:
            self.alive = False
            
        
            
    def head(self):
        if self.dir == LEFT:
            image(self.img, self.tail[0].x, self.tail[0].y, 30, 30)
           
        elif self.dir == RIGHT:
            image(self.img, self.tail[0].x, self.tail[0].y, 30, 30, 30, 30, 0, 0)
             
        elif self.dir == UP:
            image(self.img2, self.tail[0].x, self.tail[0].y, 30, 30)

        elif self.dir == DOWN:
            image(self.img2, self.tail[0].x, self.tail[0].y, 30, 30, 30, 30, 0, 0)
            
            
    # def tail(self):
        
    
                
    def show(self):
        for element in self.tail:
            element.show()
        self.head()
        self.update()
            
# class Food:
#     def __init__(self):
#         self.x = random.randint(0, play.w)
#         self.y = random.randint(0, play.h)
#         # self.type = 
        
#     # def show(self):
        
    



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
    
def mouseClicked():
    global play
    play = Game(600, 600)
    
def draw():
    if frameCount % 12 == 0:
        background(205,205,205)
        play.show()
    
