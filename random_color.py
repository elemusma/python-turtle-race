import turtle as t
import random

class RandomTuple():

    tim = t.Turtle()
    t.colormode(255)

    def random_tuple(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        generated_tuple = (r, g, b)
        return generated_tuple