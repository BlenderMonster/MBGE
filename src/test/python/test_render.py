from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock, PropertyMock, MagicMock;

import sys

__author__ = 'Monster'


class TestRender(TestCase):

    def test_width_get(self):
        bge = Mock()

        bge.render.getWindowWidth = Mock(return_value=5)
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import render
            self.assertEqual(render.width, 5)

    def test_width_set(self):
        bge = Mock()

        bge.render.getWindowHeight = Mock(return_value=170)
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import render
            render.width = 1024

        bge.render.setWindowSize.assert_called_once_with(1024, 170)

    def test_height_get(self):
        bge = Mock()

        bge.render.getWindowHeight = Mock(return_value=17)
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import render
            self.assertEqual(render.height, 17)

    def test_width_set(self):
        bge = Mock()

        bge.render.getWindowWidth = Mock(return_value=33)
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import render
            render.height = 219

        bge.render.setWindowSize.assert_called_once_with(33, 219)

    def test_fullScreen_get(self):
        bge = Mock()

        bge.render.getFullScreen = Mock(return_value="abc")
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import render
            self.assertEqual(render.fullScreen, "abc")

    def test_fullScreen_set(self):
        bge = Mock()

        bge.render.getWindowWidth = Mock(return_value=33)
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import render
            render.fullScreen = True

        bge.render.setFullScreen.assert_called_once_with(True)

    def test_displayWidth_get(self):
        bge = Mock()

        bge.render.getDisplayDimensions = Mock(return_value=["x","y"])
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import render
            self.assertEqual(render.displayWidth, "x")

    def test_displayWidth_set(self):
        bge = Mock()

        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import render
            with self.assertRaises(AttributeError):
                render.displayWidth = 144

    def test_displayHeight_get(self):
        bge = Mock()

        bge.render.getDisplayDimensions = Mock(return_value=["x","y"])
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import render
            self.assertEqual(render.displayHeight, "y")

    def test_displayHeight_set(self):
        bge = Mock()

        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import render
            with self.assertRaises(AttributeError):
                render.displayHeight = 89

    def test_materialMode_get(self):
        bge = Mock()

        bge.render.getMaterialMode = Mock(return_value="a")
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import render
            self.assertEqual(render.materialMode, "a")

    def test_materialMode_set(self):
        bge = Mock()

        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import render
            render.materialMode = 33

        bge.render.setMaterialMode.assert_called_once_with(33)

    def test_saveFrameBuffer(self):
        bge = Mock()

        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import render
            render.saveFrameBuffer("filename")

        bge.render.makeScreenshot.assert_called_once_with("filename")

    def test_doc(self):
         with patch.dict('sys.modules', {'bge': Mock()}):
            from mbge import render
            print(dir(render))
            print(help(render))