"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import turtle


from polygon import circle, arc

# LEVEL 0 PRIMITIVES 
# fd, bk, lt, rt, pu, pd

def forward(t: turtle.Turtle, length):
    t.fd(length)

def bk(t: turtle.Turtle, length):
    t.bk(length)

def lt(t: turtle.Turtle, angle=90):
    t.lt(angle)

def rt(t, angle=90):
    t.rt(angle)

def pen_down(t: turtle.Turtle):
    t.pd()

def pen_up(t):
    t.pu()


# LEVEL 1 PRIMITIVES are simple combinations of Level 0 primitives.
# They have no pre- or post-conditions.

def fdlt(t, n, angle=90):
    """forward and left"""
    forward(t, n)
    lt(t, angle)

def fdbk(t, n):
    """forward and back, ending at the original position"""
    forward(t, n)
    bk(t, n)

def skip(t, n):
    """lift the pen and move"""
    pen_up(t)
    forward(t, n)
    pen_down(t)

def stump(t, n, angle=90):
    """Makes a vertical line and leave the turtle at the top, facing right"""
    lt(t)
    forward(t, n)
    rt(t, angle)

def hollow(t, n):
    """move the turtle vertically and leave it at the top, facing right"""
    lt(t)
    skip(t, n)
    rt(t)


# LEVEL 2 PRIMITIVES use primitives from Levels 0 and 1
# to draw posts (vertical elements) and beams (horizontal elements)
# Level 2 primitives ALWAYS return the turtle to the original
# location and direction.

def post(t, n):
    """Makes a vertical line and return to the original position"""
    lt(t)
    fdbk(t, n)
    rt(t)

def beam(t, n, height):
    """Makes a horizontal line at the given height and return."""
    hollow(t, n*height)
    fdbk(t, n)
    hollow(t, -n*height)

def hangman(t, n, height):
    """Makes a vertical line to the given height and a horizontal line
    at the given height and then return.
    This is efficient to implement, and turns out to be useful, but
    it's not so semantically clean."""
    stump(t, n * height)
    fdbk(t, n)
    lt(t)
    bk(t, n*height)
    rt(t)

def diagonal(t: turtle.Turtle, x, y):
    """Makes a diagonal line to the given x, y offsets and return"""
    from math import atan2, sqrt, pi
    angle = atan2(y, x) * 180 / pi
    dist = sqrt(x**2 + y**2)
    lt(t, angle)
    fdbk(t, dist)
    rt(t, angle)

def vshape(t, n, height):
    diagonal(t, -n/2, height*n)
    diagonal(t, n/2, height*n)

def bump(t, n, height):
    """Makes a bump with radius n at height*n 
    """
    stump(t, n*height)
    arc(t, n/2.0, 180)
    lt(t)
    fdlt(t, n*height+n)


"""
The letter-drawing functions all have the precondition
that the turtle is in the lower-left corner of the letter,
and postcondition that the turtle is in the lower-right
corner, facing in the direction it started in.

They all take a turtle as the first argument and a size (n)
as the second.  Most letters are (n) units wide and (2n) units
high.

"""

def draw_a(t, n):
    diagonal(t, n/2, 2*n)
    beam(t, n, 1)
    skip(t, n)
    diagonal(t, -n/2, 2*n)

def draw_b(t, n):
    bump(t, n, 1)
    bump(t, n, 0)
    skip(t, n/2)

def draw_c(t, n):
    hangman(t, n, 2)
    forward(t, n)

def draw_d(t, n):
    bump(t, 2*n, 0)
    skip(t, n)

def draw_ef(t, n):
    hangman(t, n, 2)
    hangman(t, n, 1)

def draw_e(t, n):
    draw_ef(t, n)
    forward(t, n)
    
def draw_lowercase_e(t, n):
    """Draw a lowercase e"""
    #stump(t, n/2)
    pen_up(t)
    lt(t)
    forward(t, 0.4*(n))
    pen_down(t)
    rt(t)    
    forward(t, n/2)
    arc(t, n/2, 270)
    forward(t, n/2.4)
    arc(t, n/2, 130)
    rt(t, 40)
    pen_up(t)
    rt(t, 90)
    forward(t, n*0.1)
    pen_down(t)
    lt(t, 90)
    
def draw_lowercase_g(t, n):
    """Draw a lowercase g"""
    circle(t, (n/2)*1.4)
    skip(t, (n/2)*1.4)
    post(t, n*1.4)
    post(t, -n/2)
    hollow(t, -n/2)
    rt(t)
    arc(t, 0.7*n, -140)

def draw_f(t, n):
    draw_ef(t, n)
    skip(t, n)

def draw_g(t, n):
    hangman(t, n, 2)
    forward(t, n/2)
    beam(t, n/2, 2)
    forward(t, n/2)
    post(t, n)

def draw_h(t, n):
    post(t, 2*n)
    hangman(t, n, 1)
    skip(t, n)
    post(t, 2*n)

def draw_i(t, n):
    beam(t, n, 2)
    forward(t, n/2)
    post(t, 2*n)
    forward(t, n/2)

def draw_j(t, n):
    beam(t, n, 2)
    arc(t, n/2, 90)
    forward(t, 3*n/2)
    skip(t, -2*n)
    rt(t)
    skip(t, n/2)

def draw_k(t, n):
    post(t, 2*n)
    stump(t, n, 180)
    vshape(t, 2*n, 0.5)
    fdlt(t, n)
    skip(t, n)

def draw_l(t, n):
    post(t, 2*n)
    forward(t, n)
    
def draw_lowercase_l(t, n):
    post(t, 2*n)
    forward(t, n/8)
    

def draw_n(t: turtle.Turtle, n):
    post(t, 2*n)
    skip(t, n)
    diagonal(t, -n, 2*n)
    post(t, 2*n)

def draw_m(t, n):
    post(t, 2*n)
    draw_v(t, n)
    post(t, 2*n)

def draw_o(t, n):
    skip(t, n)
    circle(t, n)
    skip(t, n/2)

def draw_p(t, n):
    bump(t, n, 1)
    skip(t, n/2)

def draw_q(t, n):
    draw_o(t, n)
    diagonal(t, -n/2, n)

def draw_r(t, n):
    draw_p(t, n)
    diagonal(t, -n/2, n)

def draw_s(t, n):
    forward(t, n/2)
    arc(t, n/2, 180)
    arc(t, n/2, -180)
    fdlt(t, n/2, -90)
    skip(t, 2*n)
    lt(t)

def draw_t(t, n):
    beam(t, n, 2)
    skip(t, n/2)
    post(t, 2*n)
    skip(t, n/2)

def draw_u(t, n):
    post(t, 2*n)
    forward(t, n)
    post(t, 2*n)

def draw_v(t, n):
    skip(t, n/2)
    vshape(t, n, 2)
    skip(t, n/2)

def draw_w(t, n):
    draw_v(t, n)
    draw_v(t, n)

def draw_x(t, n):
    diagonal(t, n, 2*n)
    skip(t, n)
    diagonal(t, -n, 2*n)

def draw_v(t, n):
    skip(t, n/2)
    diagonal(t, -n/2, 2*n)
    diagonal(t, n/2, 2*n)
    skip(t, n/2)

def draw_y(t, n):
    skip(t, n/2)
    stump(t, n)
    vshape(t, n, 1)
    rt(t)
    fdlt(t, n)
    skip(t, n/2)

def draw_z(t, n):
    beam(t, n, 2)
    diagonal(t, n, 2*n)
    forward(t, n)
    
def draw_horizontal_1(t, n):
    """draw a horizontal line"""
    fdbk(t, 300)
    
def draw_horizontal_2(t, n):
    """draw a horizontal line"""
    pen_up(t)
    lt(t)
    forward(t, 0.7*(n*2))
    pen_down(t)
    rt(t)
    fdbk(t, 300)
    pen_up(t)
    rt(t)
    forward(t, 0.7*(n*2))
    pen_down(t)
    lt(t)

def draw_(t, n):
    # draw a space
    skip(t, n)

if __name__ == '__main__':

    # create and position the turtle
    size = 20
    bob = turtle.Turtle()


    for f in [draw_horizontal_1, draw_horizontal_2, draw_o, draw_lowercase_l, draw_lowercase_e,  draw_lowercase_g]:
        f(bob, size)
        skip(bob, size)

    turtle.mainloop()
