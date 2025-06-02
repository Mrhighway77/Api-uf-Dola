import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Crear una figura y un eje
fig, ax = plt.subplots(figsize=(10, 6))

# Agregar módulos
modules = {
    "Módulo de API": (1, 4),
    "Módulo de Modelo Predictivo": (5, 4),
    "Frontend": (3, 2),
    "Base de Datos": (1, 1),
    "Sistema de Autenticación": (5, 1),
    "Sistema de Monitoreo": (3, 4),
}

# Dibujar rectángulos para cada módulo
for module, position in modules.items():
    rect = patches.Rectangle(position, 2, 1, edgecolor='black', facecolor='lightblue', lw=2)
    ax.add_patch(rect)
    ax.text(position[0] + 1, position[1] + 0.5, module, fontsize=10, ha='center', va='center')

# Conectores entre módulos, ajustados para evitar pasar por encima de los recuadros
connections = [
    ((2.1, 4.5), (3, 3.1)),  # API a Frontend
    ((6, 4.5), (4.9, 3.8)),  # Modelo Predictivo a Sistema de Monitoreo (más ajustado)
    ((2.1, 1.5), (3, 2.1)),  # Base de Datos a Frontend
    ((6, 1.5), (4.9, 3.9)),  # Sistema de Autenticación a Sistema de Monitoreo
]

# Dibujar líneas para conectores, ajustadas para evitar pasar por recuadros
for start, end in connections:
    ax.annotate("", xy=end, xycoords='data', xytext=start, textcoords='data',
                arrowprops=dict(arrowstyle="->", lw=2))

# Configuración del gráfico
ax.set_xlim(0, 8)
ax.set_ylim(0, 5)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Ilustración 4: Vista de Implementación', fontsize=12)

# Guardar el diagrama en la ruta indicada
plt.savefig('C:/Users/marco/OneDrive/Escritorio/Proyecto de Titulo/Diagramas Arquitectura/vista_de_implementacion.png', bbox_inches='tight')

plt.close()





#    python implementacion.py