import qrcode
from datetime import datetime


def make_qrcode(text: str, filename: str = None) -> None:
    if not filename:
        now_time = datetime.now().strftime('%H-%M-%S')
        filename = f'qr_code{now_time}.png'

    qr = qrcode.QRCode(version=1, box_size=20, border=2)
    qr.add_data(text)

    img = qr.make_image()
    img.save(filename)
    return filename
