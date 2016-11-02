# Copyright 2016 Hieu Le.

"""Tests for Symbol class."""

import unittest

from core.symbol import LAMBDA
from core.symbol import Symbol
from core.symbol import SymbolType


class SymbolTest(unittest.TestCase):
    """Test class for Symbol."""

    def test_type(self):
        """Tests type property of Symbol."""
        term = Symbol(SymbolType.TERMINAL, "FOO")
        self.assertEqual(term.type, SymbolType.TERMINAL)

        var = Symbol(SymbolType.VARIABLE, "FOO")
        self.assertEqual(var.type, SymbolType.VARIABLE)

        self.assertEqual(LAMBDA.type, SymbolType.EPSILON)

    def test_name(self):
        """Tests name property of Symbol."""
        identifier = Symbol(SymbolType.TERMINAL, "IDENTIFIER")
        self.assertEqual(identifier.name, "IDENTIFIER")

        expression = Symbol(SymbolType.VARIABLE, "EXPRESSION")
        self.assertEqual(expression.name, "EXPRESSION")

        self.assertEqual(LAMBDA.name, "LAMBDA")

    def test_equality(self):
        """Tests equality checking."""
        first = Symbol(SymbolType.VARIABLE, "TERM")
        second = Symbol(SymbolType.VARIABLE, "TERM")
        third = Symbol(SymbolType.VARIABLE, "BLOCK")
        self.assertEqual(first, second)
        self.assertNotEqual(first, third)

    def test_hash(self):
        """Tests hash function."""
        first = Symbol(SymbolType.TERMINAL, "BEGIN")
        second = Symbol(SymbolType.TERMINAL, "BEGIN")
        third = Symbol(SymbolType.TERMINAL, "NUMBER")

        self.assertTrue(first == second and hash(first) == hash(second))

        self.assertNotEqual(hash(first), hash(third))

        variables = {first: 0}
        self.assertTrue(second in variables)
        self.assertFalse(third in variables)

    def test_str(self):
        """Tests debug string method."""
        terminal = Symbol(SymbolType.TERMINAL, "foo")
        self.assertEqual(str(terminal), "foo")

        variable = Symbol(SymbolType.VARIABLE, "bar")
        self.assertEqual(str(variable), "bar")

        self.assertEqual(str(LAMBDA), "LAMBDA")
