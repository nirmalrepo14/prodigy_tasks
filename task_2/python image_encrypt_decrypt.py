from PIL import Image

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    width, height = image.size
    encrypted_image = Image.new(image.mode, (width, height))

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            encrypted_pixel = tuple((p + key) % 256 for p in pixel)
            encrypted_image.putpixel((x, y), encrypted_pixel)

    encrypted_image.save("encrypted_image.png")
    print("Image encrypted successfully!")

def decrypt_image(image_path, key):
    image = Image.open(image_path)
    width, height = image.size
    decrypted_image = Image.new(image.mode, (width, height))

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            decrypted_pixel = tuple((p - key) % 256 for p in pixel)
            decrypted_image.putpixel((x, y), decrypted_pixel)

    decrypted_image.save("decrypted_image.png")
    print("Image decrypted successfully!")

def main():
    choice = input("Enter 'E' to encrypt image or 'D' to decrypt image: ").upper()
    image_path = "exampleimage.png"
    key = int(input("Enter the encryption/decryption key (an integer): "))

    if choice == 'E':
        encrypt_image(image_path, key)
    elif choice == 'D':
        decrypt_image(image_path, key)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
