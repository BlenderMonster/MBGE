import types
import sys
import bge

class Context(types.ModuleType):
    @property
    def controller(self):
        return bge.logic.getCurrentController()

    @property
    def owner(self):
        return bge.logic.getCurrentController().owner

    @property
    def scene(self):
        return bge.logic.getCurrentScene()

    @property
    def scenes(self):
        return bge.logic.getSceneList()

module = Context(__name__)
module._module = sys.modules[module.__name__]
module._pmodule = module
sys.modules[module.__name__] = module