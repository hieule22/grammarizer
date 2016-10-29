# Copyright 2016 Hieu Le.

"""A symbol from a context-free grammar can be a variable, terminal or epsilon."""

from enum import Enum


class SymbolType(Enum):
    """Type associated with a symbol."""
    variable = 0
    terminal = 1
    epsilon = 2


class Symbol(object):
    """Representation of a symbol."""

    def __init__(self, symtype, name=None):
        """Constructs a symbol from given type and name.

        Args:
            symtype: type of symbol to construct.
            name: name of symbol to construct.
        """
        self._symtype = symtype
        self._name = name

    @property
    def type(self):
        """Returns read-only type of this symbol."""
        return self._symtype

    @property
    def name(self):
        """Returns read-only name of this symbol."""
        return self._name
