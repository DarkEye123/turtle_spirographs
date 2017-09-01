import argparse
import turtle
from datetime import datetime
from Spiro import Spiro
from SpiroAnimator import SpiroAnimator
import logging
from PIL import Image

def save_drawing():
    turtle.hideturtle()
    date_str = (datetime.now()).strftime("%d%b%Y-%H%M%S")
    file_name = 'spiro-'+date_str
    logging.info("Saving drawing to %s.eps/png" % file_name)
    canvas = turtle.getcanvas()
    canvas.postscript(file=file_name+'.eps')
    img = Image.open(file_name+'.eps')
    img.save(file_name+".png", 'png')
    turtle.showturtle()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--sparams', nargs=3, dest='sparams', required=False,
                        help="The three arguments in sparams: R, r, l.")
    parser.add_argument('--count', dest='count', required=False, default=5, type=int, metavar='int',
                        help="Count of the spirographs drawn on the canvas simultaneously")
    args = parser.parse_args()
    turtle.setup(width=0.8)
    turtle.shape('turtle')
    turtle.title('Spirographs playground')
    turtle.onkey(save_drawing, 's')
    turtle.listen()
    turtle.hideturtle()

    if args.sparams:
        params = [float(x) for x in args.sparams]
        col = (0.0, 0.0, 0.0)
        spiro = Spiro(0, 0, col, *params)
        turtle.onkey(spiro.restart_draw, 'r')
        turtle.onkey(spiro.toogle_turtle, 't')
        spiro.draw()
    else:
        spiroAnim = SpiroAnimator(args.count)
        turtle.onkey(spiroAnim.toogle_turtles, 't')
        turtle.onkey(spiroAnim.restart, 'r')

    turtle.mainloop()
