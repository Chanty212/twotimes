from stringutils.utils import reverse_string, capitalize_words

def test_reverse_string():
    assert reverse_string("hello") == "olleh"

def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
