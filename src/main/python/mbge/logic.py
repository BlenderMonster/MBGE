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

@property
def maxFrames(self):
    '''
    Gets the maximum number of logic frames per render frame.
    :returns: maximum number of logic frames per render frame'''
    return bge.logic.getMaxLogicFrame()

@maxFrames.setter
def maxFrames(self, numberOfFrames):
    '''
    Sets the maximum number of logic frames per render frame.
    :param numberOfFrames: maximum number of logic frames per render frame
    '''
    bge.logic.setMaxLogicFrame(numberOfFrames)

@property
def frameRate(self):
    '''
    Gets the logic update frequency per second.
    :return: frames per second
    '''
    return bge.logic.getLogicTicRate()

@frameRate.setter
def frameRate(self, rate):
    '''
    Sets the logic update frequency.
    The logic update frequency is the number of times logic bricks are executed every second. The default is 60 Hz.
    :param rate: frames per second
    '''
    bge.logic.setLogicTicRate(rate)

@property
def exitKey(self):
    '''
    Gets the key used to exit the game session
    :return: key-code (int)
    '''
    return bge.logic.getExitKey()

@exitKey.setter
def exitKey(self, keyCode):
    '''
    Sets the key used to exit the game session
    :param keyCode: key-code (int, default  bge.events.ESCKEY)
    '''
    bge.logic.setExitKey(keyCode)

def renderNextFrame(self):
    bge.logic.NextFrame

@property
def averageFrameRate(self):
    '''
    :return: The estimated average frame rate in frames per second (gloat)
    '''
    bge.logic.getAverageFrameRate()

import mprop; mprop.init()