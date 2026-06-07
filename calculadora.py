import math
import streamlit as st

# Configuración de la página web
st.set_page_config(page_title="Tu Calculadora Geometrica", page_icon="🧮", layout="centered")

st.title("🧮 Tu Calculador WEB a mano")
st.write("Bienvenido al proyecto de calculadora de figuras planas y sólidos regulares.")

# Crear pestañas en la página web
tab1, tab2 = st.tabs(["🔺 Figuras Planas", "📦 Sólidos Regulares"])

# ==========================================
# PESTAÑA 1: FIGURAS PLANAS
# ==========================================
with tab1:
    st.header("Cálculo de Área y Perímetro")
    figura = st.selectbox("Selecciona una figura plana:", ["Cuadrado", "Rectángulo", "Triángulo", "Círculo"])
    
    st.markdown("---")
    
    if figura == "Cuadrado":
        lado = st.number_input("Ingresa el lado (l):", min_value=0.0, value=1.0, step=0.1)
        area = lado ** 2
        perimetro = 4 * lado
        st.success(f"**Área ($l^2$):** {area:.2f}")
        st.success(f"**Perímetro ($4 \\cdot l$):** {perimetro:.2f}")
        
    elif figura == "Rectángulo":
        base = st.number_input("Ingresa la base (b):", min_value=0.0, value=1.0, step=0.1)
        altura = st.number_input("Ingresa la altura (h):", min_value=0.0, value=1.0, step=0.1)
        area = base * altura
        perimetro = 2 * (base + altura)
        st.success(f"**Área ($b \\cdot h$):** {area:.2f}")
        st.success(f"**Perímetro ($2b + 2h$):** {perimetro:.2f}")
        
    elif figura == "Triángulo":
        base = st.number_input("Ingresa la base para el área:", min_value=0.0, value=1.0, step=0.1)
        altura = st.number_input("Ingresa la altura para el área:", min_value=0.0, value=1.0, step=0.1)
        st.caption("Para el perímetro, ingresa los tres lados:")
        l1 = st.number_input("Lado 1:", min_value=0.0, value=1.0, step=0.1)
        l2 = st.number_input("Lado 2:", min_value=0.0, value=1.0, step=0.1)
        l3 = st.number_input("Lado 3:", min_value=0.0, value=1.0, step=0.1)
        
        area = (base * altura) / 2
        perimetro = l1 + l2 + l3
        st.success(f"**Área ($\\frac{{b \\cdot h}}{{2}}$):** {area:.2f}")
        st.success(f"**Perímetro ($a + b + c$):** {perimetro:.2f}")
        
    elif figura == "Círculo":
        radio = st.number_input("Ingresa el radio (r):", min_value=0.0, value=1.0, step=0.1)
        area = math.pi * (radio ** 2)
        perimetro = 2 * math.pi * radio
        st.success(f"**Área ($\\pi \\cdot r^2$):** {area:.2f}")
        st.success(f"**Perímetro ($2 \\cdot \\pi \\cdot r$):** {perimetro:.2f}")

# ==========================================
# PESTAÑA 2: SÓLIDOS REGULARES
# ==========================================
with tab2:
    st.header("Cálculo de Volumen")
    solido = st.selectbox("Selecciona un sólido:", ["Cubo", "Esfera", "Cilindro", "Cono"])
    
    st.markdown("---")
    
    if solido == "Cubo":
        arista = st.number_input("Ingresa la arista (a):", min_value=0.0, value=1.0, step=0.1)
        volumen = arista ** 3
        st.info(f"**Volumen ($a^3$):** {volumen:.2f}")
        
    elif solido == "Esfera":
        radio = st.number_input("Ingresa el radio (r):", min_value=0.0, value=1.0, step=0.1)
        volumen = (4/3) * math.pi * (radio ** 3)
        st.info(f"**Volumen ($\\frac{{4}}{{3}} \\cdot \\pi \\cdot r^3$):** {volumen:.2f}")
        
    elif solido == "Cilindro":
        radio = st.number_input("Ingresa el radio de la base (r):", min_value=0.0, value=1.0, step=0.1)
        altura = st.number_input("Ingresa la altura (h):", min_value=0.0, value=1.0, step=0.1)
        volumen = math.pi * (radio ** 2) * altura
        st.info(f"**Volumen ($\\pi \\cdot r^2 \\cdot h$):** {volumen:.2f}")
        
    elif solido == "Cono":
        radio = st.number_input("Ingresa el radio de la base (r):", min_value=0.0, value=1.0, step=0.1)
        altura = st.number_input("Ingresa la altura (h):", min_value=0.0, value=1.0, step=0.1)
        volumen = (1/3) * math.pi * (radio ** 2) * altura
        st.info(f"**Volumen ($\\frac{{1}}{{3}} \\cdot \\pi \\cdot r^2 \\cdot h$):** {volumen:.2f}")
