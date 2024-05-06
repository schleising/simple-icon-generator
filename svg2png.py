from pathlib import Path

import cairosvg

logo_path = Path().home() / 'Downloads' / 'logos'

for file in logo_path.iterdir():
    # Open the .svg file
    with open(file, 'r') as f:
        svg = f.read()

    # Convert the .svg file to .png
    cairosvg.svg2png(url=file.as_posix(), write_to=(logo_path / f'{file.stem}.png').as_posix())
