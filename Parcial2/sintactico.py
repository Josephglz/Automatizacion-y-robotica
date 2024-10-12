# Generar analizador sintáctico para comunicar lo que se espera del analizador léxico al arduino
from lexico import tokens

def p_programa(p):
    '''programa : PROGRAMA ID PUNTOCOMA declaraciones bloque FINPROGRAMA'''
    p[0] = p[4] + p[5]
