import sys
import typing


class Reader:
    """Reader logic."""

    @staticmethod
    def read(input_stream: typing.TextIO = sys.stdin) -> str:
        """Reads strings from the input stream."""
        line = input_stream.readline()
        return line
