import streamlit as st
import cv2
import numpy as np
from PIL import Image
from rembg import remove
import io

st.set_page_config(page_title="Quitar fondo y redimensionar", layout="centered")
st.title("🖼️ Quitar fondo y redimensionar imagen (600x600)")

st.markdown("""
Sube una imagen (JPG, JPEG o PNG). La aplicación quitará el fondo y redimensionará la imagen a 600x600 píxeles, lista para Mercado Libre.
""")

uploaded_file = st.file_uploader("Sube tu imagen", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Mostrar imagen original
    image = Image.open(uploaded_file).convert("RGBA")
    st.image(image, caption="Imagen original", use_column_width=True)

    with st.spinner("Procesando imagen..."):
        # Quitar fondo
        result_image = remove(image)

        # Convertir a numpy y redimensionar
        result_np = np.array(result_image)
        resized = cv2.resize(result_np, (600, 600), interpolation=cv2.INTER_AREA)

        # Convertir de vuelta a PIL
        final_image = Image.fromarray(resized)

    # Mostrar imagen procesada
    st.image(final_image, caption="Imagen sin fondo (600x600)", use_column_width=True)

    # Preparar descarga
    buffer = io.BytesIO()
    final_image.save(buffer, format="PNG")
    buffer.seek(0)

    st.download_button(
        label="📥 Descargar imagen procesada",
        data=buffer,
        file_name="imagen_sin_fondo_600x600.png",
        mime="image/png"
    )
