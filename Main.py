import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

file_path = 'dataset.csv'
data = pd.read_csv(file_path)

# Grafo no dirigido
G = nx.Graph()

# Se agregan nodos y aristas al grafo
# Por defecto la librería usa listas de adyacencia para construir grafos
for index, row in data.iterrows():
    G.add_edge(row['Origen'], row['Destino'], km=row['KM'], minutos=row['Minutos'])


def es_conexion_unica(ciudad_origen, ciudad_destino):
    return len(list(nx.all_shortest_paths(G, source=ciudad_origen, target=ciudad_destino))) == 1


def mostrar_grafo():
    plt.figure(figsize=(1, 8))
    pos = nx.fruchterman_reingold_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=500, node_color='skyblue', font_size=10)
    plt.title("Grafo de Conexiones entre Ciudades")
    plt.show()


while True:
    print("\nSeleccione una opción:")
    print("1. Ruta más corta entre A y B en kilómetros")
    print("2. Ruta más corta entre A y B en minutos")
    print("3. Conexión por única carretera")
    print("4. Mostrar Grafo")
    print("5. Salir")


    opcion = input("Elige una opción (1-5): ")


    if opcion == '1':
        ciudad_origen = input("Ingresa la ciudad de origen: ")
        ciudad_destino = input("Ingresa la ciudad de destino: ")
        shortest_path = nx.shortest_path(G, source=ciudad_origen, target=ciudad_destino, weight='km')
        distancia = nx.shortest_path_length(G, source=ciudad_origen, target=ciudad_destino, weight='km')
        print(f"La ruta más corta en kilómetros entre {ciudad_origen} y {ciudad_destino} es: {shortest_path}")
        print(f"Distancia total: {distancia} km")

    elif opcion == '2':
        ciudad_origen = input("Ingresa la ciudad de origen: ")
        ciudad_destino = input("Ingresa la ciudad de destino: ")
        shortest_path = nx.shortest_path(G, source=ciudad_origen, target=ciudad_destino, weight='minutos')
        tiempo = nx.shortest_path_length(G, source=ciudad_origen, target=ciudad_destino, weight='minutos')
        print(f"La ruta más corta en minutos entre {ciudad_origen} y {ciudad_destino} es: {shortest_path}")
        print(f"Tiempo total: {tiempo} minutos")

    elif opcion == '3':
        ciudad_origen = input("Ingresa la ciudad de origen: ")
        ciudad_destino = input("Ingresa la ciudad de destino: ")
        if es_conexion_unica(ciudad_origen, ciudad_destino):
            print(f"{ciudad_origen} y {ciudad_destino} están conectadas por una única carretera.")
        else:
            print(f"{ciudad_origen} y {ciudad_destino} están conectadas por más de una carretera.")

    elif opcion == '4':
        mostrar_grafo()

    elif opcion == '5':
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, elige una opción del menú (1-5).")
