"""Module with Base Command class."""

from abc import ABC, abstractmethod
import sys
from typing import Any, TextIO, List


class BaseCommand(ABC):
    """Base class for all commands."""

    def __init__(self, stdin: TextIO = sys.stdin, stdout: TextIO = sys.stdout):
        self.stdin = stdin
        self.stdout = stdout
        self.args: List[Any] = []

    def set_args(self, args: List[Any]):
        self.args = args

    @abstractmethod
    def __call__(self) -> int:
        """All commands should support callable interface."""
        pass
