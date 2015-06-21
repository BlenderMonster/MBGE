'''
mbge.physics
============

This module provides access to the physics settings
including face detection.
'''
__author__ = 'Monster'

import bge

_DETECT_HIT = 0
_DETECT_FACE_HIT = 1
_DETECT_UV_FACE_HIT = 2

class Hit(object):
    def __init__(self, hitObject, hitPosition, HitNormal):
        self.object = hitObject
        self.position = hitPosition
        self.normal = HitNormal

    def __len__(self):
        return 1 if self.position is not None else 0

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

def detectHit(self, start, towards, distance=0, **kwargs):
    '''
    Detects the cross point of an imaginary line from "start" towards "towards" and the
    first face the line crosses. The resulting Hit contains the object the face belongs to as well as
    the hit point and the face normal.
    The distance to measure can be modified via the "distance" parameter. If not set the
    measure ends at "towards".

    :param start: position (or KX_GameObject) to measure from
    :param towards: position (or KX_GameObject) to measure towards to
    :param distance: distance to detect along the line (optional)
    :keyword property: property name that an hit object needs to have
    :keyword normalDirection: NORMAL_TOWARDS_SOURCE, NORMAL_FACE_NORMAL
    :keyword xray: True = ignores faces of objects without filter property
                   False = faces of objects without filter property block the measure
    :return: Hit
    '''
    detector = bge.logic.getCurrentScene().active_camera
    return Hit(*detector.rayCast(start, towards, distance,
                                kwargs.get("property", ""),
                                kwargs.get('normalDirection', NORMAL_TOWARDS_SOURCE),
                                1 if kwargs.get('xray', False) else 0,
                                 _DETECT_HIT))

def detectFaceHit(self, sourcePosition, targetPosition, distance=0, **kwargs):
    '''
    Detects the cross point of an imaginary line from "start" towards "towards" and the
    first face the line crosses. The resulting FaceHit contains the object the face belongs to
    as well as the hit point, the face normal and the face hit.
    The distance to measure can be modified via the "distance" parameter. If not set the
    measure ends at "towards".

    :param start: position (or KX_GameObject) to measure from
    :param towards: position (or KX_GameObject) to measure towards to
    :param distance: distance to detect along the line (optional)
    :keyword property: property name that an hit object needs to have
    :keyword normalDirection: NORMAL_TOWARDS_SOURCE, NORMAL_FACE_NORMAL
    :keyword xray: True = ignores faces of objects without filter property
                   False = faces of objects without filter property block the measure
    :return: FaceHit
    '''

    detector = bge.logic.getCurrentScene().active_camera
    return FaceHit(*detector.rayCast(sourcePosition, targetPosition, distance,
                                kwargs.get("property", ""),
                                kwargs.get('normalDirection', NORMAL_TOWARDS_SOURCE),
                                1 if kwargs.get('xray', False) else 0,
                                _DETECT_FACE_HIT))

def detectUvFaceHit(self, sourcePosition, targetPosition, distance, **kwargs):
    '''
    Detects the cross point of an imaginary line from "start" towards "towards" and the
    first face the line crosses. The resulting UvFaceHit contains the object the face belongs to
    as well as the hit point, the face normal, face hit and the uv coordinates in the primary uv set.
    The distance to measure can be modified via the "distance" parameter. If not set the
    measure ends at "towards".

    :param start: position (or KX_GameObject) to measure from
    :param towards: position (or KX_GameObject) to measure towards to
    :param distance: distance to detect along the line (optional)
    :keyword property: property name that an hit object needs to have
    :keyword normalDirection: NORMAL_TOWARDS_SOURCE, NORMAL_FACE_NORMAL
    :keyword xray: True = ignores faces of objects without filter property
                   False = faces of objects without filter property block the measure
    :return: UvFaceHit
    '''
    detector = bge.logic.getCurrentScene().active_camera
    return UvFaceHit(*detector.rayCast(sourcePosition, targetPosition, distance,
                                kwargs.get("property", ""),
                                kwargs.get('normalDirection', NORMAL_TOWARDS_SOURCE),
                                1 if kwargs.get('xray', False) else 0,
                                _DETECT_UV_FACE_HIT))

import mprop; mprop.init()