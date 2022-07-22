def verifica(strs:str):
    simples = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    composto = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

    roman_number = strs
    total = 0

    for k, v in composto.items():
        if k in roman_number:
            total += v
            roman_number = roman_number.replace(str(k), "")

    for v in roman_number:
        if v in simples:
            total += simples[v]

    return total


# TESTES


print(verifica("III"))
print(verifica("LVIII"))
print(verifica("MCMXCIV"))