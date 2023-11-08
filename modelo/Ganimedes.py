from  modelo.regalvalidacion import ReglaValidacion

class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self, longitud_esperada):
        super().__init__(longitud_esperada)

    def contiene_caracter_especial(self, clave):
        caracteres_especiales = ['@', '_', '#', '$', '%']
        return any(caracter in clave for caracter in caracteres_especiales)

    def es_valida(self, clave):
        longitud_valida = self._validar_longitud(clave)
        mayuscula_valida = self._contiene_mayuscula(clave)
        minuscula_valida = self._contiene_minuscula(clave)
        numero_valida = self._contiene_numero(clave)
        caracter_especial_valido = self.contiene_caracter_especial(clave)

        return longitud_valida and mayuscula_valida and minuscula_valida and numero_valida and caracter_especial_valido