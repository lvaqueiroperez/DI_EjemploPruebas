
def cadrados(lista):
    # PONDREMOS EN LA DOCUMENTACIÓN CÓDIDO, QUE SERÁ EL QUE PROBAREMOS CON LA FUNCIÓN "_PROBA"
    """Calcula el cuadrado de los numeros de una lista

    >>> l = [0,1,2,3,4]
    >>> cadrados(l)
    [0, 1, 4, 9, 16]
    """
    return [n ** 2 for n in lista]

def _proba():
    import doctest
    doctest.testmod()



if __name__ == "__main__":
    _proba()
    print(cadrados([0,1,2]))