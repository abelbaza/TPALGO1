# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 01:32:36 2024
TP ALGO 01 : CLASSE FRACTION (Ass. MOBISA)
@author: Abel BAZAYAMA L2GC
"""
class Fraction:
    def __init__(self, num, den):
        assert isinstance(num, int) and isinstance(den, int) and den > 0, "le dénominateur être un entier strictement positif"
        self.num = num
        self.den = den
        
    def __str__(self):
        if self.den == 1:
            return str(self.num)
        else:
            return f"{self.num}/{self.den}"
    
    def eq(self, other):
        return self.num*other.den == other.num*self.den
#=========================================================

#batterie des tests
if __name__ == '__main__':
    
    # Création des instances F1, F2, F3 et F4
    
    F1 = Fraction(3, 4)
    F2 = Fraction(-8, 1)
    F3 = Fraction(2, 3)
    F4 = Fraction(21, 28)
    
    # Affichage des instances à l'aide de la méthode spéciale str
    
    print(F1)
    print(F2)
    print(F3)
    print(F4)
    
    # Tests de l'égalité entre les fractions
    
    print(F1.eq(F3)) # Doit afficher False
    print(F2.eq(F4)) # Doit afficher False
    print(F1.eq(F1)) # Doit afficher True
    
# BAZAYAMA MBOTI ABEL L2GC POLYTECH UNIKIN 2023-2024