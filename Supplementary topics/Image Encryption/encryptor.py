import numpy as np
from PIL import Image


def encrypt_image(image_path):
    
    image = Image.open(image_path)
    image_array = np.array(image)

   
    key = np.random.randint(0, 256, size=image_array.shape, dtype=np.uint8)

    
    encrypted_image = np.bitwise_xor(image_array, key)

   
    encrypted_image = Image.fromarray(encrypted_image)
    encrypted_image.save('encrypted_image.bmp')

    
    np.save('secret_key.npy', key)

    
if __name__ == '__main__':
    image_path = 'image.png'
    encrypt_image(image_path)
