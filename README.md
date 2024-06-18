Image Encryption Tool:

This is a simple image encryption tool developed in Python that allows users to encrypt and decrypt images using pixel manipulation.
The tool performs operations like swapping pixel values or applying a basic mathematical operation (XOR) to each pixel.

Features:

Pixel Manipulation: The tool manipulates pixels of the image by applying XOR with a user-provided key for encryption and decryption.

Encryption and Decryption: Users can both encrypt and decrypt images using the same tool.

How It Works:
Encryption: The tool takes an input image and a key from the user. It then encrypts the image by applying the XOR operation with the key to each pixel.

Decryption: For decryption, the tool takes the encrypted image and the same key from the user. 
It reverses the encryption process by applying the XOR operation again with the same key, resulting in the original image.


Requirements:

Python 3.x
Pillow library (pip install Pillow)







