import types
import sys
import bge

@property
def x(self):
    'mouse cursor position x axis in pixels'
    return int(round(bge.logic.mouse.position[0] * bge.render.getWindowWidth()))

@x.setter
def x(self, x):
    bge.render.setMousePosition(x, self.y)

@property
def y(self):
    'mouse cursor position y axis in pixels'
    return int(round(bge.logic.mouse.position[1]*bge.render.getWindowHeight()))

@y.setter
def y(self, y):
    bge.render.setMousePosition(self.x, y)


import mprop; mprop.init()