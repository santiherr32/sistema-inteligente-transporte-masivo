import heapq

class TransporteMasivo:
    def __init__(self):
        self.grafo = {}  # Diccionario para almacenar las estaciones y sus conexiones

    def agregar_estacion(self, estacion):
        # Agregar una nueva estación (nodo) al grafo
        if estacion not in self.grafo:
            self.grafo[estacion] = []

    def agregar_conexion(self, origen, destino, costo):
        # Agregar una conexión (arista) entre dos estaciones con su respectivo costo
        if origen in self.grafo and destino in self.grafo:
            self.grafo[origen].append((destino, costo))
            self.grafo[destino].append((origen, costo))  # Si es bidireccional

    def encontrar_ruta_optima(self, inicio, destino):
        # Usar el algoritmo de Dijkstra para encontrar la ruta más corta
        distancias = {estacion: float('inf') for estacion in self.grafo}
        distancias[inicio] = 0
        prioridad = [(0, inicio)]
        ruta_previa = {estacion: None for estacion in self.grafo}
        
        while prioridad:
            costo_actual, estacion_actual = heapq.heappop(prioridad)

            if estacion_actual == destino:
                break

            for vecino, costo in self.grafo[estacion_actual]:
                nueva_distancia = costo_actual + costo
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    ruta_previa[vecino] = estacion_actual
                    heapq.heappush(prioridad, (nueva_distancia, vecino))

        return self.reconstruir_ruta(ruta_previa, inicio, destino)

    def reconstruir_ruta(self, ruta_previa, inicio, destino):
        # Reconstruir la ruta óptima desde el destino hasta el origen
        ruta = []
        estacion_actual = destino
        while estacion_actual:
            ruta.append(estacion_actual)
            estacion_actual = ruta_previa[estacion_actual]
        ruta.reverse()
        return ruta if ruta[0] == inicio else []

# Caso de uso
transporte = TransporteMasivo()

# Agregar estaciones (nodos)
transporte.agregar_estacion("Mamatoco")
transporte.agregar_estacion("Terminal de transportes")
transporte.agregar_estacion("La torta - Av. libertador")
transporte.agregar_estacion("SuperLicores Av. del Rio")
transporte.agregar_estacion("Edificio Posihueica")
transporte.agregar_estacion("Puerto de Santa Marta")

# Agregar conexiones (aristas) entre las estaciones con sus costos
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