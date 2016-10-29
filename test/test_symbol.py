# Copyright 2016 Hieu Le.

"""Tests for Symbol class."""

import unittest

from src.symbol import Symbol
from src.symbol import SymbolType


class TestSymbol(unittest.TestCase):
    """Test class for Symbol"""

    def test_type(self):
        """Tests type property of Symbol."""
        term = Symbol(SymbolType.terminal, "FOO")
        self.assertEqual(term.type, SymbolType.terminal)

        var = Symbol(SymbolType.variable, "FOO")
        self.assertEqual(var.type, SymbolType.variable)

        eps = Symbol(SymbolType.epsilon)
        self.assertEqual(eps.type, SymbolType.epsilon)

    def test_name(self):
        """Tests name property of Symbol."""
        identifier = Symbol(SymbolType.terminal, "IDENTIFIER")
        self.assertEqual(identifier.name, "IDENTIFIER")

        expression = Symbol(SymbolType.variable, "EXPRESSION")
        self.assertEqual(expression.name, "EXPRESSION")

        epsilon = Symbol(SymbolType.epsilon)
        self.assertEqual(epsilon.name, None)
