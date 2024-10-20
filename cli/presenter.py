"""Presenter component module."""

import sys
import typing


class Presenter:
    """Presenter logic."""

    def __init__(self, output_stream: typing.TextIO = sys.stdout) -> None:
        self.output_stream = output_stream

    def show(self, data: str) -> None:
        """Summary of show.

        Args:
            data (str): Data to present.

        Returns:
            None: Function doesn't return anything
        """
        self.output_stream.write(data + '\n')
        self.output_stream.flush()
