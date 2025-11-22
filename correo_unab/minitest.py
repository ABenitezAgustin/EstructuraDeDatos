from usuario import Usuario
from mensaje import Mensaje
from carpeta import Carpeta

# --- Crear usuarios ---
alice = Usuario("Alice", "alice@unab.com", "Alice123")
bob = Usuario("Bob", "bob@unab.com", "Bob1234")
carol = Usuario("Carol", "carol@unab.com", "Carol123")

# --- Crear subcarpetas para filtros ---
alice.crear_subcarpeta("Bandeja de Entrada", "Trabajo")
bob.crear_subcarpeta("Bandeja de Entrada", "Personal")

# --- Agregar filtros ---
alice.agregar_filtro("asunto", "URGENTE", "Trabajo")
bob.agregar_filtro("remitente", "carol@unab.com", "Personal")

# --- Enviar mensajes ---
alice.enviar_mensaje(bob, "Hola Bob", "Mensaje normal de Alice")                # normal
alice.enviar_mensaje(bob, "URGENTE: Reunión", "Debemos reunirnos", urgente=True)  # urgente
bob.enviar_mensaje(alice, "Re: Hola", "Respuesta de Bob a Alice")               # normal
carol.enviar_mensaje(bob, "Proyecto Y", "Revisar proyecto")                     # normal
carol.enviar_mensaje(alice, "Proyecto X", "Información sobre proyecto")         # normal

# --- Mostrar bandejas ---
usuarios = [alice, bob, carol]

for u in usuarios:
    print(f"\n========== Bandejas de {u.nombre} ==========")
    u.mostrar_bandeja_entrada()
    u.mostrar_bandeja_salida()

# --- Buscar mensajes ---
print("\n========== Buscar mensajes con contenido 'Proyecto' en Alice ==========")
alice.buscar_mensajes("contenido", "Proyecto")

print("\n========== Buscar mensajes con asunto 'URGENTE' en Alice ==========")
alice.buscar_mensajes("asunto", "URGENTE")

print("\n========== Buscar mensajes por remitente 'carol@unab.com' en Bob ==========")
bob.buscar_mensajes("remitente", "carol@unab.com")

# --- Mover mensajes manualmente ---
print("\n========== Mover mensaje 'Hola Bob' en Bob a carpeta Personal ==========")
bob.mover_mensaje("Hola Bob", "Bandeja de Entrada", "Personal")

# --- Procesar mensajes urgentes ---
print("\n========== Procesar mensajes urgentes de Alice ==========")
alice.procesar_mensajes_urgentes_entrada()
alice.procesar_mensajes_urgentes_salida()
alice.mostrar_bandeja_entrada()
alice.mostrar_bandeja_salida()

print("\n========== Procesar mensajes urgentes de Bob ==========")
bob.procesar_mensajes_urgentes_entrada()
bob.procesar_mensajes_urgentes_salida()
bob.mostrar_bandeja_entrada()
bob.mostrar_bandeja_salida()

print("\n========== Procesar mensajes urgentes de Carol ==========")
carol.procesar_mensajes_urgentes_entrada()
carol.procesar_mensajes_urgentes_salida()
carol.mostrar_bandeja_entrada()
carol.mostrar_bandeja_salida()

print("\n=== Mini test completo: todos los casos probados ===")

