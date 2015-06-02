'''
bge.logic
=========

This is a mock of the bge api's logic module.
It allows to use code completion against the bge modules.
The functions do not do anything.
'''
__author__ = 'Monster'

import bge

globalDict = bge.logic.globalDict

def getCurrentController():
    pass

def getCurrentScene():
    pass

def getSceneList():
    pass

def loadGlobalDict():
    pass

def saveGlobalDict():
    pass

def startGame(blend):
    pass

def endGame():
    pass

def restartGame():
    pass

def LibLoad(blend, type, data, load_actions=False, verbose=False, load_scripts=True, async=False):
    pass

def LibNew(name, type, data):
    pass

def LibFree(name):
    pass

def LibList():
    pass

def addScene(name, overlay=1):
    pass

def sendMessage(subject, body="", to="", message_from=""):
    pass

def setGravity(gravity):
    pass

def getSpectrum():
    pass

def getMaxLogicFrame():
    pass

def setMaxLogicFrame(maxlogic):
    pass

def setMaxLogicFrame(maxlogic):
    pass

def getMaxPhysicsFrame():
    pass

def setMaxPhysicsFrame(maxphysics):
    pass

def getLogicTicRate():
    pass

def setLogicTicRate(ticrate):
    pass

def getPhysicsTicRate():
    pass

def setPhysicsTicRate(ticrate):
    pass

def getExitKey():
    pass

def setExitKey(key):
    pass

def NextFrame():
    pass

def expandPath(path):
    pass

def getAverageFrameRate():
    pass

def getBlendFileList(path = "//"):
    pass

def getBlendFileList(path = "//"):
    pass

def getRandomFloat():
    pass

def PrintGLInfo():
    pass

def PrintMemInfo():
    pass

def getProfileInfo():
    pass

class Module(object):
    pass

module = Module()
module.__dict__ = globals()

for k, v in list(module.__dict__.items()):
    if isinstance(v, property):
        setattr(Module, k, v)
        del module.__dict__[k]