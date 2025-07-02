import streamlit as st
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
    image = Image.open(uploaded_file).convert("RGBA")
    st.image(image, caption="Imagen original", use_column_width=True)

    with st.spinner("Procesando imagen..."):
        # Quitar fondo
        result_image = remove(image)

        # Redimensionar con Pillow
        resized_image = result_image.resize((600, 600), Image.LANCZOS)

    st.image(resized_image, caption="Imagen sin fondo (600x600)", use_column_width=True)

    # Preparar para descarga
    buffer = io.BytesIO()
    resized_image.save(buffer, format="PNG")
    buffer.seek(0)

    st.download_button(
        label="📥 Descargar imagen procesada",
        data=buffer,
        file_name="imagen_sin_fondo_600x600.png",
        mime="image/png"
    )
