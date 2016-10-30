# Copyright 2016 Hieu Le.

"""Unit tests for error hierarchy."""

import unittest

from core.errors import Error
from core.errors import GrammarError


class ErrorsTest(unittest.TestCase):
    """Test class for Error."""

    def test_message(self):
        """Test message property of Error."""
        error = Error("Foo")
        self.assertEqual(error.message, "Foo")

        grammar_error = GrammarError("Bar")
        self.assertEqual(grammar_error.message, "Bar")
