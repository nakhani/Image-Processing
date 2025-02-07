import numpy as np
from PIL import Image

def decrypt_image(encrypted_image_path, key_path):
    
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_image_array = np.array(encrypted_image)

    
    key = np.load(key_path)

    
    decrypted_image = np.bitwise_xor(encrypted_image_array, key)

   
    decrypted_image = Image.fromarray(decrypted_image)
    decrypted_image.save('decrypted_image.jpg')

if __name__ == '__main__':
    encrypted_image_path = 'encrypted_image.bmp'
    key_path = 'secret_key.npy'
    decrypt_image(encrypted_image_path, key_path)
