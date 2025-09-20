EMOJI_PENDIENTE = "🟡"
EMOJI_COMPLETADO = "✅"

def agregar_estado(texto):
    return f"{EMOJI_PENDIENTE} {texto.strip()}"

def marcar_completado(tarea):
    if tarea.startswith(EMOJI_PENDIENTE):
        return tarea.replace(EMOJI_PENDIENTE, EMOJI_COMPLETADO, 1)
    elif tarea.startswith(EMOJI_COMPLETADO):
        return tarea.replace(EMOJI_COMPLETADO, EMOJI_PENDIENTE, 1)
    return tarea

