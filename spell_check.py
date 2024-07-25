def spell_check(text: str, character: str):
    counter = 0
    for characters in text:
        if characters == character:
            counter += 1
    return f"character: '{character}'\ncount: {counter}"


sample = ("""Quick brown fox jumps over the lazy dogQuick brown "
          fox jumps over the lazy dog""")


sym = "a"
print(spell_check(text=sample, character=sym))
