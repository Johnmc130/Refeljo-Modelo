import streamlit as st

# -----------------------------
# Configuración general
# -----------------------------
st.set_page_config(page_title="Agente Meteorológico Inteligente", page_icon="🌦️", layout="centered")

# -----------------------------
# Clase del modelo
# -----------------------------
class ModeloClima:
    def __init__(self):
        self.lluvia_anterior = False
        self.temp_anterior = 25

# -----------------------------
# Clase del agente
# -----------------------------
class AgenteClima:
    def __init__(self):
        self.modelo = ModeloClima()
        self.estado_ventanas = "cerradas"
        self.historial = []

    def actuar(self, temp, lluvia):
        # Decisión del agente basada en el modelo
        if lluvia:
            accion = "Cierra ventanas (lluvia detectada)"
            self.estado_ventanas = "cerradas"
        elif self.modelo.lluvia_anterior:
            accion = "Espera (reciente lluvia, se está secando)"
        elif temp < 20:
            accion = "Cierra ventanas (frío detectado)"
            self.estado_ventanas = "cerradas"
        elif temp > 27:
            accion = "Abre ventanas (calor detectado)"
            self.estado_ventanas = "abiertas"
        else:
            accion = "Mantiene estado actual"

        # Actualizar el modelo
        self.modelo.lluvia_anterior = lluvia
        self.modelo.temp_anterior = temp

        # Guardar historial
        self.historial.append({
            "temperatura": temp,
            "lluvia": lluvia,
            "accion": accion,
            "ventanas": self.estado_ventanas
        })

        return accion

# -----------------------------
# Estado persistente
# -----------------------------
if "agente" not in st.session_state:
    st.session_state.agente = AgenteClima()
agente = st.session_state.agente

# -----------------------------
# Encabezado
# -----------------------------
st.markdown('<div class="title">🌤️ Agente Meteorológico Inteligente</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Simula un agente que abre o cierra las ventanas según el clima y su memoria interna.</div>', unsafe_allow_html=True)

# -----------------------------
# Entradas del usuario
# -----------------------------
temp = st.slider("🌡️ Temperatura actual (°C)", 10, 40, 25)
lluvia = st.toggle("🌧️ ¿Está lloviendo ahora?", False)

# Emoji representativo del clima
if lluvia:
    emoji_clima = "🌧️"
elif temp > 27:
    emoji_clima = "☀️"
elif temp < 20:
    emoji_clima = "❄️"
else:
    emoji_clima = "⛅"

# -----------------------------
# Mostrar condiciones actuales
# -----------------------------
st.markdown(f'<div class="emoji">{emoji_clima}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="card"><b>Condiciones actuales:</b> {temp}°C, {"🌧️ Lluvia" if lluvia else "☀️ Sin lluvia"}</div>', unsafe_allow_html=True)

# -----------------------------
# Acción del agente
# -----------------------------
if st.button("🔍 Analizar clima"):
    accion = agente.actuar(temp, lluvia)

    st.markdown(f'<div class="card"><b>🤖 Acción del agente:</b><br>{accion}</div>', unsafe_allow_html=True)

    if agente.estado_ventanas == "abiertas":
        st.markdown('<div class="emoji">🪟</div>', unsafe_allow_html=True)
        st.markdown('<div class="ventanas ventanas-abiertas">Ventanas abiertas</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="emoji">🚪</div>', unsafe_allow_html=True)
        st.markdown('<div class="ventanas ventanas-cerradas">Ventanas cerradas</div>', unsafe_allow_html=True)

    with st.expander("🧠 Ver memoria interna del agente"):
        st.json(vars(agente.modelo))

    with st.expander("📋 Historial de decisiones"):
        st.table(agente.historial)

# -----------------------------
# Botón reiniciar
# -----------------------------
if st.button("🔄 Reiniciar agente"):
    st.session_state.agente = AgenteClima()
    st.success("Agente reiniciado correctamente.")
