from PIL import Image
import os

def convert_to_rgb(grayscale_image_path, output_image_path):
    # Abre la imagen en escala de grises
    grayscale_image = Image.open(grayscale_image_path)

    # Convierte la imagen en escala de grises a RGB
    rgb_image = grayscale_image.convert("RGB")

    # Guarda la imagen convertida
    rgb_image.save(output_image_path)

# Ejemplo de uso
input_folder = './custom_dataset/plates_29_09'  # Cambia esto por la carpeta donde están tus imágenes
output_folder = './custom_dataset/plates_RGB'       # Cambia esto por la carpeta donde quieres guardar las imágenes

# Convierte todas las imágenes en la carpeta
for image_file in os.listdir(input_folder):
    grayscale_image_path = os.path.join(input_folder, image_file)
    output_image_path = os.path.join(output_folder, image_file)
    convert_to_rgb(grayscale_image_path, output_image_path)

print("Conversión completada.")
