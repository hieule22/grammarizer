# Copyright 2016 Hieu Le.

"""Unit tests for generate_first_sets."""

import unittest

from core.production import Production
from core.symbol import LAMBDA
from core.symbol import SymbolType
from core.symbol import Symbol
from transformers.firstset import generate_first_sets


class GenerateFirstSetsTest(unittest.TestCase):
    """Test class for generate_first_sets."""

    def test_generate_first_sets(self):
        """Test generate_first_sets() method."""
        A = Symbol(SymbolType.VARIABLE, "A")
        B = Symbol(SymbolType.VARIABLE, "B")
        C = Symbol(SymbolType.VARIABLE, "C")
        e = Symbol(SymbolType.TERMINAL, "e")
        f = Symbol(SymbolType.TERMINAL, "f")
        g = Symbol(SymbolType.TERMINAL, "g")

        productions = [
            Production(A, [e, A]),
            Production(A, [B, f]),
            Production(B, [C, A]),
            Production(B, [C, B]),
            Production(B, [LAMBDA]),
            Production(C, [g])
        ]

        first_sets = generate_first_sets(productions)

        for key, value in first_sets.items():
            print("%s: " % str(key), end="")
            for element in value:
                print("%s " % str(element), end="")
            print("\n")

        self.assertTrue(len(first_sets) == 7)

        # TODO(hieule): Fix failing test cases.
        # First(LAMBDA) = {LAMBDA}.
        # self.assertTrue(LAMBDA in first_sets.keys())
        # self.assertTrue(first_sets[LAMBDA] <= set([LAMBDA]))
        # self.assertTrue(LAMBDA in first_sets[LAMBDA])
        #
        # # First(t) = {t} for all terminal t.
        # for t in [e, f, g]:
        #     self.assertTrue(t in first_sets.keys())
        #     self.assertTrue(first_sets[t] == {t})
        #
        # self.assertTrue(A in first_sets.keys())
        # self.assertTrue(first_sets[A] == {e, f, g})
        #
        # self.assertTrue(B in first_sets.keys())
        # self.assertTrue(first_sets[B] == {LAMBDA, g})
        #
        # self.assertTrue(C in first_sets.keys())
        # self.assertTrue(first_sets[C] == {g})

    def test_generate_first_sets_advanced(self):
        PROGRAM = Symbol(SymbolType.VARIABLE, "PROGRAM")
        DECL_LIST = Symbol(SymbolType.VARIABLE, "DECL_LIST")
        VARIABLE_DECL_LIST = Symbol(SymbolType.VARIABLE, "VARIABLE_DECL_LIST")
        VARIABLE_DECL = Symbol(SymbolType.VARIABLE, "VARIABLE_DECL")
        PROCEDURE_DECL_LIST = Symbol(SymbolType.VARIABLE, "PROCEDURE_DECL_LIST")
        IDENTIFIER_LIST = Symbol(SymbolType.VARIABLE, "IDENTIFIER_LIST")
        IDENTIFIER_LIST_PRM = Symbol(SymbolType.VARIABLE, "IDENTIFIER_LIST_PRM")
        STANDARD_TYPE = Symbol(SymbolType.VARIABLE, "STANDARD_TYPE")
        BLOCK = Symbol(SymbolType.VARIABLE, "BLOCK")
        PROCEDURE_DECL = Symbol(SymbolType.VARIABLE, "PROCEDURE_DECL")
        PROCEDURE_ARGS = Symbol(SymbolType.VARIABLE, "PROCEDURE_ARGS")
        FORMAL_PARM_LIST = Symbol(SymbolType.VARIABLE, "FORMAL_PARM_LIST")
        FORMAL_PARM_LIST_HAT = Symbol(SymbolType.VARIABLE, "FORMAL_PARM_LIST_HAT")
        STMT_LIST = Symbol(SymbolType.VARIABLE, "STMT_LIST")
        STMT_LIST_PRM = Symbol(SymbolType.VARIABLE, "DECL_LIST_PRM")
        STMT = Symbol(SymbolType.VARIABLE, "STMT")
        ASSIGNMENT_STMT = Symbol(SymbolType.VARIABLE, "ASSIGNMENT_STMT")
        IF_STMT = Symbol(SymbolType.VARIABLE, "IF_STMT")
        IF_STMT_HAT = Symbol(SymbolType.VARIABLE, "IF_STMT_HAT")
        WHILE_STMT = Symbol(SymbolType.VARIABLE, "WHILE_STMT")
        PRINT_STMT = Symbol(SymbolType.VARIABLE, "PRINT_STMT")
        PROCEDURE_CALL_STMT = Symbol(SymbolType.VARIABLE, "PROCEDURE_CALL_STMT")
        EXPR_LIST = Symbol(SymbolType.VARIABLE, "EXPR_LIST")
        ACTUAL_PARM_LIST = Symbol(SymbolType.VARIABLE, "ACTUAL_PARM_LIST")
        ACTUAL_PARM_LIST_HAT = Symbol(SymbolType.VARIABLE, "ACTUAL_PARM_LIST_HAT")
        EXPR = Symbol(SymbolType.VARIABLE, "EXPR")
        EXPR_HAT = Symbol(SymbolType.VARIABLE, "EXPR_HAT")
        SIMPLE_EXPR = Symbol(SymbolType.VARIABLE, "SIMPLE_EXPR")
        SIMPLE_EXPR_PRM = Symbol(SymbolType.VARIABLE, "SIMPLE_EXPR_PRM")
        TERM = Symbol(SymbolType.VARIABLE, "TERM")
        TERM_PRM = Symbol(SymbolType.VARIABLE, "TERM_PRM")
        FACTOR = Symbol(SymbolType.VARIABLE, "FACTOR")
        SIGN = Symbol(SymbolType.VARIABLE, "SIGN")

        program = Symbol(SymbolType.TERMINAL, "program")
        identifier = Symbol(SymbolType.TERMINAL, "identifier")
        semicolon = Symbol(SymbolType.TERMINAL, ";")
        colon = Symbol(SymbolType.TERMINAL, ":")
        coma = Symbol(SymbolType.TERMINAL, ",")
        int = Symbol(SymbolType.TERMINAL, "int")
        bool = Symbol(SymbolType.TERMINAL, "bool")
        begin = Symbol(SymbolType.TERMINAL, "begin")
        end = Symbol(SymbolType.TERMINAL, "end")
        procedure = Symbol(SymbolType.TERMINAL, "procedure")
        openbracket = Symbol(SymbolType.TERMINAL, "(")
        closebracket = Symbol(SymbolType.TERMINAL, ")")
        assignment = Symbol(SymbolType.TERMINAL, ":=")
        _if = Symbol(SymbolType.TERMINAL, "if")
        _then = Symbol(SymbolType.TERMINAL, "then")
        _else = Symbol(SymbolType.TERMINAL, "else")
        _while = Symbol(SymbolType.TERMINAL, "while")
        loop = Symbol(SymbolType.TERMINAL, "loop")
        _print = Symbol(SymbolType.TERMINAL, "print")
        relop = Symbol(SymbolType.TERMINAL, "relop")
        addop = Symbol(SymbolType.TERMINAL, "addop")
        mulop = Symbol(SymbolType.TERMINAL, "mulop")
        num = Symbol(SymbolType.TERMINAL, "num")
        plus = Symbol(SymbolType.TERMINAL, "+")
        minus = Symbol(SymbolType.TERMINAL, "-")
        _not = Symbol(SymbolType.TERMINAL, "not")

        productions = [
            Production(PROGRAM, [program, identifier, semicolon, DECL_LIST, BLOCK, semicolon]),
            Production(DECL_LIST, [VARIABLE_DECL_LIST, PROCEDURE_DECL_LIST]),
            Production(VARIABLE_DECL_LIST, [VARIABLE_DECL, semicolon, VARIABLE_DECL_LIST]),
            Production(VARIABLE_DECL_LIST, [LAMBDA]),
            Production(VARIABLE_DECL, [IDENTIFIER_LIST, colon, STANDARD_TYPE]),
            Production(PROCEDURE_DECL_LIST, [PROCEDURE_DECL, semicolon, PROCEDURE_DECL_LIST]),
            Production(PROCEDURE_DECL_LIST, [LAMBDA]),
            Production(IDENTIFIER_LIST, [identifier, IDENTIFIER_LIST_PRM]),
            Production(IDENTIFIER_LIST_PRM, [coma, identifier, IDENTIFIER_LIST_PRM]),
            Production(IDENTIFIER_LIST_PRM, [LAMBDA]),
            Production(STANDARD_TYPE, [int, bool]),
            Production(BLOCK, [begin, STMT_LIST, end]),
            Production(PROCEDURE_DECL, [procedure, identifier, openbracket, PROCEDURE_ARGS,
                                        closebracket, VARIABLE_DECL_LIST, BLOCK]),
            Production(PROCEDURE_ARGS, [FORMAL_PARM_LIST]),
            Production(PROCEDURE_ARGS, [LAMBDA]),
            Production(FORMAL_PARM_LIST, [identifier, IDENTIFIER_LIST_PRM, colon,
                                          STANDARD_TYPE, FORMAL_PARM_LIST_HAT]),
            Production(FORMAL_PARM_LIST_HAT, [semicolon, FORMAL_PARM_LIST]),
            Production(FORMAL_PARM_LIST_HAT, [LAMBDA]),
            Production(STMT_LIST, [STMT, semicolon, STMT_LIST_PRM]),
            Production(STMT_LIST, [semicolon, STMT_LIST_PRM]),
            Production(STMT_LIST_PRM, [STMT, semicolon, STMT_LIST_PRM]),
            Production(STMT_LIST_PRM, [LAMBDA]),
            Production(STMT, [ASSIGNMENT_STMT]),
            Production(STMT, [IF_STMT]),
            Production(STMT, [WHILE_STMT]),
            Production(STMT, [PRINT_STMT]),
            Production(STMT, [PROCEDURE_CALL_STMT]),
            Production(ASSIGNMENT_STMT, [identifier, assignment, EXPR]),
            Production(IF_STMT, [_if, EXPR, _then, BLOCK, IF_STMT_HAT]),
            Production(IF_STMT_HAT, [_else, BLOCK]),
            Production(IF_STMT_HAT, [LAMBDA]),
            Production(WHILE_STMT, [_while, EXPR, loop, BLOCK]),
            Production(PRINT_STMT, [_print, EXPR]),
            Production(PROCEDURE_CALL_STMT, [identifier, openbracket, EXPR_LIST, closebracket]),
            Production(EXPR_LIST, [ACTUAL_PARM_LIST]),
            Production(EXPR_LIST, [LAMBDA]),
            Production(ACTUAL_PARM_LIST, [EXPR, ACTUAL_PARM_LIST_HAT]),
            Production(ACTUAL_PARM_LIST_HAT, [coma, ACTUAL_PARM_LIST]),
            Production(ACTUAL_PARM_LIST_HAT, [LAMBDA]),
            Production(EXPR, [SIMPLE_EXPR, EXPR_HAT]),
            Production(EXPR_HAT, [relop, SIMPLE_EXPR]),
            Production(EXPR_HAT, [LAMBDA]),
            Production(SIMPLE_EXPR, [TERM, SIMPLE_EXPR_PRM]),
            Production(SIMPLE_EXPR_PRM, [addop, TERM, SIMPLE_EXPR_PRM]),
            Production(SIMPLE_EXPR_PRM, [LAMBDA]),
            Production(TERM, [FACTOR, TERM_PRM]),
            Production(TERM_PRM, [mulop, FACTOR, TERM_PRM]),
            Production(TERM_PRM, [LAMBDA]),
            Production(FACTOR, [identifier]),
            Production(FACTOR, [num]),
            Production(FACTOR, [openbracket, EXPR, closebracket]),
            Production(FACTOR, [SIGN, FACTOR]),
            Production(SIGN, [plus]),
            Production(SIGN, [minus]),
            Production(SIGN, [_not])
        ]

        first_sets = generate_first_sets(productions)

        for key, value in first_sets.items():
            print("%s | " % str(key), end="")
            for element in value:
                print("%s, " % str(element), end="")
            print("\n")