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


DATA_BLOCK_ACTION = "Action"
DATA_BLOCK_MESH = "Mesh"
DATA_BLOCK_SCENE = "Scene"

def loadFile(self, blendFileName, dataBlockType, **flags):
    return bge.logic.LibLoad(
        blendFileName, dataBlockType,
        flags)

def injectData(self, libraryName, dataBlockType, data, **flags):
    return bge.logic.LibLoad(
        libraryName, dataBlockType, data,
        flags)

def copy(self, targetLibraryName, dataBlockType, sourceLibraryNames):
    return bge.logic.LibNew(targetLibraryName, dataBlockType, sourceLibraryNames)

def unload(self, libraryName):
    return bge.logic.LibFree(libraryName)

@property
def usedLibraryNames(self):
    return bge.logic.LibList()

import mprop; mprop.init()