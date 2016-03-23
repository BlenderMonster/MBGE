import bge

@property
def allPositive(self):
    ':return: true if all sensors are positive'
    for sensor in bge.logic.getCurrentController().sensors:
        if not sensor.positive:
            return False
    return True

@property
def onePositive(self):
    ':return: true if at least one sensors is positive'
    for sensor in bge.logic.getCurrentController().sensors:
        if sensor.positive:
            return True
    return False

@property
def hitObjects(self):
    objects = []
    for sensor in bge.logic.getCurrentController().sensors:
        try:
            objects = objects + list(sensor.hitObjectList)
        except AttributeError:
            try:
                objects.append(sensor.hitObject)
            except AttributeError:
                continue
    return objects

@property
def hitPositions(self):
    positions = []
    for sensor in bge.logic.getCurrentController().sensors:
        try:
            positions = positions + (sensor.hitPosition)
        except AttributeError:
            try:
                positions.append(sensor.hitPosition)
            except AttributeError:
                continue
    return positions

@property
def bodies(self):
    foundBodies = []
    for sensor in bge.logic.getCurrentController().sensors:
        try:
            foundBodies = foundBodies + list(sensor.bodies)
        except AttributeError:
            continue
    return foundBodies

import mprop; mprop.init()