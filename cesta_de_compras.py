# Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.


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


aplicar_descuento = lambda producto: cesta_de_compras[producto]["precio"] * cesta_de_compras[producto]["porcentaje"] / 100

aplicar_iva = lambda producto: cesta_de_compras[producto]["precio"] * 0.19


def funcion_superior(cesta_de_compras, func):

    if func == aplicar_iva:
        for item in cesta_de_compras:
            resultado_iva = func(item)
            print(f"El IVA de {item} es ${resultado_iva}")

    elif func == aplicar_descuento:
        for item in cesta_de_compras:
            resultado_desc = func(item)
            print(f"El descuento de {item} es ${resultado_desc}")

    
funcion_superior(cesta_de_compras, aplicar_iva)

print()

funcion_superior(cesta_de_compras, aplicar_descuento)



