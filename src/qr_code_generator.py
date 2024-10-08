# pip install qrcode
# pip install Pillow

import qrcode

img = qrcode.make('https://codewithmosh.com/')

type(img)

img.save("mosh.png")