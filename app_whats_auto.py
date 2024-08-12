import streamlit as st
import pandas as pd
import json
import pywhatkit
import duckdb
import time

# Inicializar estado
if 'stop_loop' not in st.session_state:
    st.session_state.stop_loop = False
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# Función para formatear el texto
def format_text(text, name, time):
    return text.replace('NAME', name).replace('TIME', time)

def get_first_name(full_name):
    return full_name.split()[0]  # Toma el primer nombre

def stop_loop_fn():
    st.session_state.stop_loop = True

def send_messages(df, tiempo_abrir, tiempo_cerrar):
    for idx in range(st.session_state.current_index, len(df)):

        print(st.session_state.current_index)
        
        if st.session_state.stop_loop:
            st.write("Proceso detenido por el usuario.")
            break

        row = df.iloc[idx]
        service_name = row['service_name']
        name = get_first_name(row['name'])  # Obtener solo el primer nombre
        event_time = row['date_event']
        phone = row['phone']

        print(name, service_name, phone)
        
        # Buscar el texto correspondiente al service_name
        service_text = next((item['text'] for item in data['information'] if item['service_name'] == service_name), None)
        
        if service_text:
            # Formatear el texto con el nombre y la hora
            formatted_text = format_text(service_text, name, event_time)
            pywhatkit.sendwhatmsg_instantly(f"+{phone}", f"{formatted_text}", wait_time=tiempo_abrir, close_time=tiempo_cerrar, tab_close=False)
        else:
            st.write(f"No se encontró texto para el servicio: {service_name}")

        # Guardar el índice actual en st.session_state
        st.session_state.current_index += 1
        time.sleep(1)  # Esperar un momento antes de enviar el siguiente mensaje

    if not st.session_state.stop_loop:
        st.write("Todos los mensajes fueron enviados.")
        st.session_state.current_index = 0  # Reiniciar el índice después de completar

data = {
    "location": "BUDAPEST",
    "information": [
        {
            "service_name": "JEWISH QUARTER FREE TOUR (ENGLISH)",
            "text": f"""Hello NAME 🤗

You booked through our website for a tour of one of our partners! Get ready for the Budapest tour tomorrow at TIME ⏰ - we're expecting to see you!

The Free Tour of the Jewish Quarter: World War II and the Holocaust starts in front of the Great Synagogue of Budapest (Dohány utcai Zsinagóga)   - https://maps.app.goo.gl/1Biky6XtemSXmSzJ8

It's crucial to inform us early if you can't make it, so the guide doesn't wait. Please reply, can we count on you ❓
YES to confirm your attendance 🙂
NO to cancel your booking 🙁

To improve our organization, we kindly ask you to arrive 15 minutes before the start of the tour and check-in with your guide.

Lastly, follow us on Instagram at instagram.com/sandemanstours and be a part of a travel community like no other 💛

Best wishes and safe travels,

Mercedes | SANDEMANs Tours"""
        },
        {
            "service_name": "DISCOVERING BUDAPEST: INTRODUCTION TO HUNGARY",
            "text": f"""Hello NAME 🤗

You booked through our website for a tour of one of our partners! Get ready for the Budapest tour tomorrow at TIME ⏰ - we're expecting to see you!

The Free Tour of Budapest starts at Lajos Kossuth Square, in front of the Parliament   - https://maps.app.goo.gl/4XC5du8ktF2SAvch9

It's crucial to inform us early if you can't make it, so the guide doesn't wait. Please reply, can we count on you ❓
YES to confirm your attendance 🙂
NO to cancel your booking 🙁

To improve our organization, we kindly ask you to arrive 15 minutes before the start of the tour and check-in with your guide.

Lastly, follow us on Instagram at instagram.com/sandemanstours and be a part of a travel community like no other 💛

Best wishes and safe travels,

Mercedes | SANDEMANs Tours
"""
        },
        {
            "service_name": "FREE TOUR BARRIO JUDÍO: II GUERRA MUNDIAL Y HOLOCAUSTO",
            "text": f"""Hola NAME 🤗

¡Has reservado a través de nuestro sitio web para un tour con uno de nuestros socios! Prepárate para el tour en Budapest mañana a las TIME ⏰ - ¡te esperamos!

El Free Tour del barrio judío: Segunda Guerra Mundial y Holocausto comienza delante de la Gran Sinagoga de Budapest (Dohány utcai Zsinagóga) - https://maps.app.goo.gl/1Biky6XtemSXmSzJ8

Es crucial que nos informes con antelación si no puedes asistir, para que el guía no espere. Por favor, responde, ¿podemos contar contigo ❓
SÍ para confirmar tu asistencia 🙂
NO para cancelar tu reserva 🙁

Para mejorar nuestra organización, te pedimos amablemente que llegues 15 minutos antes del inicio del tour y te registres con tu guía.

Por último, síguenos en Instagram en instagram.com/sandemanstours y sé parte de una comunidad de viajeros como ninguna otra 💛

Mis mejores deseos y buen viaje, 

Mercedes | SANDEMANs Tours

"""
        },
        {
            "service_name": "FREE TOUR BUDAPEST ESENCIAL: INTRODUCCIÓN A HUNGRÍA",
            "text": f"""Hola NAME 🤗

¡Has reservado a través de nuestro sitio web para un tour con uno de nuestros socios! Prepárate para el tour en Budapest mañana a las TIME ⏰ - ¡te esperamos!

El Free Tour por Budapest comienza en la Plaza Lajos Kossuth, frente al Parlamento  - https://maps.app.goo.gl/4XC5du8ktF2SAvch9

Es crucial que nos informes con antelación si no puedes asistir, para que el guía no espere. Por favor, responde, ¿podemos contar contigo ❓
SÍ para confirmar tu asistencia 🙂
NO para cancelar tu reserva 🙁

Para mejorar nuestra organización, te pedimos amablemente que llegues 15 minutos antes del inicio del tour y te registres con tu guía.

Por último, síguenos en Instagram en instagram.com/sandemanstours y sé parte de una comunidad de viajeros como ninguna otra 💛

Mis mejores deseos y buen viaje, 

Mercedes | SANDEMANs Tours

"""
        },
        {
            "service_name": "BUDA'S CASTLE DISTRIC FREE TOUR (ENGLISH)",
            "text": f"""Hello NAME 🤗

You booked through our website for a tour of one of our partners! Get ready for the Budapest tour tomorrow at TIME ⏰ - we're expecting to see you!

The Buda Castle Free Tour starts at Clark Adam Square (Clark Ádám tér), next to the Zero Kilometer Stone - https://maps.app.goo.gl/ShqiHgnBPL6CcwzC8

It's crucial to inform us early if you can't make it, so the guide doesn't wait. Please reply, can we count on you ❓
YES to confirm your attendance 🙂
NO to cancel your booking 🙁

To improve our organization, we kindly ask you to arrive 15 minutes before the start of the tour and check-in with your guide.

Lastly, follow us on Instagram at instagram.com/sandemanstours and be a part of a travel community like no other 💛

Best wishes and safe travels,

Mercedes | SANDEMANs Tours
"""
        }
    ]
}

json_data = json.dumps(data, ensure_ascii=False, indent=4)

############################################################################################

st.title("Automatización envío de mensajes de WhatsApp")

# Subir archivo
uploaded_file = st.file_uploader("Subir el archivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Vista previa del archivo:")
    st.write(df)
    
    # Convertir la columna `date_event` a formato de hora
    if 'date_event' in df.columns:
        df['date_event'] = pd.to_datetime(df['date_event'], errors='coerce').dt.strftime('%I:%M %p')
    
    # Definir variables manuales
    tiempo_abrir = st.number_input('Ingresar segundos que tarda en abrir WhatsApp Web:', value=7)
    tiempo_cerrar = st.number_input('Ingresar segundos que tarda en cerrar WhatsApp Web:', value=3)

    # Botón para detener el envío de mensajes
    st.button("Detener envío de mensajes", key="stop_button", on_click=stop_loop_fn)
    
    # Botón para ejecutar el for loop
    if st.button("Enviar mensajes", key="start_button"):
        st.session_state.stop_loop = False  # Reiniciar el flag
        send_messages(df, tiempo_abrir, tiempo_cerrar)