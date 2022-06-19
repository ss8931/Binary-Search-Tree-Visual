from typing import Optional
from tree import Node, append
from turtle import *
from sys import stdin


CIR = 30
ANG = 20
FAR = 100
PROMPT = "> "


def plotNode(n: Node) -> None:
    circle(CIR, 360, 100)
    up()
    left(90)
    fd(CIR / 2)
    write(n.data, align="center", font=("Arial", 20, "normal"))
    bk(CIR/2)
    right(90)
    down()


def plot(n: Node) -> None:
    if n == None:
        return
    plotNode(n)

    if n.left != None:
        right(180 - ANG)
        fd(FAR)
        up()
        left(90 - ANG)
        fd(CIR * 2)
        left(90)
        down()
        plot(n.left)
        up()
        right(90)
        bk(CIR * 2)
        right(90 - ANG)
        down()
        bk(FAR)
        left(180 - ANG)
    if n.right != None:
        right(ANG)
        fd(FAR)
        up()
        right(90 - ANG)
        fd(CIR * 2)
        left(90)
        down()
        plot(n.right)
        up()
        right(90)
        bk(CIR * 2)
        left(90 - ANG)
        down()
        bk(FAR)
        left(ANG)

def inp(term: bool) -> Optional[int | float]:
    """
        Get input from stdin or turtle.
    """
    if term:
        line = numinput("Append", "Number")
        if line is None: return None
        return int(line) if line % 1 == 0 else float(line)

    for line in stdin:
        return int(line) if "." not in line else float(line)



if __name__ == "__main__":
    root = None
    term = stdin.isatty()
    pensize(3)
    hideturtle()
    tracer(0)
    speed(0)
    while (line := inp(term)) is not None:
        root = append(root, line)
        plot(root)
        update()

    mainloop()
