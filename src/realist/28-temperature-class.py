class Temperature:
    def __init__(self):
        self.__kelvin = 273.15

    @property
    def kelvin(self):
        return self.__kelvin

    @property
    def celsius(self):
        return self.__kelvin - 273.15

    @property
    def fahrenheit(self):
        return (self.__kelvin - 273.15) * 9 / 5 + 32

    @kelvin.setter
    def kelvin(self,value):
        self.__kelvin = value

    @celsius.setter
    def celsius(self,value):
        self.__kelvin = value + 273.15

    @fahrenheit.setter
    def fahrenheit(self,value):
        self.__kelvin = (value - 32) * 5 / 9 + 273.15

    def __repr__(self):
        return f'Temperature(__kelvin={self.__kelvin})'

    def __str__(self):
        return f'{self.kelvin:.2f}\N{DEGREE SIGN}K/{self.celsius:.2f}\N{DEGREE SIGN}C/{self.fahrenheit:.2f}\N{DEGREE SIGN}F'