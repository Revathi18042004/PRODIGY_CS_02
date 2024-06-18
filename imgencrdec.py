from PIL import Image
import numpy as np

def process_image(image_path, key):
    image = Image.open(image_path).convert('RGB')
    image_array = np.array(image)
    processed_array = image_array ^ key
    return Image.fromarray(processed_array)

def main():
    operation = input("Do you want to encrypt or decrypt an image? (enter 'encrypt' or 'decrypt'): ").strip().lower()

    if operation not in ['encrypt', 'decrypt']:
        print("Invalid operation. Please enter 'encrypt' or 'decrypt'.")
        return

    image_name = input("Enter the name of the image file (including extension): ")
    key = int(input("Enter the encryption/decryption key (int): "))

    if operation == 'encrypt':
        encrypted_image = process_image(image_name, key)
        encrypted_image_path = "encrypted_img.png"
        encrypted_image.save(encrypted_image_path, 'PNG')
        encrypted_image_jpg_path = "encrypted_img.jpg"
        encrypted_image.save(encrypted_image_jpg_path, 'JPEG')
        print(f"Encrypted image saved as '{encrypted_image_jpg_path}'")

    elif operation == 'decrypt':
        # Decrypt the image from the PNG file, then save as JPEG
        encrypted_image_path = "encrypted_img.png"
        decrypted_image = process_image(encrypted_image_path, key)
        decrypted_image_path = f"decrypted_{image_name}"
        decrypted_image.save(decrypted_image_path, 'JPEG')
        print(f"Decrypted image saved as '{decrypted_image_path}'")

if __name__ == "__main__":
    main()
