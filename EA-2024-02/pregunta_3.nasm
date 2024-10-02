JMP inicio

cadena:
    DB "FE EN TI", 0  ; Cadena de texto

inicio:
    MOV A, 0  ; Inicializar contador de palabras
    MOV B, 0  ; Variable temporal
    MOV D, cadena  ; Dirección de la cadena
    MOV C, 232  ; Dirección para almacenar resultado

analizar:
    MOV B, [D]
    CMP B, ' '
    JZ  encontrado_espacio
    CMP B, 0
    JZ  finalizar
    INC D
    JMP analizar

encontrado_espacio:
    INC A
    INC D
    JMP analizar

finalizar:
    INC A  ; Incluir última palabra
    CMP A, 10
    JAE manejar_dos_digitos

    MOV B, '0'
    MOV [C], B
    INC C

manejar_dos_digitos:
    MOV B, A
    ADD B, '0'
    MOV [C], B
    HLT
