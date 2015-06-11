from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock, PropertyMock, MagicMock;

import sys

__author__ = 'Monster'


class TestPhysics(TestCase):

    def test_loadFile(self):
        bge = Mock()

        bge.logic.LibLoad = Mock(return_value=3)
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import loader
            self.assertEqual(loader.loadFile("blend", loader.DATA_BLOCK_ACTION,
                                             load_actions=True, verbose=True, load_scripts=True, async=True ), 3)
        bge.logic.LibLoad.assert_called_once_with("blend", loader.DATA_BLOCK_ACTION,
                                                  {"load_actions": True, "verbose": True,
                                                   "load_scripts": True, "async": True} )

    def test_injectData(self):
        bge = Mock()

        bge.logic.LibLoad = Mock(return_value=2)
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import loader
            self.assertEqual(loader.injectData("mesh", loader.DATA_BLOCK_MESH,  bytearray(),
                                             load_actions=True, verbose=True, load_scripts=True, async=True ), 2)
        bge.logic.LibLoad.assert_called_once_with("mesh", loader.DATA_BLOCK_MESH, bytearray(),
                                                  {"load_actions": True, "verbose": True,
                                                   "load_scripts": True, "async": True} )

    def test_copy(self):
        bge = Mock()

        bge.logic.LibNew = Mock(return_value=4)
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import loader
            self.assertEqual(loader.copyMesh("copied",  ["a", "b"]), 4)
        bge.logic.LibNew.assert_called_once_with("copied", loader.DATA_BLOCK_MESH, ["a", "b"] )

    def test_unload(self):
        bge = Mock()

        bge.logic.LibFree = Mock(return_value=9)
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import loader
            self.assertEqual(loader.unload("unload"), 9)
        bge.logic.LibFree.assert_called_once_with("unload" )

    def test_doc(self):
         with patch.dict('sys.modules', {'bge': Mock()}):
            from mbge import loader
            print(dir(loader))
            print(help(loader))