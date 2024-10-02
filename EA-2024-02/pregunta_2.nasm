; Inicialización de variables
MOV A, 80      ; Velocidad del primer tramo (80 km/h)
MOV B, 1       ; Tiempo del primer tramo (1h)
MOV C, 0       ; Registro para la distancia total (inicializado en 0)
MOV D, 3       ; Contador de tramos (3 tramos)

LOOP:
  ; Guardar la velocidad original en un registro temporal
  PUSH A       ; Guardamos la velocidad original (A) en la pila
  
  ; Calcular distancia del tramo actual: distancia = velocidad * tiempo
  MUL B        ; Multiplicar A (velocidad) por B (tiempo), resultado en A
  
  ; Sumar el resultado al acumulador de distancia total
  ADD C, A     ; Sumar la distancia del tramo a la parte baja (C)
  
  ; Restaurar la velocidad original para ajustarla al siguiente tramo
  POP A        ; Recuperamos la velocidad original desde la pila
  
  ; Ajustar velocidad y tiempo para el siguiente tramo
  SHR A, 1     ; Dividir la velocidad por 2
  SHL B, 1     ; Multiplicar el tiempo por 2

  ; Decrementar el contador de tramos
  DEC D
  JNZ LOOP     ; Si el contador no es 0, repetir el bucle

HLT            ; Detener la ejecución
