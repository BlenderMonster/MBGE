'''
mbge.physics
============

This module provides access to the physics settings
including face detection.
'''
__author__ = 'Monster'

import types
import sys
import bge

_DETECT_HIT = 0
_DETECT_FACE_HIT = 1
_DETECT_UV_FACE_HIT = 2

class Hit(object):
    def __init__(self, hitObject, hitPosition, HitNormal):
        self.object = hitObject
        self.position = hitPosition
        self.normal = HitNormal

    def __str__(self):
        return "<{}>{{object: {}, position: {}, normal {}}}".format(
            self.__class__.__name__, self.object, self.position, self.normal)

class FaceHit(Hit):
    def __init__(self, hitObject, hitPosition, HitNormal, hitFace):
        super().__init__(hitObject, hitPosition, HitNormal)
        self.face = hitFace

    def __str__(self):
        return "<{}>{{object: {}, position: {}, normal {}, face: {}}}".format(
            self.__class__.__name__, self.object, self.position, self.normal, self.face)

class UvFaceHit(FaceHit):
    def __init__(self, hitObject, hitPosition, HitNormal, hitFace, hitUv):
        super().__init__(hitObject, hitPosition, HitNormal, hitFace)
        self.uv = hitUv

    def __str__(self):
        return "<{}>{{object: {}, position: {}, normal {}, face: {}, uv: {}}}".format(
            self.__class__.__name__, self.object, self.position, self.normal, self.face, self.uv)

NORMAL_FACE_NORMAL = 1
NORMAL_TOWARDS_SOURCE = 0


_gravity = None

@property
def gravity(self):
    'The current gravity. Can only be returned when explicitly set with this property. Otherwise it returns None.'
    return self._gravity

@gravity.setter
def gravity(self, gravity):
    self._gravity = gravity
    return bge.logic.setGravity(gravity)

@property
def maxFrames(self):
    'The maximum number of physics frames per render frame.'
    return bge.logic.getMaxPhysicsFrame()

@maxFrames.setter
def maxFrames(self, numberOfFrames):
    bge.logic.setMaxPhysicsFrame(numberOfFrames)

@property
def frameRate(self):
    'The physics update frequency per second.'
    return bge.logic.getPhysicsTicRate()

@frameRate.setter
def frameRate(self, rate):
    bge.logic.setPhysicsTicRate(rate)

def detectHit(self, sourcePosition, targetPosition, distance,
              **kwargs):
    'Detects the first face that gets hit by a line from source along target over distance.'
    detector = bge.logic.getCurrentScene().active_camera
    return Hit(*detector.rayCast(sourcePosition, targetPosition, distance,
                                 kwargs.get("filterProperty", ""),
                                 kwargs.get('normalDirection', NORMAL_TOWARDS_SOURCE),
                                 1 if kwargs.get('excludeUnfiltered', False) else 0,
                                 _DETECT_HIT))

def detectFaceHit(self, sourcePosition, targetPosition, distance,
                    filterProperty="", normalDirection=NORMAL_TOWARDS_SOURCE, excludeUnfiltered=False):
    detector = bge.logic.getCurrentScene().active_camera
    return FaceHit(*detector.rayCast(sourcePosition, targetPosition, distance,
                                     filterProperty, normalDirection, 1 if excludeUnfiltered else 0,
                                     _DETECT_FACE_HIT))

def detectUvFaceHit(self, sourcePosition, targetPosition, distance,
                    filterProperty="", normalDirection=NORMAL_TOWARDS_SOURCE, excludeUnfiltered=False):
    detector = bge.logic.getCurrentScene().active_camera
    return UvFaceHit(*detector.rayCast(sourcePosition, targetPosition, distance,
                                       filterProperty, normalDirection, 1 if excludeUnfiltered else 0,
                                       _DETECT_UV_FACE_HIT))

import mprop; mprop.init()