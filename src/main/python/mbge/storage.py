'''
bge.logic
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

    @property
    def storedContent(self):
        return bge.logic.globalDict

    @storedContent.setter
    def storedContent(self, content):
        bge.logic.globalDict = content

    def loadFromFile(self):
        bge.logic.loadGlobalDict()

    def saveToFile(self):
        bge.logic.saveGlobalDict()

module = Module(__name__)
module._module = sys.modules[module.__name__]
module._pmodule = module
sys.modules[module.__name__] = module