from analizador_lexico import AnalizadorLexico
# importamos el analizador lexico
if __name__ == "__main__":  
    # texto que se quiere analizar
    textoAnalizar = '** cadena // //= 0.23 cadena .23 none 0.23e1 0.23e-1 0.23E1 0.23E-1 -.23  _   45'

    # Creamos una instancia (objeto) del analizador
    analizador = AnalizadorLexico()

    # llamamos al metodo analizar del objeto analizador, pasamos el texto como parametro, y se guarda el resultado (arrya de tokens) en la variable resultado.
    resultado = analizador.analizar(textoAnalizar)

    # printeamos los resultados
    print("Tokens encontrados:")
    # recorremos el array de tokens iterando sobre cada elemento tipo de token - valor de Token
    for tipo, valor in resultado:
        print(f"{valor} ---> Tipo: {tipo}")
        print('-------------------------------')

