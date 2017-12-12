def tower(height,fromPole, toPole, withPole):
    if height >= 1:
        tower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        tower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

tower(int(input('How many disks you wanna play? ')),"A","B","C")
