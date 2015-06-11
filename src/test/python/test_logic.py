from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock, PropertyMock, MagicMock;

import sys

__author__ = 'Monster'


class TestPhysics(TestCase):

    def test_maxLogicFrames_get(self):
        bge = Mock()

        bge.logic.getMaxLogicFrame = Mock(return_value=3)
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import logic
            self.assertEqual(logic.maxFrames, 3)

    def test_maxLogicFrames_set(self):
        bge = Mock()

        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import logic
            logic.maxFrames = 7

        bge.logic.setMaxLogicFrame.assert_called_once_with(7)

    def test_doc(self):
         with patch.dict('sys.modules', {'bge': Mock()}):
            from mbge import logic
            print(dir(logic))
            print(help(logic))

