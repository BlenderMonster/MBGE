from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock, PropertyMock, MagicMock;

import sys

__author__ = 'Monster'


class TestContext(TestCase):

    def test_getController(self):
        bge = Mock()

        bge.logic.getCurrentController = Mock(return_value="controller")
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import context
            self.assertEqual(context.controller, "controller")

    def test_getOwner(self):
        bge = Mock()

        bge.logic.getCurrentController().owner = "owner"
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import context
            self.assertEqual(context.owner, "owner")

    def test_getScene(self):
        bge = Mock()

        bge.logic.getCurrentScene = Mock(return_value="scene")
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import context
            self.assertEqual(context.scene, "scene")

    def test_getScenes(self):
        bge = Mock()

        bge.logic.getSceneList = Mock(return_value="[scene]")
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import context
            self.assertEqual(context.scenes, "[scene]")

    def test_doc(self):
        bge = Mock()

        bge.logic.getSceneList = Mock(return_value="[scene]")
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import context
            print(dir(context))
            print(help(context))
