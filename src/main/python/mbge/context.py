import types
import sys
import bge

@property
def controller(self):
    return bge.logic.getCurrentController()

@property
def owner(self):
    return bge.logic.getCurrentController().owner

@property
def scene(self):
    return bge.logic.getCurrentScene()

@property
def scenes(self):
    return bge.logic.getSceneList()

import mprop; mprop.init()