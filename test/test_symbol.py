# Copyright 2016 Hieu Le.

"""Tests for Symbol class."""

import unittest

from src.symbol import EPSILON
from src.symbol import Symbol
from src.symbol import SymbolType


class SymbolTest(unittest.TestCase):
    """Test class for Symbol."""

    def test_type(self):
        """Tests type property of Symbol."""
        term = Symbol(SymbolType.terminal, "FOO")
        self.assertEqual(term.type, SymbolType.terminal)

        var = Symbol(SymbolType.variable, "FOO")
        self.assertEqual(var.type, SymbolType.variable)

        self.assertEqual(EPSILON.type, SymbolType.epsilon)

    def test_name(self):
        """Tests name property of Symbol."""
        identifier = Symbol(SymbolType.terminal, "IDENTIFIER")
        self.assertEqual(identifier.name, "IDENTIFIER")

        expression = Symbol(SymbolType.variable, "EXPRESSION")
        self.assertEqual(expression.name, "EXPRESSION")

        self.assertEqual(EPSILON.name, "EPSILON")

    def test_equality(self):
        """Tests equality checking."""
        first = Symbol(SymbolType.variable, "TERM")
        second = Symbol(SymbolType.variable, "TERM")
        third = Symbol(SymbolType.variable, "BLOCK")
        self.assertEqual(first, second)
        self.assertNotEqual(first, third)

    def test_hash(self):
        """Tests hash function."""
        first = Symbol(SymbolType.terminal, "BEGIN")
        second = Symbol(SymbolType.terminal, "BEGIN")
        third = Symbol(SymbolType.terminal, "NUMBER")

        self.assertTrue(first == second and hash(first) == hash(second))

        self.assertNotEqual(hash(first), hash(third))

        variables = {first: 0}
        self.assertTrue(second in variables)
        self.assertFalse(third in variables)

    def test_str(self):
        """Tests debug string method."""
        terminal = Symbol(SymbolType.terminal, "foo")
        self.assertEqual(str(terminal), "foo")

        variable = Symbol(SymbolType.variable, "bar")
        self.assertEqual(str(variable), "bar")

        self.assertEqual(str(EPSILON), "EPSILON")
