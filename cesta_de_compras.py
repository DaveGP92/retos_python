# Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.

# valor_producto = int(input("Agregue el valor del producto:\n"))

# descuento = int(input("¿Cuánto descuento quiere aplicar al producto: 10, 20 o 25%?:\n"))

cesta_de_compras = {
    "manzanas": {"precio": 2000, "porcentaje": 10},
    "pan": {"precio": 5000, "porcentaje": 5},
    "leche": {"precio": 4500, "porcentaje": 3},
    "huevos": {"precio": 16000, "porcentaje": 7},
    "queso": {"precio": 8000, "porcentaje": 12},
    "pollo": {"precio": 15000, "porcentaje": 20},
    "arroz": {"precio": 2500, "porcentaje": 4},
    "frijoles": {"precio": 6500, "porcentaje": 5},
    "café": {"precio": 14500, "porcentaje": 15},
    "azúcar": {"precio": 3500, "porcentaje": 2},
    "aceite": {"precio": 3000, "porcentaje": 9},
    "sal": {"precio": 1500, "porcentaje": 1},
    "pasta": {"precio": 1800, "porcentaje": 4},
    "tomates": {"precio": 2200, "porcentaje": 3}
}



def descuento(valor_producto, descuento):

    valor_descuento =  valor_producto * (descuento / 100)

    valor_con_descuento = valor_producto - valor_descuento

    return f"El precio del producto es de {valor_producto}.\nSu descuento fue de {descuento}%.\nSe descontaron {valor_descuento}.\nEl producto le cuesta {valor_con_descuento}"


def iva(valor_producto):

    iva = valor_producto * 0.19

    return f"Su producto cuesta {valor_producto + iva} con IVA incluído."


def aplicar_descuento_o_iva(cesta_de_compras, func):

    descuento_producto = func(cesta_de_compras["precio"], cesta_de_compras["porcentaje"])

    return descuento_producto


total = aplicar_descuento_o_iva(cesta_de_compras["manzanas"], descuento)
print(total)



    