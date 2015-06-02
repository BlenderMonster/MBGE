from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock, PropertyMock, MagicMock;

import sys

__author__ = 'Monster'


class TestPhysics(TestCase):

    def test_maxFrames_get(self):
        bge = Mock()

        bge.logic.getMaxPhysicsFrame = Mock(return_value=5)
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import physics
            self.assertEqual(physics.maxFrames, 5)

    def test_maxFrame_set(self):
        bge = Mock()

        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import physics
            physics.maxFrames = 8

        bge.logic.setMaxPhysicsFrame.assert_called_once_with(8)

    def test_gravity_get_firstTime(self):
        bge = Mock()

        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import physics
            self.assertEqual(physics.gravity, None)

    def test_gravity_set(self):
        bge = Mock()

        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import physics
            physics.gravity = [1,2,3]

        bge.logic.setGravity.assert_called_once_with([1,2,3])

    def test_gravity_get_after_set(self):
        bge = Mock()

        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import physics
            physics.gravity = [1,2,3]
            self.assertEqual(physics.gravity, [1,2,3])
        bge.logic.setGravity.assert_called_once_with([1,2,3])
