from PIL import Image,ImageTk


def Imagenes(ruta):
    imagen_pil = Image.open(ruta).convert("RGBA")
    boton_ancho, boton_alto =25, 25
    # Obtener dimensiones originales de la imagen
    img_ancho, img_alto = imagen_pil.size
    # Calcular escala para mantener proporción
    factor_escala = min(boton_ancho / img_ancho, boton_alto / img_alto)
    nuevo_ancho = int(img_ancho * factor_escala)
    nuevo_alto = int(img_alto * factor_escala)
    # Redimensionar imagen manteniendo proporción
    imagen_pil = imagen_pil.resize((nuevo_ancho, nuevo_alto), Image.Resampling.LANCZOS)
    imagen_tk = ImageTk.PhotoImage(imagen_pil)
    return imagen_tk



