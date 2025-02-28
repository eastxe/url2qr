# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click",
#     "qrcode[pil]",
# ]
# ///

import click
import qrcode

@click.command()
@click.argument("url")
def main(url):
    output = "qrcode.png"
    img = qrcode.make(url)
    img.save(output)
    click.echo(f"QR code saved to {output}")

if __name__ == "__main__":
    main()

