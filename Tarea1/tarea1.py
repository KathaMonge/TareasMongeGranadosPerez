"""
Tarea 1 – MT7003
Implementacion de funciones evaluadas con pytest
"""

# Codigo de exito
SUCCESS = 0

# Errores operation_selector
ERROR_INVALID_OPERANDS = -50
ERROR_OP_NOT_STRING = -60
ERROR_INVALID_OP = -70

# Errores calculo_promedio
ERROR_NON_NUMERIC = -80
ERROR_LIST_TOO_LONG = -90


# Inicio de la primera funcion estilo calculadora basica

def operation_selector(num1, num2, op):
    """
    Selecciona y ejecuta una operacion matematica o logica entre dos enteros.

    Parametros:
        num1 (int): Primer operando
        num2 (int): Segundo operando
        op (str): Operador (+, -, *, &)

    Retorna:
        (codigo, resultado)
    """
# Verificar que num1 y num2 sean enteros (bool NO cuenta)
    if not isinstance(num1, int) or not isinstance(num2, int):
        return ERROR_INVALID_OPERANDS, None
    if isinstance(num1, bool) or isinstance(num2, bool):
        return ERROR_INVALID_OPERANDS, None

    # Verificar que op sea string
    if not isinstance(op, str):
        return ERROR_OP_NOT_STRING, None

    # Verificar operador valido
    if op not in ["+", "-", "*", "&"]:
        return ERROR_INVALID_OP, None

    # Ejecutar operacion
    if op == "+":
        return SUCCESS, num1 + num2
    if op == "-":
        return SUCCESS, num1 - num2
    if op == "*":
        return SUCCESS, num1 * num2
    if op == "&":
        return SUCCESS, num1 & num2
