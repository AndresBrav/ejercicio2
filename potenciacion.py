    def calcularPotenciaV1(base, exponente):
        resultado = 1

        for i in range(exponente):
            resultado *= base

        return resultado

    def calcularPotenciaV2(base, exponente):
        return base ** exponente
