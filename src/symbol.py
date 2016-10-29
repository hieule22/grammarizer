# Copyright 2016 Hieu Le.

"""A symbol from a context-free grammar can be a variable, terminal or epsilon."""

from enum import Enum


class SymbolType(Enum):
    """Type associated with a symbol."""
    variable = 0
    terminal = 1
    epsilon = 2  # Reserved for the empty string symbol.


class Symbol(object):
    """Representation of a symbol."""

    def __init__(self, symtype, name):
        """Constructs a symbol from given type and name.

        Args:
            symtype: type of symbol to construct.
            name: name of symbol to construct.
        """
        self._symtype = symtype
        self._name = name

    @property
    def type(self):
        """Gets the read-only type of this symbol.

        Returns:
            The type associated with this symbol.
        """
        return self._symtype

    @property
    def name(self):
        """Gets the read-only name of this symbol.

        Returns:
            The name associated with this symbol.
        """
        return self._name

# Constant symbol reserved for the empty string.
EPSILON = Symbol(SymbolType.epsilon, "EPSILON")
