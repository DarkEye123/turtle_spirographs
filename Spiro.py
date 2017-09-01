import math
import turtle
import logging
from math import gcd


class Spiro:
    def __init__(self, xc, yc, col, R, r, l):
        self.t = turtle.Turtle()
        self.t.shape('arrow')
        self.step = 5
        self.completed = False

        self.xc = xc
        self.yc = yc
        self.R = int(R)
        self.r = int(r)
        self.l = l

        gcd_val = gcd(self.r, self.R)  # greatest common divisor

        # this is needed to prevent repeating over same path
        self.nRot = self.r // gcd_val  # basically gives me how much revolutions is needed to make curve repeat itself

        # radii ratio
        self.k = r / float(R)

        self.t.color(*col)

        # angle in radians
        self.angle = 0.0

        self.restart()

    def _generate_next_coods(self, R, k, l, angle):
        # my nice hypotrochoids and epitrochoids
        x = R * ((1 - k) * math.cos(angle) + l * k * math.cos((1 - k) * angle / k))
        y = R * ((1 - k) * math.sin(angle) - l * k * math.sin((1 - k) * angle / k))
        print(R, k, l, angle)
        return x, y

    def setparams(self, xc, yc, col, R, r, l):
        self.xc = xc
        self.yc = yc
        self.col = col
        self.R = R
        self.r = r
        self.l = l

    def restart(self):
        self.t.clear()
        self.completed = False
        self.t.up()
        self.angle = 0.0

        x, y = self._generate_next_coods(self.R, self.k, self.l, self.angle)

        self.t.setpos(self.xc + x, self.yc + y)
        logging.info("restart x %d, y %d" % (self.xc + x, self.yc + y))
        self.t.down()

    def draw(self):
        R, k, l = self.R, self.k, self.l
        for i in range(0, 360 * self.nRot + 1, self.step):
            angle = math.radians(i)
            x, y = self._generate_next_coods(R, k, l, angle)
            self.t.setpos(self.xc + x, self.yc + y)
        self.t.hideturtle()  # we are finished with drawing

    def restart_draw(self):
        self.restart()
        self.draw()

    def toogle_turtle(self):
        if self.t.isvisible():
            self.t.hideturtle()
        else:
            self.t.showturtle()

    def update(self):
        if self.completed:
            return
        self.angle += self.step
        r_angle = math.radians(self.angle)
        x, y = self._generate_next_coods(self.R, self.k, self.l, r_angle)
        self.t.setpos(self.xc + x, self.yc + y)
        #logging.info("update x %d, y %d" % (self.xc + x, self.yc + y))
        if self.angle >= 360 * self.nRot:
            self.completed = True
            self.t.hideturtle()


