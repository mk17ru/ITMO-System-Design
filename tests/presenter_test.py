import io
import sys
from io import StringIO

from cli.presenter import Presenter


#  Тесты для Presenter


def test_show_message_to_stdout():
    output = StringIO()
    presenter = Presenter(output_stream=output)

    # Выводим данные
    data = 'Hello, World!'
    presenter.show(io.StringIO(data))

    assert output.getvalue() == 'Hello, World!\n'


def test_show_message_to_custom_stream():
    output = StringIO()
    presenter = Presenter(output_stream=output)

    data = 'Test data'

    presenter.show(io.StringIO(data))

    assert output.getvalue() == 'Test data\n'


def test_show_message_with_default_stdout():
    output = StringIO()
    sys.stdout = output

    presenter = Presenter(sys.stdout)

    data = 'Default stdout data'
    presenter.show(io.StringIO(data))

    sys.stdout = sys.__stdout__

    assert output.getvalue() == 'Default stdout data\n'
