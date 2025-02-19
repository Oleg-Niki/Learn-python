import turtle
import math

def skip(t, distance):
    """Lift pen, move forward 'distance', then put pen down."""
    t.penup()
    t.forward(distance)
    t.pendown()

def arc(t, r, angle):
    """Draw an arc with radius r, through 'angle' degrees."""
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # A slight turn before/after to reduce error of linear approximation
    t.left(step_angle / 2)
    for _ in range(n):
        t.forward(step_length)
        t.left(step_angle)
    t.right(step_angle / 2)

def circle(t, r):
    """Draw a full circle with radius r."""
    arc(t, r, 360)

def draw_capital_o(t, n):
    """
    Draw a capital 'O' of total height 2n.
    We move up n so the bottom of the circle sits on the baseline,
    draw the circle, then come back to baseline and skip 2n horizontally.
    """
    t.penup()
    t.left(90)
    t.forward(n)
    t.right(90)
    t.pendown()
    circle(t, n)           # Circle of radius n => 2n tall
    # Return to baseline
    t.penup()
    t.right(90)
    t.forward(n)
    t.left(90)
    t.pendown()
    skip(t, 2*n)           # Move to the start of the next letter

def draw_lower_l(t, n):
    """
    Draw a lowercase 'l' of height n, starting at baseline and ending
    at baseline, skipping half 'n' horizontally at the end.
    """
    t.pendown()
    t.left(90)
    t.forward(n)           # vertical stroke
    t.backward(n)
    t.right(90)
    skip(t, n/2)           # space to next letter

def draw_lower_e(t, n):
    """
    Draw a lowercase 'e' of height n, starting at baseline and ending
    on the baseline. We move up to midline, make a partial arc, and come back.
    """
    # Move up to the midline
    t.penup()
    t.left(90)
    t.forward(n/2)
    t.right(90)
    t.pendown()
    # Small horizontal stroke
    t.forward(n/3)
    # 180° arc downward for the loop
    arc(t, n/3, -180)
    # Now we’re at the baseline, facing west
    t.right(180)           # turn to face east again
    skip(t, n/2)           # skip horizontally to next letter

def draw_lower_g(t, n):
    """
    Draw a lowercase 'g' of height n, with a descender. 
    Start at baseline, go up to midline, draw the loop (like 'e'), 
    then go below baseline and hook back up.
    """
    # Move up to the midline
    t.penup()
    t.left(90)
    t.forward(n/2)
    t.right(90)
    t.pendown()
    # Small horizontal stroke
    t.forward(n/3)
    # 180° arc downward for the loop
    arc(t, n/3, -180)
    # Now at baseline, facing west
    # Descender below baseline
    t.left(90)
    t.forward(n/2)         # go down
    # Draw a bigger hook (180° arc)
    arc(t, n/4, -180)
    # Come back up
    t.forward(n/2)
    t.right(90)            # face east again
    skip(t, n/2)           # move to the right

def main():
    bob = turtle.Turtle()
    bob.speed('slow')  # adjust as desired

    # Draw "Oleg" in a row
    # Capital O: 2n tall => pass n=30 for a 60-pixel tall letter
    draw_capital_o(bob, 30)
    # Lowercase letters: pass the same 'n' so their x-height is consistent
    draw_lower_l(bob, 30)
    draw_lower_e(bob, 30)
    draw_lower_g(bob, 30)

    turtle.mainloop()

if __name__ == '__main__':
    main()
