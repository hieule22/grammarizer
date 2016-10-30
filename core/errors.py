# Copyright 2016 Hieu Le.

"""The error and exception hierarchy for this library."""


class Error(Exception):
    """Base class for all the exceptions in this library.

    Attributes:
        message: explanation of the error.
    """

    def __init__(self, message):
        """Constructs an error from a specified message.

        Args:
            message: a string describing the error message.
        """
        Exception.__init__(self)
        self._message = message

    @property
    def message(self):
        """Gets the read-only message associated with this error.

        Returns:
            A string specifying this error's message.
        """
        return self._message


class GrammarError(Error):
    """Exception raised for errors in the grammar transformations."""

    def __init__(self, message):
        Error.__init__(self, message)
