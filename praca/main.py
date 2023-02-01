from sredniaocen import Student
import student
studento = Student("Ania","Alowata",22,1)
studento.informations()
ocenowo = student.generator_ocen([],[])
ocenowo.generuj_losowe_oceny()
srednio = student.generator_ocen([],[])
srednio.srednie()

student.Matma.ddelta(float(input("a: ")),float(input("b: ")),float(input("c: ")))