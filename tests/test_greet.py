from hello_world.greet import greet


def test_greet():
    expected = 'Hello there peter!'
    assert greet('peter') == expected