'''
mbge.file
=========

This module provides access to files.
'''
__author__ = 'Monster'

import bge

def expandPath(path):
    'Converts a blender internal path into a proper file system path.'
    return bge.logic.expandPath(path)

def getBlendFileList(path = "//"):
    'Returns a list of blend files in the path.'
    return bge.logic.getBlendFileList(path)

