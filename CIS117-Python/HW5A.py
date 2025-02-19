"""Modified letters.py

This code is based on Think Python Chapter 4 examples by Allen Downey.
It draws the name "Oleg" with a capital O (drawn with the original function)
and custom lowercase letters for l, e, and g.
  
Adjust the parameters if you wish to refine the shapes.
Make sure polygon.py (providing circle and arc) is in the same folder.
"""

from __future__ import print_function, division
import turtle
from polygon import circle, arc

# LEVEL 0 PRIMITIVES 
def fd(t, length):
    t.fd(length)

def bk(t, length):
    t.bk(length)

def lt(t, angle=90):
    t.lt(angle)

def rt(t, angle=90):
    t.rt(angle)

def pd(t):
    t.pd()

def pu(t):
    t.pu()

# LEVEL 1 PRIMITIVES 
def fdlt(t, n, angle=90):
    fd(t, n)
    lt(t, angle)

def fdbk(t, n):
    fd(t, n)
    bk(t, n)

def skip(t, n):
    pu(t)
    fd(t, n)
    pd(t)

def stump(t, n, angle=90):
    lt(t)
    fd(t, n)
    rt(t, angle)

def hollow(t, n):
    lt(t)
    skip(t, n)
    rt(t)

# LEVEL 2 PRIMITIVES
def post(t, n):
    lt(t)
    fdbk(t, n)
    rt(t)

def beam(t, n, height):
    hollow(t, n * height)
    fdbk(t, n)
    hollow(t, -n * height)

def hangman(t, n, height):
    stump(t, n * height)
    fdbk(t, n)
    lt(t)
    bk(t, n * height)
    rt(t)

def diagonal(t, x, y):
    from math import atan2, sqrt, pi
    angle = atan2(y, x) * 180 / pi
    dist = sqrt(x**2 + y**2)
    lt(t, angle)
    fdbk(t, dist)
    rt(t, angle)

def vshape(t, n, height):
    diagonal(t, -n/2, height * n)
    diagonal(t, n/2, height * n)

def bump(t, n, height):
    stump(t, n * height)
    arc(t, n/2.0, 180)
    lt(t)
    fdlt(t, n * height + n)

# -------------------------------
# UPPERCASE LETTER (unchanged)
def draw_o(t, n):
    """Draw an uppercase O using a circle with radius n."""
    skip(t, n)
    circle(t, n)
    skip(t, n)

# -------------------------------
# LOWERCASE LETTER DRAWING FUNCTIONS
def draw_lower_l(t, n):
    """Draw a lowercase 'l'.
    n is the letter's height.
    This letter is drawn as a simple vertical stroke with a slight advance.
    """
    # Starting at the lower-left of the letter:
    pu(t)
    pd(t)
    lt(t, 90)   # face upward
    fd(t, n)    # draw vertical stroke
    bk(t, n)    # return to baseline
    rt(t, 90)   # restore eastward heading
    fd(t, n/2)  # advance horizontally (letter width)

def draw_lower_e(t, n):
    """Draw a lowercase 'e'.
    n is roughly the x-height.
    The design uses an almost complete circle (300° arc) to form the loop,
    with a short horizontal stroke to mimic the midline.
    """
    pu(t)
    pd(t)
    # Draw an almost complete circle for the loop:
    arc(t, n/2, 330)
    # Draw the "middle bar" of the e:
    lt(t, 60)
    fd(t, n/4)
    bk(t, n/4)
    rt(t, 60)
    # Advance to the right to finish the letter:
    fd(t, n/2)

def draw_lower_g(t, n):
    """Draw a lowercase 'g'.
    n is the x-height of the upper (round) part;
    the tail (descender) is about n/2.
    The design draws an almost complete loop then adds a descending tail.
    """
    pu(t)
    pd(t)
    # Draw the upper loop of g:
    arc(t, n/2, 300)
    # Now add the tail:
    rt(t, 60)   # adjust orientation downward
    fd(t, n/2)  # descend from the loop
    lt(t, 45)
    fd(t, n/4)  # draw a small hook
    bk(t, n/4)  # undo the hook stroke
    rt(t, 45)
    bk(t, n/2)  # return to the baseline of the loop
    # Advance horizontally to finish letter:
    fd(t, n/2)

# -------------------------------
# MAIN BLOCK: Draw "Oleg" with uppercase O and lowercase l, e, g.
if __name__ == '__main__':
    # Set sizes: capital_size for O and lower_height for the lowercase letters.
    capital_size = 40   # for uppercase O (draw_o uses this as its radius)
    lower_height = 20   # x-height for the lowercase letters

    bob = turtle.Turtle()

    # Draw uppercase O:
    draw_o(bob, capital_size)
    skip(bob, capital_size)  # space between letters

    # Draw lowercase l:
    draw_lower_l(bob, lower_height)
    skip(bob, lower_height)

    # Draw lowercase e:
    draw_lower_e(bob, lower_height)
    skip(bob, lower_height)

    # Draw lowercase g:
    draw_lower_g(bob, lower_height)
    skip(bob, lower_height)

    turtle.mainloop()
