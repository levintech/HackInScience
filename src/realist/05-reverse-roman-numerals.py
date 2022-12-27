roman_numerals_dict = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}

def from_roman_numeral(roman_numeral):
    number = 0
    
    while roman_numeral:
        # try first two chars
        if roman_numeral[:2] in roman_numerals_dict.keys():
            number += roman_numerals_dict[roman_numeral[:2]]
            roman_numeral = roman_numeral[2:]

        # try first char
        if roman_numeral[:1] in roman_numerals_dict.keys():
            number += roman_numerals_dict[roman_numeral[:1]]
            roman_numeral = roman_numeral[1:]

    return number