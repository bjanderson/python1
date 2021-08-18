from app import get_greeting


def test_get_greeting():
    greeting = get_greeting()
    assert greeting == "hello world"
