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

    def test_detectHit_allParameters(self):
        bge = Mock()

        sourcePosition = "sp"
        targetPosition = "tp"
        distance = "dist"
        filterProperty = "fp"
        normalDirection = "nd"
        excludeUnfiltered = False
        hitObject = "ho"
        hitPosition = "hp"
        hitNormal = "hn"

        mock = MagicMock(
            return_value=[hitObject, hitPosition, hitNormal])
        bge.logic.getCurrentScene().active_camera.rayCast = mock

        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import physics
            hit = physics.detectHit(sourcePosition, targetPosition, distance,
                                    property=filterProperty,
                                    normalDirection=normalDirection,
                                    xray=excludeUnfiltered)
            self.assertEqual(hit.object, hitObject)
            self.assertEqual(hit.position, hitPosition)
            self.assertEqual(hit.normal, hitNormal)

        bge.logic.getCurrentScene().active_camera.rayCast.assert_called_once_with(
                sourcePosition, targetPosition, distance,
                filterProperty, normalDirection, excludeUnfiltered, 0)

    def test_detectHit_only_mandatoryParameters(self):
        bge = Mock()

        sourcePosition = "sp"
        targetPosition = "tp"
        hitObject = "ho"
        hitPosition = "hp"
        hitNormal = "hn"

        mock = MagicMock(
            return_value=[hitObject, hitPosition, hitNormal])
        bge.logic.getCurrentScene().active_camera.rayCast = mock

        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import physics
            hit = physics.detectHit(sourcePosition, targetPosition)
            self.assertEqual(hit.object, hitObject)
            self.assertEqual(hit.position, hitPosition)
            self.assertEqual(hit.normal, hitNormal)

            bge.logic.getCurrentScene().active_camera.rayCast.assert_called_once_with(
                    sourcePosition, targetPosition, 0,
                    "", 0, 0, 0)

    def test_detectFaceHit_allParameters(self):
        bge = Mock()

        sourcePosition = "sp"
        targetPosition = "tp"
        distance = "dist"
        filterProperty = "fp"
        normalDirection = "nd"
        excludeUnfiltered = True
        hitObject = "ho"
        hitPosition = "hp"
        hitNormal = "hn"
        hitFace = "fa"

        mock = MagicMock(
            return_value=[hitObject, hitPosition, hitNormal, hitFace])
        bge.logic.getCurrentScene().active_camera.rayCast = mock

        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import physics
            hit = physics.detectFaceHit(sourcePosition, targetPosition, distance,
                                    property=filterProperty,
                                    normalDirection=normalDirection,
                                    xray=excludeUnfiltered)
            self.assertEqual(hit.object, hitObject)
            self.assertEqual(hit.position, hitPosition)
            self.assertEqual(hit.normal, hitNormal)
            self.assertEqual(hit.face, hitFace)

        bge.logic.getCurrentScene().active_camera.rayCast.assert_called_once_with(
                sourcePosition, targetPosition, distance,
                filterProperty, normalDirection, 1, 1)

    def test_detectUvFaceHit_allParameters(self):
        bge = Mock()

        sourcePosition = "sp"
        targetPosition = "tp"
        distance = "dist"
        filterProperty = "fp"
        normalDirection = "nd"
        excludeUnfiltered = True
        hitObject = "ho"
        hitPosition = "hp"
        hitNormal = "hn"
        hitFace = "fa"
        hitUv = "hu"

        mock = MagicMock(
            return_value=[hitObject, hitPosition, hitNormal, hitFace, hitUv])
        bge.logic.getCurrentScene().active_camera.rayCast = mock

        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import physics
            hit = physics.detectUvFaceHit(sourcePosition, targetPosition, distance,
                                    property=filterProperty,
                                    normalDirection=normalDirection,
                                    xray=excludeUnfiltered)
            self.assertEqual(hit.object, hitObject)
            self.assertEqual(hit.position, hitPosition)
            self.assertEqual(hit.normal, hitNormal)
            self.assertEqual(hit.face, hitFace)
            self.assertEqual(hit.uv, hitUv)

        bge.logic.getCurrentScene().active_camera.rayCast.assert_called_once_with(
                sourcePosition, targetPosition, distance,
                filterProperty, normalDirection, 1, 2)


    def test_doc(self):
         with patch.dict('sys.modules', {'bge': Mock()}):
            from mbge import physics
            print(dir(physics))
            print(help(physics))