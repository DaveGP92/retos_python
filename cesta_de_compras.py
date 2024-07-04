# Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.

valor_producto = int(input("Agregue el valor del producto:\n"))
descuento = int(input("¿Cuánto descuento quiere aplicar al producto: 10, 20 o 25%?:\n"))

def aplicar_descuento(valor_producto, descuento):

    descuento =  valor_producto * (descuento / 100)

    valor_con_descuento = valor_producto - descuento

    return f"Su descuento fue de {descuento}. El producto le cuesta {valor_con_descuento}"

resul = aplicar_descuento(valor_producto, descuento)

print(resul)