"""Module with Base Command class."""

from abc import ABC, abstractmethod
import sys
from typing import Any, TextIO


class BaseCommand(ABC):
    """Base class for all commands."""

    def __init__(self, stdin: TextIO = sys.stdin, stdout: TextIO = sys.stdout):
        self.stdin = stdin
        self.stdout = stdout

    @abstractmethod
    def __call__(self, *args: Any) -> int:
        """All commands should support callable interface."""
        pass
