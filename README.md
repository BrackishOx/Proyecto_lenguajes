# Lenguaje Nativo

## 1. Descripcion General

Se desarrollo un lenguaje aritmetico nativo orientado a la evaluacion de expresiones matematicas basicas. 
El lenguaje fue implementado completamente desde cero sin utilizar generadores automaticos de analizadores lexicos o sintacticos.

Operaciones soportadas:

- Suma (+)
- Resta (-)
- Multiplicacion (*)
- Division (/)
- Parentesis

---

# 2. Analisis Lexico

## 2.1 Alfabeto

Σ = { 0–9, +, -, *, /, (, ), espacio }

## 2.2 Tokens

- NUM
- PLUS
- MINUS
- MULT
- DIV
- LPAREN
- RPAREN
- EOF

## 2.3 Expresiones Regulares Conceptuales

NUM → [0-9]+ 
PLUS → "+" 
MINUS → "-" 
MULT → "*" 
DIV → "/" 
LPAREN → "(" 
RPAREN → ")"

## 2.4 Implementacion

El analisis lexico fue implementado manualmente mediante un recorrido caracter por caracter, funcionando como un Automata Finito Determinista implicito.

---



# 3. Gramatica Formal (BNF)
# Lenguaje Aritmetico Nativo
<expresion> ::= <termino> { ("+" | "-") <termino> }

<termino> ::= <factor> { ("*" | "/") <factor> }

<factor> ::= NUM
| "(" <expresion> ")"

Propiedades:

- Gramatica libre de contexto
- Respeta precedencia de operadores

---

# 4. Analisis Sintactico

Se implemento un parser descendente recursivo LL(1).

Funciones principales:

- expr()
- term()
- factor()

Cada funcion corresponde directamente a una produccion de la gramatica.

---

# 5. Analisis Semantico

La evaluacion es dirigida por la sintaxis.

Operaciones:

- + → suma
- - → resta
- * → multiplicacion
- / → division

Se implementa validacion de division por cero.

---

# 6. Arquitectura del Sistema

entrada.txt → lexer.py → parser.py → main.py → resultado

Flujo:

1. main lee archivo
2. lexer tokeniza
3. parser valida y evalua
4. se imprime resultado

---

# 7. Caracteristicas Tecnicas

- Implementacion 100% manual
- Sin librerias externas
- Sin generadores automaticos
- Parser LL(1)
- Evaluacion inmediata
