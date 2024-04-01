import streamlit as st 
from PIL import Image

# config

st.set_page_config(page_title= "WuapasApp ✂️",page_icon= "", layout="wide")

def local_css(css_file):
    with open(css_file) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

local_css("style/main.css")
email_address ="sdominguezpagani@gmail.com"

#intro

with st.container():
    st.header("Hola somos Wapas")
    st.title("Creamos soluciones en tu cabello")
    st.write("Somos unas apacionadas en bellesa")

#sobre nosotros 

with st.container():
    st.write("----")
    left_column, right_column = st.columns((2))
    with left_column:
        st.header("Sobre Wapas 💅 ")
        st.write("""
                 ¡Bienvenidas a Wapas!

                En Wapas, no solo somos expertas en cabello, somos creadoras de confianza y belleza. Desde nuestro corazón de barrio con grandes aspiraciones, transformamos tu estilo con un toque personalizado y único.

                Soy Ángeles, la fundadora de Wapas, y durante los últimos cinco años nos hemos dedicado a realzar la belleza natural de cada mujer que entra por nuestras puertas.

                En Wapas, tu cabello es nuestra pasión, y estamos aquí para crear contigo una historia de belleza que resalte lo mejor de ti.

                Únete a nosotros en Wapas, donde la belleza se encuentra con la confianza.

                ***Ángeles y el equipo de Wapas***
                 """
                 )
    with right_column:
        st.empty() 

#servicios

with st.container():
    st.write("---")
    st.header("Nuestros servicios ☝️ ")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        image = Image.open("imagenes/alisado.jpg")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Alisados")
        st.write("""
                 En wapas nos especialisamos en alisados de calidad premiun
                 """)
        
with st.container():
    st.write("---")
    st.header("Nuestros servicios")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        image = Image.open("imagenes/celulas_madre.jpg")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Celulas Madres")
        st.write("""
                 Celulas Madres para que tu pelo cresca fuerte 
                 """)

with st.container():
    st.write("---")
    st.header("Nuestros servicios")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        image = Image.open("imagenes/corte.jpg")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Cortes")
        st.write("""
                 Cortes de cabello adaptados al grito de la moda.
                 """)           

# Contacto

with st.container():
    st.write("---")
    st.header("Ponte en contacto con nosotros 📩")
    st.write("##")
    contact_form = f"""
        <form action="https://formsubmit.co/{email_address}" method="POST">
        <input type= "hidden" name="_captcha" value="false">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Tu nombre" required>
        <input type="email" name="email" placeholder="Tu email" required>
        <textarea name="message" placeholder="Tu mensaje aquí" required></textarea>
        <button type="submit">Enviar</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()