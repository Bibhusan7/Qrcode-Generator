import qrcode

def create():
    qr = qrcode.QRCode(
        version = 5,
        box_size = 3,
        border = 2

    )
    qr.add_data("Name: Shikhar\nAge: 16\nGender: Male")
    qr.make(fit=True)
    img = qr.make_image(fill = "black", back_color = "white")
    img.save("MyQRcode.png")

create()