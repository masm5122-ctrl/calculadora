

def somar(num1, num2):
    resultado = num1 + num2
    return resultado


def subtrair(num1, num2):
    resultado = num1 - num2
    return resultado


def multiplicar(num1, num2):
    resultado = num1 * num2
    return resultado


def dividir(num1, num2):
    if num2 == 0:
        return "Erro divisao"
    return num1/num2

def porcentagem(num1, porcent):
    return num1 * (porcent/100)

