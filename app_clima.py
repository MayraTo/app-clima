import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "TU_API_KEY_AQUI"

def obtener_clima():
    ciudad = entrada_ciudad.get().strip()

    if not ciudad:
        messagebox.showwarning("Aviso", "Por favor ingresa una ciudad")
        return

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad},MX&appid={API_KEY}&units=metric&lang=es"
        respuesta = requests.get(url)

        if respuesta.status_code != 200:
            messagebox.showerror("Error", f"{respuesta.status_code}: {respuesta.text}")
            return

        datos = respuesta.json()

        temp = datos["main"]["temp"]
        sensacion = datos["main"]["feels_like"]
        humedad = datos["main"]["humidity"]
        viento = datos["wind"]["speed"]
        desc = datos["weather"][0]["description"]

        resultado.set(
            f"📍 {ciudad}\n"
            f"🌡️ Temp: {temp}°C\n"
            f"🤒 Sensación: {sensacion}°C\n"
            f"💧 Humedad: {humedad}%\n"
            f"🌬️ Viento: {viento} m/s\n"
            f"☁️ {desc}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))

# INTERFAZ
ventana = tk.Tk()
ventana.title("App del Clima")
ventana.geometry("300x250")

tk.Label(ventana, text="Ingresa una ciudad:").pack(pady=10)

entrada_ciudad = tk.Entry(ventana)
entrada_ciudad.pack(pady=5)

tk.Button(ventana, text="Consultar Clima", command=obtener_clima).pack(pady=10)

resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado).pack(pady=10)

ventana.mainloop()
