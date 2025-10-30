import streamlit as st

# -----------------------------
# Configuración general
# -----------------------------
st.set_page_config(page_title="Agente Meteorológico Inteligente", page_icon="🌦️", layout="centered")

# -----------------------------
# Estilos CSS personalizados
# -----------------------------
st.markdown("""
<style>
    /* Fondo general - Compatible con Streamlit */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Contenedor principal */
    .block-container {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 20px;
        padding: 2rem !important;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
        max-width: 800px;
        margin-top: 2rem;
    }
    
    /* Título principal */
    .title {
        font-size: 2.5rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Subtítulo */
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.3rem;
        margin-bottom: 2rem;
        padding: 0 1rem;
        font-weight: 500;
    }
    
    /* Emoji grande */
    .emoji {
        font-size: 5rem;
        text-align: center;
        margin: 1.5rem 0;
        animation: float 3s ease-in-out infinite;
    }
    
    /* Animación de rotación + flotación para emojis específicos */
    .emoji-rotate {
        font-size: 5rem;
        text-align: center;
        margin: 1.5rem 0;
        animation: rotate-float 8s ease-in-out infinite;
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    @keyframes rotate-float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        25% { transform: translateY(-10px) rotate(90deg); }
        50% { transform: translateY(0px) rotate(180deg); }
        75% { transform: translateY(-10px) rotate(270deg); }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    /* Tarjetas de información */
    .card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
        border-left: 5px solid #667eea;
        font-size: 1.2rem;
        color: #333;
        font-weight: 500;
    }
    
    .card b {
        color: #1a1a1a;
        font-weight: 700;
    }
    
    /* Estado de ventanas */
    .ventanas {
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
        padding: 1rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .ventanas-abiertas {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        color: #2d6a4f;
        border: 3px solid #52b788;
    }
    
    .ventanas-cerradas {
        background: linear-gradient(135deg, #ffeaa7 0%, #fdcb6e 100%);
        color: #d63031;
        border: 3px solid #e17055;
    }
    
    /* Botones mejorados */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Slider personalizado */
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Labels del slider */
    .stSlider label {
        font-size: 1.8rem !important;
        font-weight: 700 !important;
        color: #333 !important;
        background: white;
        padding: 0.5rem 1.2rem;
        border-radius: 10px;
        display: inline-block;
        margin-bottom: 0.8rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    
    /* Forzar tamaño del texto del slider con más especificidad */
    .stSlider label p,
    .stSlider label span,
    .stSlider label div {
        font-size: 1.8rem !important;
        font-weight: 700 !important;
    }
    
    /* Selector aún más específico */
    [data-testid="stSlider"] label {
        font-size: 1.8rem !important;
    }
    
    [data-testid="stSlider"] label * {
        font-size: 1.8rem !important;
    }
    
    /* Expander personalizado - Encabezado */
    .streamlit-expanderHeader {
        background: white !important;
        border-radius: 10px;
        font-weight: 700 !important;
        color: #333 !important;
        border: 2px solid #667eea;
        font-size: 1.1rem;
        padding: 1rem !important;
    }
    
    .streamlit-expanderHeader:hover {
        background: #f8f9fa !important;
        border-color: #764ba2;
    }
    
    /* Forzar color del texto del expander */
    .streamlit-expanderHeader p,
    .streamlit-expanderHeader div,
    .streamlit-expanderHeader span,
    .streamlit-expanderHeader svg {
        color: #333 !important;
        fill: #333 !important;
    }
    
    /* Selector más específico para el header */
    [data-testid="stExpander"] summary {
        background: white !important;
        color: #333 !important;
        font-weight: 700 !important;
        border: 2px solid #667eea !important;
        border-radius: 10px !important;
        padding: 1rem !important;
    }
    
    [data-testid="stExpander"] summary * {
        color: #333 !important;
    }
    
    /* Contenido del expander */
    .streamlit-expanderContent {
        background: white !important;
        border: 2px solid #e0e0e0;
        border-top: none;
        border-radius: 0 0 10px 10px;
        padding: 1rem;
    }
    
    /* Texto dentro del expander */
    .streamlit-expanderContent p,
    .streamlit-expanderContent div,
    .streamlit-expanderContent span {
        color: #333 !important;
    }
    
    /* JSON dentro del expander */
    .streamlit-expanderContent pre {
        background: #f5f5f5 !important;
        color: #333 !important;
        padding: 1rem;
        border-radius: 8px;
    }
    
    .streamlit-expanderContent code {
        color: #333 !important;
    }
    
    /* Tablas */
    .stTable {
        border-radius: 10px;
        overflow: hidden;
    }
    
    /* Mejorar visibilidad de tablas */
    table {
        background: white !important;
        color: #333 !important;
    }
    
    table thead tr th {
        background: #667eea !important;
        color: white !important;
        font-weight: 700;
        padding: 0.75rem;
    }
    
    table tbody tr td {
        background: white !important;
        color: #333 !important;
        padding: 0.75rem;
        border-bottom: 1px solid #e0e0e0;
    }
    
    table tbody tr:nth-child(even) td {
        background: #f8f9fa !important;
    }
    
    table tbody tr:hover td {
        background: #e3f2fd !important;
    }
    
    /* Dataframe de Streamlit */
    [data-testid="stDataFrame"] {
        background: white !important;
    }
    
    [data-testid="stDataFrame"] * {
        color: #333 !important;
    }
    
    /* Mensajes de éxito */
    .stSuccess {
        background-color: #d4edda;
        border-left: 5px solid #28a745;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

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
        elif temp < 15:
            accion = "Cierra ventanas (frío detectado)"
            self.estado_ventanas = "cerradas"
        elif temp > 30:
            accion = "Abre ventanas (mucho calor detectado)"
            self.estado_ventanas = "abiertas"
        elif temp > 25:
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

# Espaciado
st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# Entradas del usuario
# -----------------------------
# Slider centrado (de 0 a 40°C)
temp = st.slider("🌡️ Temperatura actual (°C)", 0, 40, 25)

# Botón de lluvia debajo
if "lluvia" not in st.session_state:
    st.session_state.lluvia = False

# Centrar el botón de lluvia
col_izq, col_centro, col_der = st.columns([1, 2, 1])
with col_centro:
    if st.button("🌧️ Lluvia: " + ("SÍ ✅" if st.session_state.lluvia else "NO ❌"), key="btn_lluvia", use_container_width=True):
        st.session_state.lluvia = not st.session_state.lluvia
        st.rerun()

lluvia = st.session_state.lluvia

# Emoji representativo del clima
if lluvia:
    emoji_clima = "🌧️"
elif temp < 10:
    emoji_clima = "☃️"
elif temp < 15:
    emoji_clima = "❄️"
elif temp < 20:
    emoji_clima = "⛅"
elif temp < 25:
    emoji_clima = "🌤️"
elif temp < 30:
    emoji_clima = "☀️"
else:
    emoji_clima = "🔥"

# -----------------------------
# Mostrar condiciones actuales
# -----------------------------
# Usar clase de rotación solo para ❄️ y ☀️
emoji_class = "emoji-rotate" if emoji_clima in ["❄️", "☀️"] else "emoji"
st.markdown(f'<div class="{emoji_class}">{emoji_clima}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="card"><b>Condiciones actuales:</b> {temp}°C, {"🌧️ Lluvia" if lluvia else "☀️ Sin lluvia"}</div>', unsafe_allow_html=True)

# -----------------------------
# Acción del agente
# -----------------------------
analizar = st.button("🔍 Analizar clima", use_container_width=True)

if analizar:
    accion = agente.actuar(temp, lluvia)

    st.markdown(f'<div class="card"><b>🤖 Acción del agente:</b><br>{accion}</div>', unsafe_allow_html=True)

    if agente.estado_ventanas == "abiertas":
        # Centrar la imagen
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("ventana_abierta.png", use_container_width=True)
        st.markdown('<div class="ventanas ventanas-abiertas">✅ Ventanas Abiertas</div>', unsafe_allow_html=True)
    else:
        # Centrar la imagen
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("ventana_cerrada.png", use_container_width=True)
        st.markdown('<div class="ventanas ventanas-cerradas">🔒 Ventanas Cerradas</div>', unsafe_allow_html=True)

    with st.expander("🧠 Ver memoria interna del agente"):
        st.json(vars(agente.modelo))

    with st.expander("📋 Historial de decisiones"):
        if agente.historial:
            st.table(agente.historial)
        else:
            st.info("No hay historial todavía.")

# -----------------------------
# Botón reiniciar
# -----------------------------
st.markdown("<br>", unsafe_allow_html=True)
reiniciar = st.button("🔄 Reiniciar agente", use_container_width=True)

if reiniciar:
    st.session_state.agente = AgenteClima()
    st.success("✅ Agente reiniciado correctamente.")
    st.rerun()