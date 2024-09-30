# Sistema de Transporte Masivo

## Descripción General

Este sistema implementa un modelo de transporte masivo utilizando la estructura de datos de grafo y el algoritmo de Dijkstra para encontrar la ruta más corta entre dos estaciones.
El sistema permite agregar estaciones, establecer conexiones entre ellas y calcular rutas óptimas.

## Clase Principal: TransporteMasivo

### Atributos

- `self.grafo`: Un diccionario que almacena las estaciones como claves y listas de tuplas (destino, costo) como valores, representando las conexiones y sus costos.

### Métodos

#### `__init__(self)`

Constructor de la clase. Inicializa el grafo como un diccionario vacío.

#### `agregar_estacion(self, estacion)`

Agrega una nueva estación al sistema.

**Parámetros:**

- `estacion`: String, nombre de la estación a agregar.

**Funcionamiento:**

- Si la estación no existe en el grafo, la agrega con una lista vacía de conexiones.

#### `agregar_conexion(self, origen, destino, costo)`

Establece una conexión bidireccional entre dos estaciones.

**Parámetros:**

- `origen`: String, nombre de la estación de origen.
- `destino`: String, nombre de la estación de destino.
- `costo`: Número, costo de la conexión.

**Funcionamiento:**

- Verifica que ambas estaciones existan en el grafo.
- Agrega la conexión en ambas direcciones (origen a destino y destino a origen).

#### `encontrar_ruta_optima(self, inicio, destino)`

Implementa el algoritmo de Dijkstra para encontrar la ruta más corta entre dos estaciones.

**Parámetros:**

- `inicio`: String, nombre de la estación de inicio.
- `destino`: String, nombre de la estación de destino.

**Funcionamiento:**

1. Inicializa las estructuras de datos necesarias (distancias, cola de prioridad, registro de rutas).
2. Implementa el algoritmo de Dijkstra:
   - Explora las estaciones comenzando desde la estación de inicio.
   - Actualiza las distancias y rutas más cortas a medida que se encuentran mejores caminos.
   - Utiliza una cola de prioridad para seleccionar eficientemente la siguiente estación a explorar.
3. Termina cuando se alcanza la estación de destino o se han explorado todas las estaciones alcanzables.

**Retorna:**

- Lista de estaciones que forman la ruta más corta (obtenida llamando a `reconstruir_ruta`).

#### `reconstruir_ruta(self, ruta_previa, inicio, destino)`

Reconstruye la ruta óptima desde el destino hasta el origen.

**Parámetros:**

- `ruta_previa`: Diccionario, almacena la estación anterior en la ruta más corta para cada estación.
- `inicio`: String, nombre de la estación de inicio.
- `destino`: String, nombre de la estación de destino.

**Funcionamiento:**

- Comienza desde la estación de destino y retrocede hasta la estación de inicio utilizando el diccionario `ruta_previa`.
- Construye la lista de estaciones en orden inverso y luego la invierte.

**Retorna:**

- Lista de estaciones que forman la ruta más corta, o una lista vacía si no se encontró una ruta.

## Instalación

1. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/santiherr32/sistema-inteligente-transporte-masivo.git
   cd sistema-inteligente-transporte-masivo
   ```

2. **Crear un entorno virtual (opcional pero recomendado)**:

   En sistemas Unix/macOS:

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

   En Windows:

   ```bash
   python -m venv env
   .\env\Scripts\activate
   ```

3. **Ejecutar el proyecto**:

   Una vez completada la instalación, se puede ejecutar el código principal del proyecto con el siguiente comando:

   ```bash
   python sistema-inteligente-transporte.py
   ```

## Ejemplo de Uso

```python
# Crear una instancia del sistema de transporte
transporte = TransporteMasivo()

# Agregar estaciones
transporte.agregar_estacion("Mamatoco")
transporte.agregar_estacion("Terminal de transportes")
transporte.agregar_estacion("La torta - Av. libertador")
transporte.agregar_estacion("SuperLicores Av. del Rio")
transporte.agregar_estacion("Edificio Posihueica")
transporte.agregar_estacion("Puerto de Santa Marta")

# Agregar conexiones entre estaciones
transporte.agregar_conexion("Mamatoco", "Terminal de transportes", 3)
transporte.agregar_conexion("Mamatoco", "Puerto de Santa Marta", 10)
transporte.agregar_conexion("Puerto de Santa Marta", "Edificio Posihueica", 1)
transporte.agregar_conexion("Mamatoco", "La torta - Av. libertador", 6)
transporte.agregar_conexion("Terminal de transportes", "SuperLicores Av. del Rio", 10)
transporte.agregar_conexion("La torta - Av. libertador", "SuperLicores Av. del Rio", 5)
transporte.agregar_conexion("SuperLicores Av. del Rio", "Edificio Posihueica", 7)

# Encontrar la ruta más óptima entre dos estaciones
ruta_optima = transporte.encontrar_ruta_optima("Edificio Posihueica", "Mamatoco")
print("Ruta óptima:", ruta_optima)
```

Este ejemplo crea un sistema de transporte con seis estaciones, establece conexiones entre ellas, y luego encuentra la ruta más óptima entre "Edificio Posihueica" y "Mamatoco"

## Notas Adicionales

- El sistema asume que todas las conexiones son bidireccionales.
- Los costos de las conexiones deben ser números positivos.
- El algoritmo de Dijkstra garantiza encontrar la ruta más corta en términos de costo total.
- Si no existe una ruta entre las estaciones de inicio y destino, el método `encontrar_ruta_optima` devolverá una lista vacía.

## Link Video Davis Galan Grafo

www.youtube.com/watch?v=-C1EPrIHt04



