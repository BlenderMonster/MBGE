'''
mbge.render
===========

This module provides access to the render settings
'''
import bge

KX_BLENDER_MULTITEX_MATERIAL = bge.render.KX_BLENDER_MULTITEX_MATERIAL
KX_BLENDER_GLSL_MATERIAL = bge.render.KX_BLENDER_GLSL_MATERIAL

@property
def width(self):
    'The render window''s width in pixels'
    return bge.render.getWindowWidth()

@width.setter
def width(self, width):
    bge.render.setWindowSize(width, bge.render.getWindowHeight())

@property
def height(self):
    'The render window''s height in pixels'
    return bge.render.getWindowHeight()

@height.setter
def height(self, height):
    bge.render.setWindowSize(bge.render.getWindowWidth(), height)

@property
def fullScreen(self):
    'True if the window is full screen'
    return bge.render.getFullScreen()

@fullScreen.setter
def fullScreen(self, enable):
    bge.render.setFullScreen(enable)

@property
def displayWidth(self):
    'The actual width of the physical display (e.g., the monitor) in Pixels (readonly).'
    return bge.render.getDisplayDimensions()[0]

@property
def displayHeight(self):
    'The actual height of the physical display (e.g., the monitor) in Pixels (readonly).'
    return bge.render.getDisplayDimensions()[1]

@property
def materialMode(self):
    'The material mode to use for OpenGL rendering. Changes will only affect newly created scenes.'
    return bge.render.getMaterialMode()

@materialMode.setter
def materialMode(self, materialMode):
    bge.render.setMaterialMode(materialMode)

def saveFrameBuffer(self, filename):
    '''
    Saves the current frame buffer to an image file
    :param filename: filename (can include // to be relative, can include a # to include an incrementor)
    '''
    bge.render.makeScreenshot(filename)

import mprop; mprop.init()