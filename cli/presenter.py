"""Presenter component module."""

import typing
import sys


class Presenter:
    """Presenter logic."""

    def __init__(self, output_stream: typing.TextIO = sys.stdout) -> None:
        self.output_stream = output_stream

    def show(self, data: str) -> None:
        """Summary of show.

        Args:
            data (str): Description of data.

        Returns:
            None: Description of return value
        """
        self.output_stream.write(data + '\n')
        self.output_stream.flush()
