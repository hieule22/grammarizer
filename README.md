# Grammarizer

## Background

The syntax of a programming language oftentimes is best represented in the form
of a [context-free grammar](https://en.wikipedia.org/wiki/Context-free_grammar).
Construction of a suitable grammar is essential for simplifying and expediting
the [syntactical analysis phase](https://en.wikipedia.org/wiki/Parsing) of a
modern compiler.

## Overview

This library provides several tools to transform a context-free grammar into an
equivalent form more conducive for predictive parsing, that is,
[recursive-descent parsing](https://en.wikipedia.org/wiki/Recursive_descent_parser)
which requires no backtracking.

## Transformations:

* Elimination of Left Recursion.

* Left Factoring.

* First Set Generation.