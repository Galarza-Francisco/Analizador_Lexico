# Analizador Léxico: Es la primera fase de un compilador o intérprete. Su función es convertir una secuencia de caracteres en una secuencia de tokens, que son unidades significativas del lenguaje.
# Tokens: Son las unidades básicas de un lenguaje de programación. Pueden ser palabras clave, identificadores, números, operadores, etc.
# Expresiones Regulares: Son patrones de búsqueda de texto que permiten definir de manera concisa y flexible las reglas para reconocer tokens.


import re 
# se importa re para trabajar con expresiones regulares

class AnalizadorLexico:
    # defino clase, defino los atributos(datos) y metodos(funcoines) que va a tenr el objeto
    def __init__(self):
        # creo la clase, haciendo referencia a self, que es el objeto actual.
        # self.patron creo un atributo patron en el objeto
        # re.compile() complila la expresion regular que despues se usa para buscar coincidencias.
        # r'' indica que es una cadena raw, que es una cadena sin formato trata a las \ como un caracter literal.  
        # la expresion regular esta armada por dos partes, separadas por el | (or). tiene de un lado la expresion regular y del otro el nombre que la identifica.
        # se crea un atrinuto palabras resevadas para las palablas de python.
        self.palabras_reservadas = set([
            'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
            'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
            'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
            'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
        ])
        self.patron = re.compile(r'(?P<NUMERO_REAL>\d+\.\d+)|' r'(?P<NUMERO_ENTERO>\d+)|' r'(?P<IDENTIFICADOR>[a-zA-Z_]\w*)|' r'(?P<ASIGNACION>=)|' r'(?P<OTRO>\S)')


        # Operadores
        # (?P<OPERADOR>==|!=|<=|>=|[-+*/%=<>])

    def analizar(self, texto): 
        # metodo para analizar el texto de entrada, tiene como parametro esta cadena y self es el objeto actual.
        tokens_clasificados = [] # se crea un array vacio para giuardar los resultados
        #el bucle for itera sobre cada coincidencia encontrada
        for match in self.patron.finditer(texto):
            # self.patron.finditer(texto) busca todas las coincidencias de la expresion regular en el texto
            # finditer devuelve un iterador que permite recorrer cada coincidencia encontrada
           
            # develve el nombre del ultimo grupo que coincidio en la expresion regular. eso nos da el tipo de token que es (identificador, numero real, numero entero, etc.)
            tipo = match.lastgroup

            # devuelve la cadena completa que coincidio en la expresion regular. da el "valor" del token
            valor = match.group()
            # condicional para ver si el identificador es una palabra reservada
            if tipo == 'IDENTIFICADOR' and valor in self.palabras_reservadas:
                tipo = 'PALABRA_RESERVADA'
            elif tipo == 'ESPACIO':
                continue  # no le damos bola a los espacios
            # con append se agrega un elemento al array, con la tupla (tipo, valor)
            tokens_clasificados.append((tipo, valor))

        return tokens_clasificados # devuelve el array con los tokens ya clasificados



