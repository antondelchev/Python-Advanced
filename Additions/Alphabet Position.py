def alphabet_position(text):
    alphabet = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]

    result = [str(alphabet.index(el) + 1) for el in text.lower() if el.isalpha()]
    return " ".join(result)
