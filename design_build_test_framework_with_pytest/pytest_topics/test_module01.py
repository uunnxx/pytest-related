from . import first_program


def test_first_program():
    assert first_program.hello() == 'Hello World!'
