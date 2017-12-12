#JEAN LOIZIN
#CS100
#DATE 2-06-15


#3.17

a,b,c= 3,4,5
if a<b:
    print("\n'OK'")
    
if  c<b:
    print("It's not okay")
else:
    print("\n'OK'")

if (a+b)==c:
    print("It's not okay")
else:
    print("\n'OK'")

if ((a+b)**2)==(c**2):
    print("It's not okay")
else:
    print("\n'OK'")
    


#3.18
a,b,c=3,4,5



if a<b:
    print("\n\n'NOT OKAY'")
    
if  c<b:
    print('OK')
else:
    print("\n'NOT OKAY'")

if (a+b)==c:
    print('OK')
else:
    print("\n'NOT OKAY'")

if ((a+b)**2)==(c**2):
    print('OK')
else:
    print("\n'NOT OKAY'\n\n")



# TRIANGLE

C=str(input("Please enter the color desire: "))
W=int(input("Please enter the Width: " ))
L=int(input("Please enter the lenght: "))
      

import turtle
s=turtle.Turtle()
s.down()

s.color(C)
s.width(W)
for i in range (3):
      s.forward(L)
      s.right(120)
      

