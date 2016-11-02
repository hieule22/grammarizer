# Copyright 2016 Hieu Le.

"""Unit tests for Production class."""

import unittest

from core.errors import GrammarError
from core.production import Production
from core.symbol import Symbol
from core.symbol import SymbolType


class ProductionTest(unittest.TestCase):
    """Test class for Production."""

    def test_accessors(self):
        """Test accessor methods of Production."""
        head = Symbol(SymbolType.VARIABLE, "EXPRESSION")
        body = [Symbol(SymbolType.VARIABLE, "EXPRESSION"),
                Symbol(SymbolType.TERMINAL, "+"),
                Symbol(SymbolType.VARIABLE, "TERM")]

        prod = Production(head, body)
        self.assertEqual(prod.head, head)
        self.assertListEqual(prod.body, body)

    def test_error_construct(self):
        """Test exception raising from constructor."""
        head = Symbol(SymbolType.TERMINAL, "-")
        with self.assertRaises(GrammarError) as context:
            Production(head, [])

        self.assertTrue("Production head must be a variable" in
                        context.exception.message)

    def test_str(self):
        """Tests debug string method."""
        head = Symbol(SymbolType.VARIABLE, "FOO")
        body = [Symbol(SymbolType.TERMINAL, "bar"),
                Symbol(SymbolType.TERMINAL, "+"),
                Symbol(SymbolType.TERMINAL, "quoz")]
        production = Production(head, body)

        self.assertEqual(str(production), "FOO ::= bar + quoz")
