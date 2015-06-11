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
    '''
    Loads data from a file.
    :param blendFileName:
    :param dataBlockType:
    :keyword load_actions: Search for and load all actions in a given Scene
    :keyword verbose: Print debugging information
    :keyword load_scripts: Load text datablocks as well
    :keyword async: Asynchronous loading - DATA_BLOCK_SCENE only
    '''
    return bge.logic.LibLoad(
        blendFileName, dataBlockType,
        flags)

def injectData(self, libraryName, dataBlockType, data, **flags):
    '''
    Injects blend file data into the scene.
    :param libraryName:
    :param dataBlockType:
    :param data: bytes from a blend file
    :keyword load_actions: Search for and load all actions in a given Scene
    :keyword verbose: Print debugging information
    :keyword load_scripts: Load text datablocks as well
    :keyword async: Asynchronous loading - DATA_BLOCK_SCENE only
    :return: bge.types.KX_LibLoadStatus
    '''
    return bge.logic.LibLoad(
        libraryName, dataBlockType, data,
        flags)

def copyMesh(self, targetLibraryName, sourceLibraryNames):
    '''
    Copies an existing mesh.
    :param targetLibraryName
    :param sourceLibraryNames
    :return: a list of KX_MeshProxy
    '''
    return bge.logic.LibNew(targetLibraryName, DATA_BLOCK_MESH, sourceLibraryNames)

def unload(self, libraryName):
    '''
    Removes a library.
    :param libraryName:
    :return: True if the library was unloaded
    '''
    return bge.logic.LibFree(libraryName)

@property
def usedLibraryNames(self):
    'The names of the loaded libraries (readonly)'
    return bge.logic.LibList()

import mprop; mprop.init()