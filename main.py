import colorsys
import sys

# Use Pillow to create a new image with cornflowerblue background and a white letter C
from PIL import Image, ImageDraw, ImageFont

def create_badge(size: int, text: str, text_fill: str):
    # Create a new image with a cornflowerblue background
    badge_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))

    # Create a Draw object
    draw = ImageDraw.Draw(badge_img)

    # Load the helvetica font in Mac OS
    font = ImageFont.truetype('~/Library/Fonts/Roboto-Medium.ttf', size)

    # Get the size of the text
    x_start, y_start, x_end, y_end = draw.textbbox((0, 0), text, font=font, stroke_width=3)

    # Calculate the width and height of the text
    width = x_end - x_start
    height = y_end - y_start

    # Calculate the x and y position to center the text
    x = (size - width) / 2
    y = (size - height) / 2 - int(size / 6.4)

    # Draw a white letter C on the image in bold Helvetica in the center
    draw.text((x, y), text=text, fill=text_fill, font=font, stroke_width=3)

    # Save the image to a file
    badge_img.save(f'icons/badge-{size}x{size}.png')

def create_icon(size: int, text: str, text_fill: str, red: int, green: int, blue: int, create_ico = False):
    # Create a new image with a cornflowerblue background
    icon_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))

    # Create a Draw object
    draw = ImageDraw.Draw(icon_img)

    # Draw a rounded rectangle with a fill color
    draw.rounded_rectangle((0, 0, size, size), radius=int(size * 0.2), fill=(red, green, blue))

    # Load the helvetica font in Mac OS
    font = ImageFont.truetype('~/Library/Fonts/Roboto-Medium.ttf', size)

    # Get the size of the text
    x_start, y_start, x_end, y_end = draw.textbbox((0, 0), text, font=font, stroke_width=3)

    # Calculate the width and height of the text
    width = x_end - x_start
    height = y_end - y_start

    # Calculate the x and y position to center the text
    x = (size - width) / 2
    y = ((size - height) / 2) - int(size / 6.4)

    # Draw a white letter C on the image in bold Helvetica in the center
    draw.text((x, y), text=text, fill=text_fill, font=font, stroke_width=3)

    # Save the image to a file
    icon_img.save(f'icons/android-chrome-{size}x{size}.png')

    # Create the favicon.ico file if create_ico is True
    if create_ico:
        # Set the size of the favicon
        favicon_size = 48

        # Resize the image to 48x48
        favicon_img = icon_img.resize((favicon_size, favicon_size), Image.NEAREST)

        # Save the image to a file
        favicon_img.save(f'icons/favicon-{favicon_size}x{favicon_size}.ico')

def main():
    # Get the first parameter from the command line
    letter = sys.argv[1]

    # Set the color of the icon to cornflowerblue using the HLS color model
    h = 7 / 360
    s = 65 / 100
    l = 55 / 100

    # Convert the HLS color to RGB
    r, g, b = [int(i * 255) for i in colorsys.hls_to_rgb(h, l, s)]

    create_badge(192, letter, 'white')
    create_icon(144, letter, 'white', r, g, b)
    create_icon(192, letter, 'white', r, g, b)
    create_icon(512, letter, 'white', r, g, b, create_ico=True)

if __name__ == '__main__':
    main()
