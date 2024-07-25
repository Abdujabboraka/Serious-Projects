def check_bracks(text: str):
    toplam = []
    qavslar = {"(": ")", "{": "}", "[": "]"}

    for i in text:
        #qavs ochilishini tekshirish
        if i in qavslar:
            toplam.append(i)
        #qavs yopilishini tekshirish
        elif i in qavslar.values():
            if toplam == [] or qavslar[toplam.pop()] != i:
                return False
    return toplam == []


print(check_bracks(text="({})"))
