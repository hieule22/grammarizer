# Copyright 2016 Hieu Le.

"""Unit tests for Production class."""

import unittest

from src.errors import GrammarError
from src.production import Production
from src.symbol import Symbol
from src.symbol import SymbolType


class ProductionTest(unittest.TestCase):
    """Test class for Production."""

    def test_accessors(self):
        """Test accessor methods of Production."""
        head = Symbol(SymbolType.variable, "EXPRESSION")
        body = [Symbol(SymbolType.variable, "EXPRESSION"),
                Symbol(SymbolType.terminal, "+"),
                Symbol(SymbolType.variable, "TERM")]

        prod = Production(head, body)
        self.assertEqual(prod.head, head)
        self.assertListEqual(prod.body, body)

    def test_error_construct(self):
        """Test exception raising from constructor."""
        head = Symbol(SymbolType.terminal, "-")
        with self.assertRaises(GrammarError) as context:
            Production(head, [])

        self.assertTrue("Production head must be a variable" in
                        context.exception.message)
