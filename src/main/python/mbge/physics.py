'''
mbge.logic
=========

This is a mock of the bge api's logic module.
It allows to use code completion against the bge modules.
The functions do not do anything.
'''
__author__ = 'Monster'

import types
import sys
import bge

DETECT_HIT = 0
DETECT_FACE_HIT = 1
DETECT_UV_FACE_HIT = 2

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

class Module(types.ModuleType):

    NORMAL_FACE_NORMAL = 1
    NORMAL_TOWARDS_SOURCE = 0

    def __init__(self, name):
        self.__name__ = name
        self._gravity = None

    @property
    def gravity(self):
        return self._gravity

    @gravity.setter
    def gravity(self, gravity):
        self._gravity = gravity
        return bge.logic.setGravity(gravity)

    @property
    def maxFrames(self):
        return bge.logic.getMaxPhysicsFrame()

    @maxFrames.setter
    def maxFrames(self, numberOfFrames):
        bge.logic.setMaxPhysicsFrame(numberOfFrames)

    @property
    def frameRate(self):
        return bge.logic.getPhysicsTicRate()

    @frameRate.setter
    def frameRate(self, rate):
        bge.logic.setPhysicsTicRate(rate)

    def detectHit(self, sourcePosition, targetPosition, distance,
                        filterProperty="", normalDirection=NORMAL_TOWARDS_SOURCE, excludeUnfiltered=False):
        detector = bge.logic.getCurrentScene().active_camera
        return Hit(*detector.rayCast(sourcePosition, targetPosition, distance,
                                     filterProperty, normalDirection, 1 if excludeUnfiltered else 0,
                                     DETECT_HIT))

    def detectFaceHit(self, sourcePosition, targetPosition, distance,
                        filterProperty="", normalDirection=NORMAL_TOWARDS_SOURCE, excludeUnfiltered=False):
        detector = bge.logic.getCurrentScene().active_camera
        return FaceHit(*detector.rayCast(sourcePosition, targetPosition, distance,
                                         filterProperty, normalDirection, 1 if excludeUnfiltered else 0,
                                         DETECT_FACE_HIT))

    def detectUvFaceHit(self, sourcePosition, targetPosition, distance,
                        filterProperty="", normalDirection=NORMAL_TOWARDS_SOURCE, excludeUnfiltered=False):
        detector = bge.logic.getCurrentScene().active_camera
        return UvFaceHit(*detector.rayCast(sourcePosition, targetPosition, distance,
                                           filterProperty, normalDirection, 1 if excludeUnfiltered else 0,
                                           DETECT_UV_FACE_HIT))

module = Module(__name__)
module._module = sys.modules[module.__name__]
module._pmodule = module
sys.modules[module.__name__] = module