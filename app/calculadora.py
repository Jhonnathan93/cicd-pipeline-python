# app/calculadora.py

AUTORES = "jsocampod@eafit.edu.co, asrodriguo@eafit.edu.co, jdgutierrg@eafit.edu.co, mgutierrej@eafit.edu.co"


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
