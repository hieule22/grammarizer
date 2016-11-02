# Copyright 2016 Hieu Le.

"""The first set of a string s over the language is the set of terminals
that begin a sentential form derivable from s using the production rule
of the grammar.
"""

from core.symbol import LAMBDA
from core.symbol import SymbolType


def generate_first_sets(productions):
    """Generates the first set for each symbol in the grammar.

    Args:
        productions: the production rules of a context-free grammar that
                     has been freed of any left recursion and left factored.

    Returns:
        The first sets for each variable and terminal in the grammar.
    """

    first_all = dict(LAMBDA={LAMBDA})
    # Initialize first sets.
    for production in productions:
        __initialize_first(first_all, production.head)
        for a in production.body:
            __initialize_first(first_all, a)
        if __is_lambda_production(production):
            first_all[production.head] = {LAMBDA}

    has_changes = True
    while has_changes:
        has_changes = False
        for production in productions:
            if not __is_lambda_production(production):
                x = production.head
                for a in production.body:
                    original_size = len(first_all[x])
                    first_all[x] |= first_all[a].difference({LAMBDA})
                    if len(first_all[x]) != original_size:
                        has_changes = True
                    if LAMBDA not in first_all[a]:
                        break

                first_intersection = set()
                for a in production.body:
                    first_intersection &= first_all[a]
                if LAMBDA in first_intersection and LAMBDA not in first_all[x]:
                    first_all[x] |= {LAMBDA}
                    has_changes = True

    return first_all


def __is_lambda_production(production):
    """Checks if a given production is a lambda production."""
    return len(production.body) == 1 and LAMBDA in production.body


def __initialize_first(first_all, x):
    """Initialize the first set of a non-lambda symbol from the grammar."""
    if x not in first_all:
        if x.type == SymbolType.TERMINAL:
            first_all[x] = {x}
        elif x.type == SymbolType.VARIABLE:
            first_all[x] = set()
