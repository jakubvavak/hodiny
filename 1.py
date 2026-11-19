class InvalidData(Exception):
    pass

class Osoba:
    def __init__(self, jmeno, telefon, email):
        self.jmeno = jmeno
        self.telefon = telefon
        self.email = email

if __name__ == "__main__":
    o = Osoba("Jan Novak", "004225877845", "jan@novak.cz")
    o.jmeno = "4357253" #kontrola, ze jmeno obsahuje pouze pismena
    o.telefon = "asjkdfhbasikfh" #kontrola, ze telefon obsahuje jenom cisla
    o.email = "xxx1"  #kontrola, ze email obsahuje pouze pismena, cisla, zavinac a tecky

    x= "aaa"
    if x.isalpha()
    if x.isnumeric()





    