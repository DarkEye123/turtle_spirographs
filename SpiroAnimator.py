import math
import logging
import turtle
import random
from Spiro import Spiro


class SpiroAnimator:
    def __init__(self, spiros=5):
        self.deltaT = 10  # timer in miliseconds
        self.width = turtle.window_width()
        self.height = turtle.window_height()
        self.spiros = []
        self.n_spiros = spiros
        for i in range(spiros):
            rparams = self.gen_random_params()
            logging.info("created spiro with params %s" % rparams)
            spiro = Spiro(*rparams)
            self.spiros.append(spiro)
        turtle.ontimer(self.update, self.deltaT)

    def gen_random_params(self):
        width, height = self.width, self.height
        R = random.randint(50, min(width, height) // 2)
        r = random.randint(10, 9 * R // 10)
        l = random.uniform(0.1, 0.9)
        xc = random.randint(-width // 8, width // 8)
        yc = random.randint(-height // 8, height // 8)
        logging.info("seed x(%d, %d), y(%d,%d)" %(-width // 8, width // 8, -height // 8, height // 8))
        col = (random.random(),
               random.random(),
               random.random())
        return [xc, yc, col, R, r, l]

    def restart(self):
        for spiro in self.spiros:
            spiro.t.clear()
            rparams = self.gen_random_params()
            spiro.setparams(*rparams)
            spiro.restart()

    def update(self):
        completed = 0
        for spiro in self.spiros:
            spiro.update()
            if spiro.completed:
                completed+=1
        if completed == self.n_spiros:
            self.restart()
        turtle.ontimer(self.update, self.deltaT)

    def toogle_turtles(self):
        for spiro in self.spiros:
            spiro.toogle_turtle()
