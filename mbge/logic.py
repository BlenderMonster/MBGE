'''
mbge.logic
=========

This module provides access to the games logic settings.
'''
__author__ = 'Monster'

import bge

@property
def maxFrames(self):
    'The maximum number of logic frames per render frame.'
    return bge.logic.getMaxLogicFrame()

@maxFrames.setter
def maxFrames(self, numberOfFrames):
    bge.logic.setMaxLogicFrame(numberOfFrames)

@property
def frameRate(self):
    'The logic update frequency per second.'
    return bge.logic.getLogicTicRate()

@frameRate.setter
def frameRate(self, rate):
    'The logic update frequency is the number of times logic bricks are executed every second.'
    bge.logic.setLogicTicRate(rate)

@property
def exitKey(self):
    'Gets the key code of the key used to exit the game session.'
    return bge.logic.getExitKey()

@exitKey.setter
def exitKey(self, keyCode):
    bge.logic.setExitKey(keyCode)

def renderNextFrame(self):
    'Forces the renderer to render the current frame'
    bge.logic.NextFrame

@property
def averageFrameRate(self):
    'The estimated average frame rate in frames per second (readonly)'
    bge.logic.getAverageFrameRate()

import mprop; mprop.init()