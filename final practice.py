'''
def paralleLines(t,numlines,linelength):
    t.down()
    for i in range(numlines):
        t.forward(linelength)
        t.up()
        t.bk(linelength)
        t.right(90)
        t.forward(30)
        t.left(90)
        t.down()

import turtle
t=turtle.Turtle()

paralleLines(t,5,100)
'''
'''hulkLine=["you","wouldn't","like","me","when","i'm","angry"]
def containsLetter(hulkLine):
    
    SearchLetter='i'
    newLines=[]
    for words in hulkLine:
        if SearchLetter in words:
            newLines.append(words)
    return newLines

print(containsLetter(hulkLine))
'''
"""def tri(t,size):
    t.down()
    for i in range(3):
        t.fd(size)
        t.left(120)


def trifecta(size,angle,num):
    t.down()
    for i in range(num):
        tri(t,size)
        t.right(angle)


import turtle
t=turtle.Turtle()
trifecta(100,25,5)"""




























filein='you can steer yourself any direction you choose'
fileout=''

def makeWordList(filein,fileout):
    inf=open(filein,'r')
    outf=open(fileout,'w')
    inLines = inf.lower().split('\n')
    for words in inLines:
        outf.write(words)
    return fileout
makeWordList(filein,fileout)

