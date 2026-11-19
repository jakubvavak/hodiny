class InvalidData(Exception):
    pass

class Osoba:
    def __init__(self, jmeno, telefon, email):
        self.jmeno = jmeno      # zavolá setter -> kontrola
        self.telefon = telefon  # zavolá setter -> kontrola
        self.email = email      # zatím bez kontroly

    @property
    def jmeno(self):
        return self._jmeno

    @jmeno.setter
    def jmeno(self, hodnota):
        # mezery povolíme kvůli "Jan Novak", jinak jen písmena
        if not hodnota.replace(" ", "").isalpha():
            raise InvalidData(f"Neplatné jméno: {hodnota}")
        self._jmeno = hodnota

    @property
    def telefon(self):
        return self._telefon

    @telefon.setter
    def telefon(self, hodnota):
        if not hodnota.isdigit():
            raise InvalidData(f"Neplatný telefon: {hodnota}")
        self._telefon = hodnota


if __name__ == "__main__":
    o = Osoba("Jan Novak", "004225877845", "jan@novak.cz")

    try:
        o.jmeno = "4357253"
    except InvalidData as e:
        print(e)

    try:
        o.telefon = "asjkdfhbasikfh"
    except InvalidData as e:
        print(e)