import colorsys
import sys

# Use Pillow to create a new image with cornflowerblue background and a white letter C
from PIL import Image, ImageDraw, ImageFont
from PIL.Image import Resampling

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
    y = (size - height) / 2 - int(size / 5)

    # Draw a white letter C on the image in bold Helvetica in the center
    draw.text((x, y), text=text, fill=text_fill, font=font, stroke_width=3)

    # Save the image to a file
    badge_img.save(f'icons/badge-{size}x{size}.png')

def create_icon(size: int, text: str, text_fill: str, red: int, green: int, blue: int, create_ico = False, create_maskable = False):
    # Create a new image with a cornflowerblue background
    icon_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))

    # Create a Draw object
    draw = ImageDraw.Draw(icon_img)

    # Draw a rounded rectangle with a fill color
    draw.rounded_rectangle((0, 0, size, size), radius=int(size * 0.2), fill=(red, green, blue))

    # Load the helvetica font in Mac OS
    font = ImageFont.truetype('~/Library/Fonts/Roboto-Medium.ttf', size - 40)

    # Get the size of the text
    x_start, y_start, x_end, y_end = draw.textbbox((0, 0), text, font=font, stroke_width=3)

    # Calculate the width and height of the text
    width = x_end - x_start
    height = y_end - y_start

    # Calculate the x and y position to center the text
    x = (size - width) / 2
    y = ((size - height) / 2) - int(size / 6)

    # Draw a white letter C on the image in bold Helvetica in the center
    draw.text((x, y), text=text, fill=text_fill, font=font, stroke_width=3)

    # Save the image to a file
    icon_img.save(f'icons/android-chrome-{size}x{size}.png')

    # Create the favicon.ico file if create_ico is True
    if create_ico:
        # Set the size of the favicon
        favicon_size = 48

        # Resize the image to 48x48
        favicon_img = icon_img.resize((favicon_size, favicon_size), Resampling.NEAREST)

        # Save the image to a file
        favicon_img.save(f'icons/favicon-{favicon_size}x{favicon_size}.ico')

    # Create the maskable icon if create_maskable is True
    if create_maskable:
        # The maskable icon needs to be reduced by 20% in size and centered in a size x size image
        maskable_size = int(size * 0.8)

        # Create a new image with a cornflowerblue background
        maskable_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))

        # Create a Draw object
        draw = ImageDraw.Draw(maskable_img)

        # Draw a rounded rectangle with a fill color
        draw.rectangle((0, 0, size, size), fill=(red, green, blue))

        # Calculate the x and y position to center the maskable icon
        x = (size - maskable_size) // 2
        y = (size - maskable_size) // 2

        # Resize the image to maskable_size x maskable_size
        icon_img = icon_img.resize((maskable_size, maskable_size), Resampling.NEAREST)

        # Paste the maskable icon in the center of the image
        maskable_img.paste(icon_img, (x, y))

        # Save the image to a file
        maskable_img.save(f'icons/android-chrome-maskable-{size}x{size}.png')

def main():
    # Get the first parameter from the command line
    letter = sys.argv[1]

    # Set the color of the icon to cornflowerblue using the HLS color model
    h = 218.54 / 360
    s = 79.19 / 100
    l = 75 / 100

    # Convert the HLS color to RGB
    r, g, b = [int(i * 255) for i in colorsys.hls_to_rgb(h, l, s)]

    create_badge(192, letter, 'white')
    create_icon(144, letter, 'white', r, g, b)
    create_icon(192, letter, 'white', r, g, b)
    create_icon(512, letter, 'white', r, g, b, create_ico=True, create_maskable=True)

if __name__ == '__main__':
    main()
