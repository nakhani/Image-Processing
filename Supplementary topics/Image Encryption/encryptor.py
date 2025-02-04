import numpy as np
from PIL import Image
import os

def encrypt_image(image_path, output_path, key_path):
    
    image = Image.open(image_path)
    image_array = np.array(image)

    # Generate a random key
    key = np.random.randint(0, 256, size=image_array.shape, dtype=np.uint8)

    # Encrypt the image
    encrypted_image = np.bitwise_xor(image_array, key)

    # Save the encrypted image
    encrypted_image = Image.fromarray(encrypted_image)
    encrypted_image.save(output_path)

    # Save the key
    np.save(key_path, key)

    print(f"Encrypted image saved as {output_path}")
    print(f"Secret key saved as {key_path}")

if __name__ == '__main__':
    image_path = 'input_image.jpg'
    output_path = 'encrypted_image.bmp'
    key_path = 'secret_key.npy'
    encrypt_image(image_path, output_path, key_path)
