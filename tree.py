import turtle
def tree(t, trunkLength):
    import random
    def angle():
        return random.randint(35,40)
    def subBranch():
        return random.randint(12,18)
    angle=angle()
    subBranch=subBranch()
    if trunkLength < 5:
        return
    else:
        t.speed(0)
        t.forward(trunkLength)
        t.right(angle)
        tree(t, trunkLength-subBranch)
        t.left(2*angle) #twice the angle
        tree(t, trunkLength-subBranch)
        t.right(angle)
        t.backward(trunkLength)
t = turtle.Turtle()
t.left(90)
