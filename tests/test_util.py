from unittest import TestCase
from mock import patch, Mock, MagicMock
import json
from transifex.exceptions import InvalidSlugException, TransifexAPIException
from transifex.util import *

class TransifexUtilTest(TestCase):

    def test_translation_hash(self):
        """
        Test the `translation_hash` utility funciton
        """
        # A context which is blank, None, and Empty list should all be the same
        entity = "Jar Jar binks is my co-pilot"
        control = translation_hash(entity)
        self.assertEqual(control, translation_hash(entity, None))
        self.assertEqual(control, translation_hash(entity, ""))
        self.assertEqual(control, translation_hash(entity, []))

        # Providing a context should make it different
        self.assertNotEqual(control, translation_hash(entity, "Anakin Skywalker"))
        self.assertNotEqual(control, translation_hash(entity, ["Anakin Skywalker"]))
