'''
mbge.loader
=========

This module provides access to load data into the running scene.
'''
__author__ = 'Monster'

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

def copyMesh(self, targetLibraryName, meshNames):
    '''
    Copies an existing mesh.
    :param targetLibraryName
    :param meshNames - a list of meshes to be copied
    :return: a list of KX_MeshProxy with new unique names
    '''
    return bge.logic.LibNew(targetLibraryName, DATA_BLOCK_MESH, meshNames)

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