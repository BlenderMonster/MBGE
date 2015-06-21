from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock, MagicMock;
import sys

__author__ = 'Monster'


class TestSensors(TestCase):

    def test_parseAsList_None(self):
        from mutil import properties

        self.assertEqual(properties.parseAsList(None), None)

    def test_parseAsList_Empty(self):
        from mutil import properties

        self.assertEqual(properties.parseAsList(""), [])

    def test_parseAsList_single_integer(self):
        from mutil import properties

        self.assertEqual(properties.parseAsList("1"), [1])

    def test_parseAsList_two_integer(self):
        from mutil import properties

        self.assertEqual(properties.parseAsList("1, 2"), [1,2])

    def test_parseAsList_integer_and_float(self):
        from mutil import properties

        self.assertEqual(properties.parseAsList("1, 2.1"), [1, 2.1])

    def test_parseAsList_integer_and_string(self):
        from mutil import properties

        self.assertEqual(properties.parseAsList('1, "abc"'), [1, "abc"])
