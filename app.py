from barcode import EAN13
from barcode.writer import ImageWriter

number = '075323782312'
code = EAN13(number, writer = ImageWriter())
code.save("NewCode")