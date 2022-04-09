from reportlab.pdfgen import canvas
from random import getrandbits

class PDF():
    def make_pdf(images):
        title = f"tmp_{getrandbits(24)}.pdf"
        pdf = canvas.Canvas(title)
        pdf.setTitle("Exercícios de Potenciação")
        pdf.drawCentredString(300, 770, "Exercícios de potenciação")
        for e, i in enumerate(images):
            pdf.drawInlineImage(i, x=-200, y=650+(e*100), height=100, preserveAspectRatio=True)
        pdf.save()
        return title