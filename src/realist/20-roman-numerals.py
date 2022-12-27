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

def to_roman_numeral(number):
    roman_text = ''
    
    while number > 0:
        for key, value in roman_numerals_dict.items():
            if number >= value:
                roman_text = roman_text + key
                number = number - value
                break
    
    return roman_text