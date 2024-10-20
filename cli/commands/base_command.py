"""Module with Base Command class."""

import enum
import sys
import typing
from abc import ABC, abstractmethod
from typing import Any


class Commands(enum.StrEnum):
    """Commands logic."""

    CAT = 'cat'
    ECHO = 'echo'
    EXIT = 'exit'
    PWD = 'pwd'
    WC = 'wc'
    WHICH = 'which'


class BaseCommand(ABC):
    """Base class for all commands."""

    def __init__(self, stdin: typing.TextIO = sys.stdin, stdout: typing.TextIO = sys.stdout):
        self.stdin = stdin
        self.stdout = stdout
        self.args: list[Any] = []

    @property
    def stdin(self) -> typing.TextIO:
        """Summary of stdin.

        Returns:
            TextIO: Description of return value
        """
        return self._stdin

    @stdin.setter
    def stdin(self, stdin: typing.TextIO) -> None:
        """Summary of stdin.

        Args:
            stdin (TextIO): Description of stdin.
        """
        self._stdin = stdin

    @property
    def stdout(self) -> typing.TextIO:
        """Summary of stdout.

        Returns:
            TextIO: Description of return value
        """
        return self._stdout

    @stdout.setter
    def stdout(self, stdout: typing.TextIO) -> None:
        """Summary of stdout.

        Args:
            stdout (TextIO): Description of stdout.
        """
        self._stdout = stdout

    def set_args(self, args: list[Any]) -> None:
        """Summary of set_args.

        Args:
            args (List[Any]): Description of args.
        """
        self.args = args

    @abstractmethod
    def __call__(self) -> int:
        """All commands should support callable interface."""
        pass
