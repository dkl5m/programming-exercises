from datetime import date


class Patient:

    def __init__(self, name, age, ppr, email):
        self.name = name
        self.age = age
        self.ppr = ppr
        self.email = email

    @classmethod
    def ageYearBorn(cls, name, yearBorn, ppr, email):
        age = date.today().year - yearBorn
        return cls(name, age, ppr, email)


class Medician:
    pass


"""
patient = Patient('Mona', 20, "000.000.000-00", "mona@gmail.com")
print(patient.__dict__)
print(Patient.ageYearBorn(2003))
"""

patient = Patient.ageYearBorn('Mona', 2003, "000.000.000-00", "mona@gmail.com")
print(patient.__dict__)
print(patient.age)
