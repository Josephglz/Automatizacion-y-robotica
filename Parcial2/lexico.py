import re
import LoadDictionary as ld

dicc = []

def deleteSpecialCharacters(cad):
    return re.sub(r'[áÁ]', 'a', re.sub(r'[éÉ]', 'e', re.sub(r'[íÍ]', 'i', re.sub(r'[óÓ]', 'o', re.sub(r'[úÚ]', 'u', cad)))))

def joinBigNumber(palabra):
    partes = palabra.split(' y ')
    total = 0
    for parte in partes:
        if parte in ld.num_dictionary:
            total += ld.num_dictionary[parte]
    return str(total)

def replaceStringNumbersToInt(cad):
    patron_numeros = r'\b(' + '|'.join(ld.num_dictionary.keys()) + r')(\s+y\s+(' + '|'.join(ld.num_dictionary.keys()) + r'))*\b'

    return re.sub(patron_numeros, lambda match: joinBigNumber(match.group(0)), cad)


def procesarCadena(cad):

    dicc = ld.loadDictionary()
    # Homologar a minusculas
    cad = cad.lower()
    # Remover símbolos de admiración e interrogación
    cad = re.sub(r'[!¡?¿,]', '', cad)
    # Remover acentos
    cad = deleteSpecialCharacters(cad)
    # Convertir texto a número
    cad = replaceStringNumbersToInt(cad)
    comando = cad.split(" ")
    
    # TODO: Convertir palabras a numeros y no eliminar los números INT - Terminado
    for i in range(len(comando)):
        if not comando[i].isdigit():
            if comando[i] not in dicc:
                comando[i] = ""

    for cmd in comando:
        if not cmd.isdigit():
            if cmd not in dicc:
                comando = [x for x in comando if x != cmd]

    print(comando)

    idx = -1
    for cmd in comando:
        if cmd.isdigit():
            idx = comando.index(cmd)
            break
    if idx == -1:
        comando = [comando[0]]
    else:
        comando = [comando[0], comando[idx]]

    print(comando)


if __name__ == "__main__":
    # c = "encender el coche y avanzar treinta y ocho y girar a la derecha nueve"
    # c = "derecha siete y detenerse"
    # c = "encender el coche y avanzar"
    c = "avanzar siete y girar a la derecha"
    procesarCadena(c)