class Corso:
    def __init__(self, codice, crediti, nome, pd):
        self.codice=codice
        self.crediti = crediti
        self.nome = nome
        self.pd = pd

    def __str__(self):
        return f"{self.nome} ({self.codice})"