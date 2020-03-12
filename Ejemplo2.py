# OJO CON LOS ESPACIOS !!!!
# PROBAMOS DE LA MISMA MANERA, EN EL TERMINAL EJECUTANDO EL FICHERO CON "python3 fichero.py"
import unittest


def cadrados(lista):
    # PONDREMOS EN LA DOCUMENTACIÓN CÓDIDO, QUE SERÁ EL QUE PROBAREMOS CON LA FUNCIÓN "CADRADOS" Y "_PROBA"
    # LO QUE ESTÁ ENTRE CORCHETES ES EL RESULTADO QUE ESPERAMOS [0,1,4,9,16]
    # LO QUE PONEMOS EN >>> ES LA PRUEBA !!! Y LO QUE HAY AL FINAL DEL CÓDIGO DE >>> ES EL RESULTADO ESPERADO !!!
    """Calcula el cuadrado de los numeros de una lista

    >>> l = [0,1,2,3,4]
    >>> cadrados(l)
    [0, 1, 4, 9, 16]
    """
    return [n ** 2 for n in lista]


# Creamos otra función
def cadrados2(n):
    """Calcula o cadrado do numero pasado como parametro (quitar lo de abajo para estos casos????)

    >>> l = [0,1,2,3,4]
    >>> for n in l:
    ... cadrad
    4

    :param n: numero
    :return: cadrado do numero n**2
    """

    return n ** 2


def suma(a, b):
    """Suma dos enteros a, b o concatena dos cadenas a, b

    """
    if isinstance(a, int) and isinstance(b, int):
        return (a + b)

    elif isinstance(a, str) and isinstance(b, str):
        return (int(a) + int(b))

    else:
        raise Exception("Argumentos no válidos")


class ProbaCadrados(unittest.TestCase):

    def setUp(self):
        print("preparando a proba")
        self.l = [0, 1, 2, 3, 4]

    def testCadrado(self):
        print("executando a proba")
        self.assertEqual(cadrados2(2), 4)

    def tearDown(self):
        print("destruindo o contexto")
        del self.l

    def testCadrados(self):
        l = [0, 1, 2, 3, 4]
        r = cadrados(l)
        self.assertEqual(r, [0, 1, 4, 9, 16])

    def testCadrados2(self):
        l = [0, 1, 2, 3, 4]
        r = list()
        for n in l:
            r.append(cadrados2(n))
        self.assertEqual(r, [0, 1, 4, 9, 16])

    def testSuma(self):
        self.assertEqual(suma(3, 5), 8)
        self.assertEqual(suma('3', '5'), 8)
        self.assertRaises(Exception, suma, 3.0, 5.0)


if __name__ == "__main__":
    #Si ponemos el unittest ejecutará los test !!!
    unittest.main()
    suma(2, 3)
    suma('23', '12')
    suma(2.03, 3.45)
