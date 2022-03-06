import qrcode
from datetime import datetime


def make_qrcode(text: str) -> None:
    now_time = datetime.now().strftime('%H-%M-%S')
    qr_name = f'qr_code{now_time}.png'

    qr = qrcode.QRCode(version=1, box_size=20, border=2)
    qr.add_data(text)

    img = qr.make_image()
    img.save(qr_name)
    return qr_name


make_qrcode('texto')
