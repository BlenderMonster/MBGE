from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock

__author__ = 'Monster'


class TestStereo(TestCase):

    def test_focalLength_get(self):
        bge = Mock()

        bge.render.getFocalLength = Mock(return_value="focalLength")
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import stereo
            self.assertEqual(stereo.focalLength, "focalLength")

    def test_focalLength_set(self):
        bge = Mock()

        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import stereo
            stereo.focalLength = 123
        bge.render.setFocalLength.assert_called_once_with(123)

    def test_eyeSeparation_get(self):
        bge = Mock()

        bge.render.getEyeSeparation = Mock(return_value="eyeSeparation")
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import stereo
            self.assertEqual(stereo.eyeSeparation, "eyeSeparation")

    def test_eyeSeparation_set(self):
        bge = Mock()

        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import stereo
            stereo.eyeSeparation = "eyeSeparation"
        bge.render.setEyeSeparation.assert_called_once_with("eyeSeparation")

