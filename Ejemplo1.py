#OJO CON LOS ESPACIOS !!!!
import unittest
def cadrados(lista):
    # PONDREMOS EN LA DOCUMENTACIÓN CÓDIDO, QUE SERÁ EL QUE PROBAREMOS CON LA FUNCIÓN "CADRADOS" Y "_PROBA"
    #LO QUE ESTÁ ENTRE CORCHETES ES EL RESULTADO QUE ESPERAMOS [0,1,4,9,16]
    #LO QUE PONEMOS EN >>> ES LA PRUEBA !!! Y LO QUE HAY AL FINAL DEL CÓDIGO DE >>> ES EL RESULTADO ESPERADO !!!
    """Calcula el cuadrado de los numeros de una lista

    >>> l = [0,1,2,3,4]
    >>> cadrados(l)
    [0, 1, 4, 9, 16]
    """
    return [n ** 2 for n in lista]


#Creamos otra función
def cadrados2(n):

    """Calcula o cadrado do numero pasado como parametro

    >>> l = [0,1,2,3,4]
    >>> for n in l:
    ... cadrad
    4

    :param n: numero
    :return: cadrado do numero n**2
    """

    return n ** 2

class ProbaCadrados (unittest.TestCase):
    def testCadrados (self):
        l = [0,1,2,3,4]
        r = cadrados(l)
        self.assertEqual(r,[0,1,4,9,16])

    def testCadrados2(self):
        l = [0,1,2,3,4]
        r = list()
        for n in l:
            r.append(cadrados(n))
        self.assertEqual(r,[0,1,4,9,16])






def _proba():
    import doctest
    doctest.testmod()



if __name__ == "__main__":
    _proba()
    print(cadrados([0,1,2]))
    print(cadrados2(2))