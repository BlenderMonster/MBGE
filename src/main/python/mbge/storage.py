'''
mbge.storage
=========

This module provides build-in store/restore and save/load.
'''
__author__ = 'Monster'

import bge

@property
def storedContent(self):
    'A storage that can be saved to file. Store marshallable objects only.'
    return bge.logic.globalDict

@storedContent.setter
def storedContent(self, content):
    bge.logic.globalDict = content

def loadFromFile(self):
    bge.logic.loadGlobalDict()

def saveToFile(self):
    bge.logic.saveGlobalDict()

import mprop; mprop.init()