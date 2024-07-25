def differ(text1: str, text2: str):
    set_text1 = set(text1)
    set_text2 = set(text2)
    if text1 == text2:
        print(f"NO DIFFERENCE BETWEEN {text1} AND {text2}")
    elif len(text2) > len(text1):
        print(list(set_text2.difference(set_text1)))

    else:
        print(list(set_text1.difference(set_text2)))


differ(text1="abd", text2="abd")