import bge

def activateAll(self):
    'Activates all connected actuators'
    controller = bge.logic.getCurrentController()
    for actuator in controller.actuators:
        controller.activate(actuator)

def deactivateAll(self):
    'Activates all connected actuators'
    controller = bge.logic.getCurrentController()
    for actuator in controller.actuators:
        controller.deactivate(actuator)

import mprop; mprop.init()