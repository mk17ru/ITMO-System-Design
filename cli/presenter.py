"""Модуль с реализацией компонента Presenter."""

import typing
import sys


class Presenter:
    """Класс Presenter."""

    def __init__(self, output_stream: typing.TextIO = sys.stdout) -> None:
        """Инициализация."""
        self.output_stream = output_stream

    def show(self, data: str) -> None:
        """:param data: str:"""
        self.output_stream.write(data + '\n')
        self.output_stream.flush()
