import sys
from io import StringIO

from cli.presenter import Presenter


# Тесты для Presenter


def test_show_message_to_stdout():
    output = StringIO()
    presenter = Presenter(output_stream=output)

    # Выводим сообщение
    message = "Hello, World!"
    presenter.show(message)

    assert output.getvalue() == "Hello, World!\n"


def test_show_message_to_custom_stream():
    output = StringIO()
    presenter = Presenter(output_stream=output)

    message = "Test message"
    presenter.show(message)

    assert output.getvalue() == "Test message\n"


def test_show_message_with_default_stdout():
    output = StringIO()
    sys.stdout = output

    presenter = Presenter(sys.stdout)

    message = "Default stdout message"
    presenter.show(message)

    sys.stdout = sys.__stdout__

    assert output.getvalue() == "Default stdout message\n"
