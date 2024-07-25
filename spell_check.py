def spell_check(text: str, character: str):
    counter = 0
    for characters in text:
        if characters == character:
            counter += 1
    return f"character: '{character}'\ncount: {counter}"


print(spell_check(text="Quick brown fox jumps over the lazy dogQuick brown fox jumps over the lazy dog", character="a"))

