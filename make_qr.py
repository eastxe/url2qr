# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "qrcode[pil]",
# ]
# ///

import qrcode

def main():
    url = "https://www.example.com"
    img = qrcode.make(url)
    img.save("qrcode.png")

if __name__ == "__main__":
    main()

