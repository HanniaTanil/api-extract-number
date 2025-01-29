# api-extract-number
API que calcula el numero faltante de un conjunto de los primeros 100 números naturales del cual se extrajo uno. Se usa FastAPI. 

Especificaciones:
-	Se debe de implementar una clase que represente al conjunto de los primeros 100 números
-	La clase implementada debe de tener el método Extract para extraer un cierto número deseado
-	La clase implementada debe de poder calcular que numero se extrajo y presentarlo
-	Debe de incluir validación del input de datos (numero, número menor de 100)
-	La aplicación debe de poder ejecutarse con un argumento introducido por el usuario que haga uso de nuestra clase y muestre que pudo calcular que se extrajo ese número


La API cuenta con dos endpoints
/extract 
Donde se extrae el numero ingresado del conjunto de los primeros cien números naturales y se calcula a partir de la diferencia
de sumas de los dos conjuntos.
Se valida que la entrada sea un número y sea menor a 100
Se vuelve a crear el conjunto de 100 números naturales para más consultas

/reset
Se vuelve a crear el conjunto de números naturales para más consultas
