import os
from pdf2image import convert_from_path


pages = convert_from_path("S2P1.pdf", 300)
pdf_file = pages[0].save("1.jpg", "JPEG")