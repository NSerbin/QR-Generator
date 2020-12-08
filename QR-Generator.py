import pyqrcode
import png

def QRGenerator():
    """ Function to make QR Code """
    
    # Insert The web adress 
    url = input("Enter the web adress: ")
    # Name of QR code png file
    name = input("Enter image name to save: ")+ ".png"
    # Creating QR code
    qr = pyqrcode.create(url)
    # Saving QR code as a png file
    qr.png(name, scale =6)

if __name__ == "__main__":
    QRGenerator()
