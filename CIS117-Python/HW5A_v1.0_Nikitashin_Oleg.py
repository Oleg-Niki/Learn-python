"""Modified letters.py
This code is based on Ch4 examples by Allen Downey.
It draws the name "Oleg" with a capital O and lower-case letters for l, e, and g.
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
    dist = sqrt(x ** 2 + y ** 2)
    lt(t, angle)
    fdbk(t, dist)
    rt(t, angle)

def vshape(t, n, height):
    diagonal(t, -n / 2, height * n)
    diagonal(t, n / 2, height * n)

def bump(t, n, height):
    stump(t, n * height)
    arc(t, n / 2.0, 180)
    lt(t)
    fdlt(t, n * height + n)

# LETTER DRAWING FUNCTIONS
def draw_a(t, n):
    diagonal(t, n / 2, 2 * n)
    beam(t, n, 1)
    skip(t, n)
    diagonal(t, -n / 2, 2 * n)

def draw_b(t, n):
    bump(t, n, 1)
    bump(t, n, 0)
    skip(t, n / 2)

def draw_c(t, n):
    hangman(t, n, 2)
    fd(t, n)

def draw_d(t, n):
    bump(t, 2 * n, 0)
    skip(t, n)

def draw_ef(t, n):
    hangman(t, n, 2)
    hangman(t, n, 1)

def draw_e(t, n):
    draw_ef(t, n)
    fd(t, n)

def draw_f(t, n):
    draw_ef(t, n)
    skip(t, n)

def draw_g(t, n):
    hangman(t, n, 2)
    fd(t, n / 2)
    beam(t, n / 2, 2)
    fd(t, n / 2)
    post(t, n)

def draw_h(t, n):
    post(t, 2 * n)
    hangman(t, n, 1)
    skip(t, n)
    post(t, 2 * n)

def draw_i(t, n):
    beam(t, n, 2)
    fd(t, n / 2)
    post(t, 2 * n)
    fd(t, n / 2)

def draw_j(t, n):
    beam(t, n, 2)
    arc(t, n / 2, 90)
    fd(t, 3 * n / 2)
    skip(t, -2 * n)
    rt(t)
    skip(t, n / 2)

def draw_k(t, n):
    post(t, 2 * n)
    stump(t, n, 180)
    vshape(t, 2 * n, 0.5)
    fdlt(t, n)
    skip(t, n)

def draw_l(t, n):
    post(t, 2 * n)
    fd(t, n)

def draw_n(t, n):
    post(t, 2 * n)
    skip(t, n)
    diagonal(t, -n, 2 * n)
    post(t, 2 * n)

def draw_m(t, n):
    post(t, 2 * n)
    draw_v(t, n)
    post(t, 2 * n)

def draw_o(t, n):
    skip(t, n)
    circle(t, n)
    skip(t, n)

def draw_p(t, n):
    bump(t, n, 1)
    skip(t, n / 2)

def draw_q(t, n):
    draw_o(t, n)
    diagonal(t, -n / 2, n)

def draw_r(t, n):
    draw_p(t, n)
    diagonal(t, -n / 2, n)

def draw_s(t, n):
    fd(t, n / 2)
    arc(t, n / 2, 180)
    arc(t, n / 2, -180)
    fdlt(t, n / 2, -90)
    skip(t, 2 * n)
    lt(t)

def draw_t(t, n):
    beam(t, n, 2)
    skip(t, n / 2)
    post(t, 2 * n)
    skip(t, n / 2)

def draw_u(t, n):
    post(t, 2 * n)
    fd(t, n)
    post(t, 2 * n)

def draw_v(t, n):
    skip(t, n / 2)
    diagonal(t, -n / 2, 2 * n)
    diagonal(t, n / 2, 2 * n)
    skip(t, n / 2)

def draw_w(t, n):
    draw_v(t, n)
    draw_v(t, n)

def draw_x(t, n):
    diagonal(t, n, 2 * n)
    skip(t, n)
    diagonal(t, -n, 2 * n)

def draw_y(t, n):
    skip(t, n / 2)
    stump(t, n)
    vshape(t, n, 1)
    rt(t)
    fdlt(t, n)
    skip(t, n / 2)

def draw_z(t, n):
    beam(t, n, 2)
    diagonal(t, n, 2 * n)
    fd(t, n)

def draw_(t, n):
    # Draw a space
    skip(t, n)

# MODIFIED MAIN BLOCK TO DRAW THE NAME "Oleg"
if __name__ == '__main__':
    # Adjust these sizes to change the appearance of capital vs. lower-case letters.
    capital_size = 40     # Full-size for the first letter (capital)
    lowercase_size = 20   # Half-size for the lower-case letters

    bob = turtle.Turtle()

    # Draw capital letter 'O'
    draw_o(bob, capital_size)
    skip(bob, capital_size)

    # Draw lower-case letters 'l', 'e', 'g'
    draw_l(bob, lowercase_size)
    skip(bob, lowercase_size)
    draw_e(bob, lowercase_size)
    skip(bob, lowercase_size)
    draw_g(bob, lowercase_size)
    skip(bob, lowercase_size)

    turtle.mainloop()
