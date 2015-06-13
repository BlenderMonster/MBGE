from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock, PropertyMock, MagicMock;

import sys

__author__ = 'Monster'


class TestStorage(TestCase):

    def test_storedContent_get(self):
        bge = Mock()

        dictionary = {1:2}
        bge.logic.globalDict = dictionary
        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import storage
            self.assertEqual(storage.storedContent, dictionary)

    def test_storedContent_set(self):
        bge = Mock()

        dictionary = {1:2}

        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import storage
            storage.storedContent = dictionary
        self.assertEqual(bge.logic.globalDict, dictionary)

    def test_loadFromFile(self):
        bge = Mock()

        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import storage
            storage.loadFromFile()

        bge.logic.loadGlobalDict.assert_called_once_with()

    def test_saveToFile(self):
        bge = Mock()

        with patch.dict('sys.modules', {'bge': bge}):
            from mbge import storage
            storage.saveToFile()

        bge.logic.saveGlobalDict.assert_called_once_with()
