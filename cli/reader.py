import string
import typing
import sys


class Reader:
    def read(self, input_stream: typing.TextIO = sys.stdin) -> str:
        """Reads strings from the input stream."""
        return input_stream.read()