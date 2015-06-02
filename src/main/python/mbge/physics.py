'''
mbge.logic
=========

This is a mock of the bge api's logic module.
It allows to use code completion against the bge modules.
The functions do not do anything.
'''
__author__ = 'Monster'

import types
import sys
import bge

class Module(types.ModuleType):
    def __init__(self, name):
        self.__name__ = name
        self._gravity = None

    @property
    def gravity(self):
        return self._gravity

    @gravity.setter
    def gravity(self, gravity):
        self._gravity = gravity
        return bge.logic.setGravity(gravity)

    @property
    def maxFrames(self):
        return bge.logic.getMaxPhysicsFrame()

    @maxFrames.setter
    def maxFrames(self, numberOfFrames):
        bge.logic.setMaxPhysicsFrame(numberOfFrames)

    @property
    def frameRate(self):
        return bge.logic.getPhysicsTicRate()

    @frameRate.setter
    def frameRate(self, rate):
        bge.logic.setPhysicsTicRate(rate)

module = Module(__name__)
module._module = sys.modules[module.__name__]
module._pmodule = module
sys.modules[module.__name__] = module