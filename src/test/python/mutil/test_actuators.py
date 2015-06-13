from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock, MagicMock, call;
import sys

__author__ = 'Monster'


class TestActuators(TestCase):

    def test_activateAll(self):
        bge = Mock()

        controller = Mock()
        bge.logic.getCurrentController = Mock(return_value=controller)
        controller.actuators = ["a", "b", "c"]
        with patch.dict('sys.modules', {'bge': bge}):
            from mutil import actuators
            actuators.activateAll()

        controller.activate.assert_has_calls(
            [call("a"), call("c"), call("b")],
            any_order=True
        )

    def test_deactivateAll(self):
        bge = Mock()

        controller = Mock()
        bge.logic.getCurrentController = Mock(return_value=controller)
        controller.actuators = ["a", "b", "c"]
        with patch.dict('sys.modules', {'bge': bge}):
            from mutil import actuators
            actuators.deactivateAll()

        controller.deactivate.assert_has_calls(
            [call("a"), call("c"), call("b")],
            any_order=True
        )