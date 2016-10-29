# Copyright 2016 Hieu Le.

"""The productions of a grammar specify the manner in which the terminals
and non-terminals can be combined to form strings.
"""

from src.errors import GrammarError
from src.symbol import SymbolType


class Production(object):
    """Representation of a single production.

    Attributes:
        head: a variable on the right hand side of the production.
        body: a combination of zero or more terminals and variables on the
              right hand side of the production. The components of the body
              describes one way in which strings of the variable at the head
              can be constructed.

    Example:
        EXPRESSION ::= EXPRESSION + TERM | EXPRESSION - TERM | TERM
        TERM ::= TERM * FACTOR | TERM * FACTOR | TERM / FACTOR
    """

    def __init__(self, head, body):
        """Constructs a production from a given head and body.

        Args:
            head: a variable specifying the head of the production.
            body: a list of variables and terminals specifying the body of
                  the production.

        Raises:
            GrammarError: if head is not a variable.
        """
        if head.type != SymbolType.variable:
            raise GrammarError('Production head must be a variable: %s'
                               % head.name)
        self._head = head
        self._body = body

    @property
    def head(self):
        """Gets the read-only head of this production.

        Returns:
            A variable specifying the production head.
        """
        return self._head

    @property
    def body(self):
        """Gets the read-only body of this production.

        Returns:
            A list of variables and terminals specifying the production body.
        """
        return self._body
