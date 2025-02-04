import numpy as np
from PIL import Image

def decrypt_image(encrypted_image_path, key_path, output_path):
    # Read the encrypted image
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_image_array = np.array(encrypted_image)

    # Load the key
    key = np.load(key_path)

    # Decrypt the image
    decrypted_image = np.bitwise_xor(encrypted_image_array, key)

    # Save the decrypted image
    decrypted_image = Image.fromarray(decrypted_image)
    decrypted_image.save(output_path)

    print(f"Decrypted image saved as {output_path}")

if __name__ == '__main__':
    encrypted_image_path = 'encrypted_image.bmp'
    key_path = 'secret_key.npy'
    output_path = 'decrypted_image.jpg'
    decrypt_image(encrypted_image_path, key_path, output_path)
