from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock, MagicMock;
import sys

__author__ = 'Monster'


class TestSensors(TestCase):

    def test_allPositive_True_False(self):
        bge = Mock()

        sensorPositive = Mock()
        sensorPositive.positive = True
        sensorNegative = Mock()
        sensorNegative.positive = False
        bge.logic.getCurrentController().sensors = [sensorPositive, sensorNegative]
        with patch.dict('sys.modules', {'bge': bge}):
            from mutil import sensors
            self.assertEqual(sensors.allPositive, False)

    def test_allPositive_True_True(self):
        bge = Mock()

        sensorPositive = Mock()
        sensorPositive.positive = True
        bge.logic.getCurrentController().sensors = [sensorPositive, sensorPositive]
        with patch.dict('sys.modules', {'bge': bge}):
            from mutil import sensors
            self.assertEqual(sensors.allPositive, True)

    def test_onePositive_True_False(self):
        bge = Mock()

        sensorPositive = Mock()
        sensorPositive.positive = True
        sensorNegative = Mock()
        sensorNegative.positive = False
        bge.logic.getCurrentController().sensors = [sensorPositive, sensorNegative]
        with patch.dict('sys.modules', {'bge': bge}):
            from mutil import sensors
            self.assertEqual(sensors.onePositive, True)

    def test_onePositive_True_False(self):
        bge = Mock()

        sensorPositive = Mock()
        sensorPositive.positive = True
        sensorNegative = Mock()
        sensorNegative.positive = False
        bge.logic.getCurrentController().sensors = [sensorNegative, sensorNegative]
        with patch.dict('sys.modules', {'bge': bge}):
            from mutil import sensors
            self.assertEqual(sensors.onePositive, False)

    def test_hitObjects(self):
        bge = Mock()

        sensors = []
        raySensor = Mock(None, )
        raySensor.x = 1
        sensors.append(Mock(spec_set=["hitObject"]))
        sensors[0].hitObject = "A"
        sensors.append(Mock())
        sensors[1].hitObjectList = ["B"]
        sensors.append(Mock())
        sensors[2].hitObjectList = ["C", "D"]
        bge.logic.getCurrentController().sensors = sensors
        with patch.dict('sys.modules', {'bge': bge}):
            from mutil import sensors
            self.assertEqual(sensors.hitObjects, ["A", "B", "C", "D"])
