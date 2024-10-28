"""Presenter component module."""

import io
import sys
import typing

from cli.reader import Reader


class Presenter:
    """Presenter logic."""

    def __init__(self, output_stream: typing.TextIO = sys.stdout) -> None:
        self.output_stream = output_stream
        self.reader = Reader()

    def show(self, stream: io.StringIO) -> None:
        """Summary of show.

        Args:
            stream (str): Data to present.

        Returns:
            None: Function doesn't return anything
        """
        data = self.reader.read(stream)
        self.output_stream.write(data + '\n')
        self.output_stream.flush()
