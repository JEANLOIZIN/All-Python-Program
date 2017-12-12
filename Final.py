def blockWall(Len,n):
    t.down()
    for i in range(n):
        while i<4:
            t.fd(Len)
            t.left(90)
            t.fd(Len)
        
        
import turtle
t=turtle.Turtle()
blockWall(30,4)
    
