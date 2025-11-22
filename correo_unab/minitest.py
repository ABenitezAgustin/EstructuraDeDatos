from usuario import Usuario
from mensaje import Mensaje
from carpeta import Carpeta

# --- Crear usuarios ---
agustin = Usuario("agustin", "agustin@unab.com", "Agustin1")
jennifer = Usuario("jennifer", "Jennifer@unab.com", "Jennifer1")
leonardo = Usuario("leonardo", "leonardo@unab.com", "Leonardo1")

# --- Crear subcarpetas para filtros ---
agustin.crear_subcarpeta("Bandeja de Entrada", "Trabajo")
jennifer.crear_subcarpeta("Bandeja de Entrada", "Personal")

# --- Agregar filtros ---
agustin.agregar_filtro("asunto", "URGENTE", "Trabajo")
jennifer.agregar_filtro("remitente", "leonardo@unab.com", "Personal")

# --- Enviar mensajes ---
agustin.enviar_mensaje(jennifer, "Hola Jennifer", "Mensaje normal de agustin")                # normal
agustin.enviar_mensaje(jennifer, "URGENTE: Reunión", "Tenemos que reunirnos", urgente=True)  # urgente
jennifer.enviar_mensaje(agustin, "Re: Hola", "Respuesta de jennifer a agustin")               # normal
leonardo.enviar_mensaje(jennifer, "Proyecto Y", "Revisar proyecto")                     # normal
leonardo.enviar_mensaje(agustin, "Proyecto X", "Información sobre proyecto")         # normal

# --- Mostrar bandejas ---
usuarios = [agustin, jennifer, leonardo]

for u in usuarios:
    print(f"\n========== Bandejas de {u.nombre} ==========")
    u.mostrar_bandeja_entrada()
    u.mostrar_bandeja_salida()

# --- Buscar mensajes ---
print("\n========== Buscar mensajes con contenido 'Proyecto' en Agustin ==========")
agustin.buscar_mensajes("contenido", "Proyecto")

print("\n========== Buscar mensajes con asunto 'URGENTE' en Agustin ==========")
agustin.buscar_mensajes("asunto", "URGENTE")

print("\n========== Buscar mensajes por remitente 'agustin@unab.com' en jennifer ==========")
jennifer.buscar_mensajes("remitente", "agustin@unab.com")

# --- Mover mensajes manualmente ---
print("\n========== Mover mensaje 'Hola jennifer' en jennifer a carpeta Personal ==========")
jennifer.mover_mensaje("Hola jennifer", "Bandeja de Entrada", "Personal")

# --- Procesar mensajes urgentes ---
print("\n========== Procesar mensajes urgentes de Agustin ==========")
agustin.procesar_mensajes_urgentes_entrada()
agustin.procesar_mensajes_urgentes_salida()
agustin.mostrar_bandeja_entrada()
agustin.mostrar_bandeja_salida()

print("\n========== Procesar mensajes urgentes de jennifer ==========")
jennifer.procesar_mensajes_urgentes_entrada()
jennifer.procesar_mensajes_urgentes_salida()
jennifer.mostrar_bandeja_entrada()
jennifer.mostrar_bandeja_salida()

print("\n========== Procesar mensajes urgentes de leonardo ==========")
leonardo.procesar_mensajes_urgentes_entrada()
leonardo.procesar_mensajes_urgentes_salida()
leonardo.mostrar_bandeja_entrada()
leonardo.mostrar_bandeja_salida()

print("\n=== Mini test completo: todos los casos probados ===")

