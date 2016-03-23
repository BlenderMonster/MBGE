'''
mbge.storage
=========

This module provides access to attributes related to stereo display.
'''
__author__ = 'Monster'

import bge

@property
def focalLength(self):
    'The focal length for stereo mode.'
    return bge.render.getFocalLength()

@focalLength.setter
def focalLength(self, focalLength):
    bge.render.setFocalLength(focalLength)

@property
def eyeSeparation(self):
    'The current eye separation for stereo mode.'
    return bge.render.getEyeSeparation()

@eyeSeparation.setter
def eyeSeparation(self, eyeSeparation):
    bge.render.setEyeSeparation(eyeSeparation)


import mprop; mprop.init()