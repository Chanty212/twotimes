def reverse_string(text: str) -> str:
    """Return the reversed version of the input string."""
    return text[::-1]


def capitalize_words(sentence: str) -> str:
    """Capitalize each word in a sentence."""
    return " ".join(word.capitalize() for word in sentence.split())
