from baza import to_latin,to_cyrillic
def convert(source: str, target: str) -> str:


    if target == 'latin':
        # latin = to_latin(source)

        return to_latin(source)

    if target == 'cyrrilic':
        # cyrrilic = to_cyrillic(source)

        return to_cyrillic(source)





if __name__ == '__main__':
    assert convert('FAYL', 'cyrrilic') == 'ФАЙЛ'
    assert convert('FAYL', 'latin') == 'FAYL'
    assert convert('ФАЙЛ', 'latin') == 'FAYL'