
import datetime
from random import randint
class basicdata:
    def __init__(self,imie : str,nazwisko : str,wiek : int,rok : int) -> None:
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.wiek = wiek
        self.rok = rok

    def informations(self):
        print(f"""
        imie        {self.__imie}
        nazwisko    {self.__nazwisko}
        wiek        {self.wiek}
        rok         {self.rok}
        """)

class generator_ocen:
    def __init__(self,oceny_z_matemtyki : list,oceny_z_fizyki : list) -> None:
        self.oceny_z_matemtyki = oceny_z_matemtyki
        self.oceny_z_fizyki = oceny_z_fizyki

    def generuj_losowe_oceny(self):
        for i in range(5):
            self.oceny_z_matemtyki.append(randint(1,6))
            self.oceny_z_fizyki.append(randint(1,6))
        print(f"""
        matematyka:    {self.oceny_z_matemtyki}
        fizyka:    {self.oceny_z_fizyki}
        """)
    
    def srednie(self):
        for i in range(5):
            self.oceny_z_matemtyki.append(randint(1,6))
            self.oceny_z_fizyki.append(randint(1,6))
        print(f"""
        srednia_z_matematyki    {sum(self.oceny_z_matemtyki)/len(self.oceny_z_matemtyki)}
        srednia_z_fizyki        {sum(self.oceny_z_fizyki)/len(self.oceny_z_fizyki)}
        """)


class Matma:
    @staticmethod
    def ddelta(a,b,c):
        delta = b**2-4*a*c
        if delta > 0 :
            print("równanie kwadratowe ma 2 rozwiązania")
        if delta == 0:
            print("równanie kwadratowe ma 1 rozwiązanie")
        if delta < 0:
            print("równanie kwadratowe nie ma rozwiązania")