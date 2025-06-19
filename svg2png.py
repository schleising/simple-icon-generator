from pathlib import Path

import cairosvg

logo_path = Path().home() / 'Downloads' / 'logos'

for file in logo_path.iterdir():
    # Convert the .svg file to .png
    cairosvg.svg2png(url=file.as_posix(), write_to=(logo_path / f'{file.stem}16.png').as_posix(), scale=1)
    cairosvg.svg2png(url=file.as_posix(), write_to=(logo_path / f'{file.stem}32.png').as_posix(), scale=2)
    cairosvg.svg2png(url=file.as_posix(), write_to=(logo_path / f'{file.stem}48.png').as_posix(), scale=3)
    cairosvg.svg2png(url=file.as_posix(), write_to=(logo_path / f'{file.stem}128.png').as_posix(), scale=8)
