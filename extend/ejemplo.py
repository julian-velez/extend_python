# Creamos una lista inicial llamada 'marcas_ropa' que contiene algunas marcas de ropa
marcas_ropa = ['nike', 'adidas', 'puma', 'reebok']

# Creamos otra lista llamada 'agregar_nueva_marca' con marcas adicionales
agregar_nueva_marca = ['Dior', 'gucci', 'prada']

# Usamos el método 'extend' para añadir todos los elementos de la lista 'agregar_nueva_marca'
# al final de la lista 'marcas_ropa'
marcas_ropa.extend(agregar_nueva_marca)

# Imprimimos la lista final, que ahora contiene todas las marcas originales más las nuevas
print(marcas_ropa)
