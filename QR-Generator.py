import pyqrcode
import sys
import logging

# Configure basic logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_qr_code(url: str, file_name: str) -> None:
    """
    Generates a QR code from a given URL and saves it as a PNG file.

    Parameters:
        url (str): The URL to encode in the QR code.
        file_name (str): The name of the file to save the QR code.

    Raises:
        Exception: If an error occurs during QR code generation or file saving.
    """
    try:
        qr = pyqrcode.create(url)
        qr.png(file_name, scale=6)
        logging.info(f"QR Code successfully saved as {file_name}")
    except Exception as e:
        logging.error(f"Failed to create or save QR code: {e}")
        raise

def main():
    """ Main function to get user input and generate QR code. """
    try:
        url = input("Enter the web address: ")
        name = input("Enter the image name to save: ") + ".png"
        generate_qr_code(url, name)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
