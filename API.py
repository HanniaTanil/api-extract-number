#Api que calcula el número faltante de un conjunto de los 
#primeros 100 números naturales del cual se extrajo uno

##Hannia Tanil Padilla Escobar 
##28 de enero de 2025

from fastapi import FastAPI, HTTPException, Request 
from pydantic import BaseModel, Field #validación de los datos
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

#Clase para representar el conjunto de números
class NumerosNaturales:
    def __init__(self, n=100):
        self.n = n
        #Se crea el conjunto de números del 1 al 100
        self.full_set = set(range(1, self.n +1))
        #Se copia el conjunto original
        self.current_set = self.full_set.copy()
    
    def extract(self, number: int):
        #Se verifica que el número "number" exista en el conjunto current_set
        #Si existe se elimina del conjunto
        #Si no existe se lanza un error
        if number in self.current_set:
            self.current_set.remove(number)
        else:
            raise ValueError(f"El número {number} no está en el conjunto actual.")
        
    def encontrar_numero_faltante(self):
        # Calcular la suma esperada y restar la suma actual para encontrar el faltante
        #Calcula la suma de los números extraídos, aún si es más de uno
        suma_esperada = self.n * (self.n + 1) // 2
        suma_actual = sum(self.current_set)
        return suma_esperada - suma_actual
    
    def reset(self):
        self.current_set = self.full_set.copy()


# Modelo de entrada para la API
#Se usa Pydantic para validar los datos que el usuario envía
class ExtractRequest(BaseModel):
    number: int = Field(..., description="Número a extraer del conjunto (entre 1 y 100)")

# se crea una instancia de FastAPI
app = FastAPI()

# Instancia de la clase NumerosNaturales
numeros = NumerosNaturales()

#Capturar errores 422 (en caso de un formato que no sea número)
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detalles": "Error en la solicitud: Asegurate de enviar un número entero válido"}
    )

#endpoint extract
@app.post("/extract")
def extract_number(request: ExtractRequest):
    
    #Endpoint para extraer un número del conjunto.
    #Valida el número y devuelve el faltante.
    
    number = request.number

    if not (1 <= number <= 100):
        raise HTTPException(status_code=400, detail="El número debe estar entre 1 y 100.")
    
    try:
        # se llama al método extract
        numeros.extract(number)
        numero_faltante = numeros.encontrar_numero_faltante()
        response = {
            "message": f"Número {number} extraído correctamente.",
            "numero extraído": numero_faltante,
        }
    
        #Reiniciar el conjunto automáticamente
        numeros.reset()

        return response
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

#endpoint reset
@app.get("/reset")
def reset_set():
    """
    Endpoint para reiniciar el conjunto de números a su estado original.
    """
    numeros.reset()
    return {"message": "Conjunto reiniciado correctamente."}