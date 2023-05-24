#since there are going to be different multiple balls, we create a class
class ball():

    #creating a constructor for the class
    def __init__(self, canvas, #we receive our canvas
                  x, #x position
                  y, #y position
                  diameter, #diameter of ball
                  xVel, #moving speed on x-coordinates
                  yVel, #moving speed on y-coordinates
                  color #color of ball
                  ):
        self.canvas = canvas #the canvas we receive when pass to us as an argument
        self.image = canvas.create_oval(x,y,diameter,diameter, fill=color) #draw the ball --diameter is the same for width and height
        self.yVel = yVel # related to direction and speed which it would head in
        self.xVel = xVel

    #the ball will not move until this function is created
    def move(self):
        # get the coordinates
        co_xy = self.canvas.coords(self.image) #we pass in image
        #print(co_xy)
        #we have four coordinates, nw, ne, sw, se
        #checking to see if the ball touches the left or right sides of the window
        if (co_xy[2]>=(self.canvas.winfo_width()) or co_xy[0]<0): #[0] -nw, [1] -ne, [2] -se(bottom right corner), [3] -sw
            self.xVel=-self.xVel #change direction when it touches the window
        if (co_xy[3]>=(self.canvas.winfo_height()) or co_xy[1]<0):
            self.yVel=-self.yVel
        #move image and in what directions (xVel & yVel)
        self.canvas.move(self.image, self.xVel, self.yVel) #we call the function inside itself