'''
mbge.mouse
==========

This module provides access to common mouse functions.
'''
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

@property
def visible(self):
    'The visibility of the system mouse cursor'
    return bge.render.mouse.visible

@visible.setter
def visible(self, visible):
    bge.logic.mouse.visible = visible

@property
def events(self):
    'All current mouse events (readonly)'
    return bge.render.mouse.events

import mprop; mprop.init()