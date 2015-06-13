from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock, PropertyMock, MagicMock;

import sys

__author__ = 'Monster'


class TestMouse(TestCase):

    def test_x_get(self):
        bge = Mock()

        bge.render.getWindowWidth =  Mock(return_value=2)
        bge.logic.mouse.position = [3, 5]
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import mouse
            self.assertEqual(mouse.x, 2*3)

    def test_x_set(self):
        bge = Mock()

        bge.logic.mouse.position = [2, 3]
        bge.render.getWindowHeight = Mock(return_value=5)
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import mouse
            mouse.x = 1024

        bge.render.setMousePosition.assert_called_once_with(1024, 3*5)

    def test_y_get(self):
        bge = Mock()

        bge.render.getWindowHeight =  Mock(return_value=2)
        bge.logic.mouse.position = [3, 5]
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import mouse
            self.assertEqual(mouse.y, 2*5)

    def test_y_set(self):
        bge = Mock()

        bge.logic.mouse.position = [2, 3]
        bge.render.getWindowWidth = Mock(return_value=5)
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import mouse
            mouse.y = 1024

        bge.render.setMousePosition.assert_called_once_with(2*5, 1024)

    def test_doc(self):
         with patch.dict('sys.modules', {'bge': Mock()}):
            from mbge import render
            print(dir(render))
            print(help(render))